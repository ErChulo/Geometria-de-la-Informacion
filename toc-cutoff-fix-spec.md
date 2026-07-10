# Spec — Fix the "Índice General" (Table of Contents) Bottom-Edge Cutoff

Short name: `toc-cutoff-fix`

Status: Draft v1 — pre-implementation. No code changes yet.

---

## 1. Problem statement

The first page of the **Índice General** (Table of Contents) of the LaTeX book
*"Geometría de la información"* is being clipped at the **bottom edge** — the
last entry's title, dot leaders, or page number is partially hidden below the
printable area. The symptom is reproducible, the user has not recently edited
TOC-related files, and the issue is blocking the final review pass.

The book is otherwise close to print-ready; this is the last layout blocker.

---

## 2. Goals & non-goals

### Goals
1. Eliminate the bottom-edge clipping on the first TOC page so it reads as a
   professional book.
2. Keep the visual feel **minimal, classic, dot-leader** (no boxed TOC,
   no banners, no "Contents" replacement).
3. Preserve the **bottom = 2 in** bottom margin in `main.tex` if feasible; if
   not, allow the smallest possible reduction.
4. Keep all changes **minimal** — adjust TOC spacing and `\emergencystretch`
   first; touch margins only if necessary.
5. If the TOC naturally flows onto a 2nd/3rd page, allow that, but keep the
   break clean (no orphaned chapter title on page 1).
6. Output must be print-quality **and** readable on screen (PDF).

### Non-goals
- Redo the cover page, title page, or chapter typography.
- Switch from `tocloft` to a different TOC package.
- Change the paper size, font, or overall design language.
- Add page numbers / ornaments the book doesn't already have.

---

## 3. User preferences (gathered via interview)

| Topic | Decision |
|---|---|
| What is being clipped | Last entry's title/dots/page number on first TOC page |
| Number of entries on first page | User unsure — agent should assume "moderate" and design for graceful overflow |
| Recent edits | None — problem appeared without recent changes |
| Visual style of TOC | Minimal dot-leader, classic book style |
| TOC title | Keep "Índice General" (current) |
| TOC depth | **2** — chapters + parts / sub-parts |
| Numeric TOC entries | Only main chapters + prologue in TOC; do NOT show appendices / solutions / bibliography |
| Scope of fix | Minimal — only TOC spacing + `\emergencystretch`; do not touch other geometry/margins |
| Pagination policy | Allow natural overflow onto more pages; tidy chapter numbering |
| Bottom margin | Ok to reduce slightly if unavoidable; preserve 2 in if possible |
| Output target | Both print and PDF |

---

## 4. Root-cause analysis (prioritized)

Reference files: `src/main.tex`, `src/style-book.sty`, `src/Prologo.tex`,
`src/capitulo0.tex`.

### A. **PRIMARY: `geometry` calculates `\textheight` before `linespread`**
The `\usepackage{geometry}` (with `heightrounded`) is loaded in `main.tex`
*before* `\usepackage{style-book}`. At the moment `geometry` rounds
`\textheight` to a multiple of `\baselineskip`, it uses the default
`\linespread`. Then `style-book.sty` applies `\linespread{1.04}` and
`\setlength{\headheight}{26pt}`. The actual body becomes slightly taller than
the `\textheight` `geometry` reserved, and on content-heavy pages (with
`\flushbottom` active) the last line is pushed *below* the bottom margin —
exactly the clipping the user is seeing on the TOC first page.

### B. **SECONDARY: `\flushbottom` + rigid `tocloft` spacing**
`\flushbottom` (in `style-book.sty`) forces every page to stretch to the
bottom margin. The TOC entries use **fixed** skips:

```latex
\setlength{\cftbeforesecskip}{0.5em}
\setlength{\cftbeforesubsecskip}{0.3em}
```

They contain no `plus …` glue, so LaTeX cannot absorb the extra vertical
mismatch from cause A. The TOC is the page with the *least* stretchable
content → it overflows first.

### C. **TERTIARY: depth mismatch**
Currently `\setcounter{tocdepth}{1}` — only chapters. User wants
**depth = 2** (chapters + parts / sub-parts). That *adds* rows; combined
with A and B it pushes more content toward the bottom-edge problem.
Need to be careful: depth change must be coordinated with the spacing fix
so it doesn't worsen the clipping.

### D. **Aesthetic gap**
The current `style-book.sty` only customizes `\cfttoctitlefont`,
`\cftsecfont`, `\cftsubsecfont`, `\cftsecleader`, and three `\cftbefore…skip`
lengths. For a "professional book" feel at depth 2 we should also tune:

- `\cftchapfont`, `\cftchappagefont` (chapter title + page number font)
- `\cftdotsep` (dot leader spacing)
- optionally bolding/indentation of chapters vs sub-parts

---

## 5. Proposed solution (minimal patch)

### 5.1 `src/main.tex`

**Goal:** re-order so `geometry` knows the real `\headheight` and `\linespread`;
wrap the TOC in a local `\raggedbottom` + larger `\emergencystretch`; bump
`tocdepth` to 2.

Replace:

```latex
\geometry{letterpaper, inner=1.75in, outer=1in, top=1in, bottom=2in, heightrounded}
```

with the `geometry` call staying where it is (it's already loaded), but **add
explicit `headheight=26pt`** so it matches what `style-book.sty` declares:

```latex
\geometry{
  letterpaper,
  inner=1.75in, outer=1in,
  top=1in, bottom=2in,
  heightrounded,
  headheight=26pt,        % <-- match style-book.sty
  headsep=18pt            % <-- clean spacing below running header
}
```

Then in the `\frontmatter` block, replace:

```latex
\setcounter{tocdepth}{1}
\tableofcontents
\cleardoublepage
\markboth{}{}    % limpia marcas de TOC
\pagestyle{fancy}
```

with:

```latex
\setcounter{tocdepth}{2}    % chapters + parts / subparts
\begingroup
  \raggedbottom              % let TOC pages have natural height
  \emergencystretch=3em      % give LaTeX room to reflow
  \tableofcontents
  \cleardoublepage
\endgroup
\markboth{}{}                % limpia marcas de TOC
\pagestyle{fancy}
```

Notes:
- `\raggedbottom` is scoped to the `\begingroup…\endgroup` so it does NOT
  affect chapter pages (those keep `\flushbottom` as the book expects).
- `\emergencystretch=3em` is local to the TOC, leaving the rest of the book
  with the existing `2em` value.

### 5.2 `src/style-book.sty`

Add elasticity to TOC skips so LaTeX can absorb small mismatches globally:

```latex
% Before:
\setlength{\cftbeforesecskip}{0.5em}
\setlength{\cftbeforesubsecskip}{0.3em}

% After:
\setlength{\cftbeforesecskip}{0.5em plus 2pt minus 1pt}
\setlength{\cftbeforesubsecskip}{0.3em plus 1pt minus 1pt}
```

Add professional-book typography for chapters vs sub-parts:

```latex
\renewcommand{\cftchapfont}{\sffamily\bfseries\color{AccentDark}}
\renewcommand{\cftchappagefont}{\sffamily\bfseries\color{AccentDark}}
\renewcommand{\cftchapaftersnum}{\hspace{0.5em}}  % space after chapter number
\renewcommand{\cftdotsep}{2.5}                    % tighter classical dot leader
\renewcommand{\cftsubsecfont}{\sffamily\small\mdseries}
\renewcommand{\cftsubsecpagefont}{\sffamily\small\color{Accent}}
```

Add a thin, Accent-colored ornamental rule under the "Índice General" title
(to match chapter titles' `titlerule`):

```latex
\renewcommand{\cftaftertoctitle}{%
  \vspace{4pt}\color{Accent}\hrule height 0.4pt\vspace{6pt}%
}
```

### 5.3 Appendices / backmatter in TOC

Confirm in `src/respuestas.tex`, `src/apendice_mathematica.tex`, and
`src/bibliografia.tex` that any `\addcontentsline{toc}{chapter}{…}` is
**intentional**. Per user preference, do NOT add new backmatter lines to the
TOC. Existing lines (Prólogo, Apéndice Mathematica, Bibliografía) should be
hidden from the printed TOC.

Implementation options (no code change yet, picking later):

1. **Local override** — wrap those `\include` files conditionally so their
   `\addcontentsline` calls run only when a `keepbackmatterintoc` flag is set.
2. **Sed post-pass** — strip unwanted TOC lines via `makeindex` / a `sed` step
   in the Makefile (less LaTeX-idiomatic).
3. **New commands** — replace `\addcontentsline` in those files with a no-op
   helper `\AddToTocMaybe` that respects a flag.

Recommend option 3 for cleanness.

---

## 6. Acceptance criteria

The fix is "done" when **all** of these hold:

1. **AC-1 — No clipping.** Open the rendered TOC: the last row of every TOC
   page sits entirely inside the printable area (no clipping at the bottom
   edge).
2. **AC-2 — Hierarchy respected.** TOC shows: Prólogo, Capítulos 0–7.
   Sub-parts of each chapter are visible at depth 2 (if the book has them).
   Appendices, Respuestas, and Bibliografía are NOT in the printed TOC.
3. **AC-3 — Minimal change.** Bottom margin in `main.tex` is still ≥ 1.5 in
   (preferably 2 in). `\flushbottom` is unchanged globally (only the TOC
   group uses `\raggedbottom`).
4. **AC-4 — Professional book look.** Chapters in the TOC use a chapter-style
   font (sans, bold, Accent color). Sub-parts are visibly lighter
   (`\small`, optionally not bold). Dot leader is classical and tight.
   "Índice General" has the small accent rule under it.
5. **AC-5 — Pagination clean.** No orphan single-line TOC entries on page 1;
   no broken page break right after a chapter title.
6. **AC-6 — Build clean.** Repeating `make build` twice yields a build with
   no new warnings about overflow, underfull/overfull boxes on the TOC pages,
   or undefined references attributable to the change.
7. **AC-7 — Backmatter untouched.** All chapter content (`capitulo0`…`7`,
   Prologo, Mathematica appendix body, bibliography) is unchanged in
   pagination, layout, or content.

---

## 7. Verification commands

```bash
cd src
make clean
make build              # 2-pass LaTeX (Makefile already does this)
# Inspect TOC pages in the resulting main.pdf:
#   - page(s) containing "Índice General" — confirm no clipping
#   - bottom of each TOC page — last row fully visible
#   - all chapter rows visible without orphan titles
# Optional LaTeX diagnostics inside the build:
#   grep -nE 'Overfull \\vbox|Underfull \\vbox' main.log  # expect none on TOC pages
#   grep -nE 'Undefined|circular' main.log              # must be empty
```

Manual smoke test: render the produced PDF page-by-page, eyeball pages 1–N
where N is the last TOC page. All TOC pages should look like a normal book
TOC; the first one must NOT have anything poking out below the bottom margin.

---

## 8. Open questions / future spec items

These remain open (do **not** block implementation of the fix):

- **Q1.** Is `\chapternumberline` styling desired for chapters in the TOC
  ("Capítulo 1" prefix), or is the chapter title alone enough? Default would
  be to add `\chapternumberline` styling (consistent with chapter headers).
- **Q2.** Should the Roman-numeral prologue page in the TOC use a unique
  roman numeral (`i`, `ii`) or follow the main page numbering? Default: keep
  current behavior (TOC uses book-class default — the prologue chapter
  appears as "Prólogo — v" since it's in `\frontmatter`).
- **Q3.** Should the print run use `\openright` forcing odd-page chapter
  starts? Currently `twoside` is set but `\openright` is not explicitly
  toggled. Affects pagination of TOC vs body, but not the TOC clipping
  itself.
- **Q4.** Should the TOC have an "Lot of Figures / Lot of Tables" follow-up?
  Not requested, kept out of scope.

---

## 9. Out-of-scope improvements (for follow-up)

These are NOT part of this spec but are worth tracking for after the TOC is
fixed:

- Replace `\emergencystretch=…` magic numbers with a microtype-tuned value.
- Align `geometry`'s `headsep` and `footskip` with `fancyhdr` so the running
  header height and footer never collide.
- Review whether `\ChapterBigNumber` (66 pt) causes any chapter title to
  spill onto a second line for very long titles — independent of TOC.
- Consider a `\frontmatter` TOC redesign with a decorative rule between
  chapter groups (Prólogo / Capítulos) for a publisher-grade look.

---

## 10. Files that will be touched by the implementation

| File | Reason |
|---|---|
| `src/main.tex` | Re-compute `\textheight` correctly via `headheight=26pt`; wrap TOC in `\raggedbottom`+`\emergencystretch` group; set `tocdepth=2`. |
| `src/style-book.sty` | Add `plus`/`minus` glue to TOC skips; explicitly style `\cftchapfont`, `\cftchappagefont`, `\cftsubsecfont`, `\cftsubsecpagefont`, `\cftdotsep`; add rule under TOC title. |
| `src/respuestas.tex` *(maybe)* | Replace `\addcontentsline` with a guarded helper if option 3 is adopted for hiding backmatter. |
| `src/apendice_mathematica.tex` *(maybe)* | Same as above. |
| `src/bibliografia.tex` *(maybe)* | Same as above. |

No file content or chapter text is modified.

---

## 11. Risks

- **R1.** Adding `headheight=26pt` to `geometry` *after* `style-book` defines
  it again could cause a "you have specified a headheight that's too small"
  warning. Mitigation: declare `headheight` **only** in `geometry`, have
  `style-book.sty` leave that variable alone. If a warning persists,
  increase to `28pt`.
- **R2.** Bumping `tocdepth` to 2 may reveal long sub-section titles in the
  TOC that don't fit on one line. Mitigation: tighten `\cftbeforesubsecskip`
  and use `\small` for sub-parts (already in the patch).
- **R3.** Wrapping the TOC in `\raggedbottom` could create visually less
  "flush" TOC pages compared to chapter pages. Mitigation: scope to the
  `\begingroup…\endgroup` so it does NOT carry over to chapter pages.
- **R4.** Hiding backmatter from the printed TOC may surprise the reader if
  some of those sections (Respuestas, Mathematica) need to be discoverable.
  Mitigation: per user preference; future spec can revisit if needed.

---

## 12. Definition of done

- All ACs in §6 pass on a clean build.
- No new LaTeX warnings in `main.log` on TOC pages.
- Visual review done by the user (they had asked `¿puedo asistir?`).
- Commit message references `toc-cutoff-fix` and ACs verified.

.PHONY: build clean view help

# Configuración
MAIN_TEX = main.tex
PDF_OUTPUT = main.pdf
LATEX_CMD = pdflatex
LATEX_FLAGS = -interaction=nonstopmode -file-line-error

help:
	@echo "Comandos disponibles:"
	@echo "  make build    - Compila el libro (2 pasadas)"
	@echo "  make clean    - Limpia archivos temporales"
	@echo "  make view     - Abre el PDF generado"
	@echo "  make help     - Muestra esta ayuda"

build:
	@echo "🔨 Compilando $(MAIN_TEX)..."
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_TEX)
	@echo "📖 Segunda pasada para índices y referencias..."
	$(LATEX_CMD) $(LATEX_FLAGS) $(MAIN_TEX)
	@echo "✅ Compilación completada: $(PDF_OUTPUT)"

clean:
	@echo "🧹 Limpiando archivos temporales..."
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.synctex.gz *.auxlock
	@echo "✨ Hecho"

view: build
	@echo "👀 Abriendo PDF..."
	xdg-open $(PDF_OUTPUT) || open $(PDF_OUTPUT) || echo "Abre manualmente: $(PDF_OUTPUT)"
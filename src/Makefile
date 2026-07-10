.PHONY: build clean view help notebooks-fast

# Configuración
MAIN_TEX = main.tex
PDF_OUTPUT = main.pdf
LATEX_CMD = pdflatex
LATEX_FLAGS = -interaction=nonstopmode -file-line-error

NB_DIR = ../notebooks

help:
	@echo "Comandos disponibles:"
	@echo "  make build          - Compila el libro (2 pasadas)"
	@echo "  make clean          - Limpia archivos temporales"
	@echo "  make view           - Abre el PDF generado"
	@echo "  make notebooks-fast - Smoke-test del setup de notebooks/"
	@echo "  make help           - Muestra esta ayuda"

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

# -----------------------------------------------------------------------------
# Companion notebooks (Fase 1: smoke test). Fase 2+ añadirá ejecutores
# individuales (e.g., `make notebook-cap1-fisher-tensor` corre el piloto).
# -----------------------------------------------------------------------------
notebooks-fast:
	@echo "🧪 Smoke test de notebooks/utils.py..."
	@python3 -c "import sys; sys.path.insert(0, '$(NB_DIR)'); import utils; exit(utils._smoke_test())" \
	  && echo "✅ utils.py OK" \
	  || (echo "❌ Smoke test falló. ¿Instalaste requirements.txt? (pip install -r requirements.txt)" && exit 1)
	@echo "📂 notebooks/:" && ls -la $(NB_DIR)
	@echo "✅ Setup verificado."
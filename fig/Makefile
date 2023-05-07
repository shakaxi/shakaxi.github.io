TEX := $(shell find $(shell pwd) -iname '*.tex')
PDF := $(subst .tex,.pdf, $(TEX))
AUX := $(subst .tex,.aux, $(TEX))
LOG := $(subst .tex,.log, $(TEX))
PNG := $(subst .pdf,.png, $(PDF))

TEX2PDF := /usr/bin/pdflatex
PDF2PNG := /usr/bin/convert
PDF2PNGOPT := -density 100

%.png: %.pdf
	@$(PDF2PNG) $(PDF2PNGOPT) $< $@

%.pdf: %.tex
	@$(TEX2PDF) $<

.phony: default clean clear
default: $(PNG)
clean:
	@-rm -f $(AUX) $(LOG) $(PDF)
clear: clean
	@-rm -f $(PNG)

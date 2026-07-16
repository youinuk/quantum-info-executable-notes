.PHONY: validate test notes review clean

validate:
	python scripts/validate_mapping.py

test:
	pytest -q

notes:
	latexmk -pdf main_notes.tex

review:
	latexmk -pdf main_review.tex

clean:
	latexmk -C main_notes.tex
	latexmk -C main_review.tex

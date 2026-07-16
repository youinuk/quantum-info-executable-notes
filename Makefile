.PHONY: validate test book review chapter06 clean

validate:
	python scripts/validate_mapping.py

test:
	pytest -q

book:
	latexmk -pdf main.tex

review:
	latexmk -pdf editions/review.tex

chapter06:
	latexmk -pdf editions/chapter06.tex

clean:
	latexmk -C main.tex
	latexmk -C editions/review.tex
	latexmk -C editions/chapter06.tex


install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py


test: 
	python -m pytest -vv --nbval -cov=mylib -cov=main 

all: install format test 





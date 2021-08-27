install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C app.py
	pylint --disable=R,C data_generation.py

test:
	python -m pytest -vv --cov=test_app.py

all:
	install lint test
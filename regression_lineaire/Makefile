NAME := linear_regression

.PHONY: install test clean

upgrade:
	@python3 -m pip install --upgrade pip

install:
	@python3 -m pip install -r packages.txt

all: | upgrade  install
		python3 reg_lineaire.py train data.csv -visual
clean:
	@python3 setup.py clean
	@rm -rf $(NAME)/__pycache__/	2> /dev/null || true
	@rm -rf car_price_parameters.txt			2> /dev/null || true
	@rm -rf __pycache__/		2> /dev/null || true
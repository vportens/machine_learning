NAME := linear_regression

.PHONY: install test clean


all: | upgrade  install
	@python3 reg_lineaire.py train data.csv -visual


upgrade:
	@python3 -m pip install --upgrade pip

install:
	@python3 -m pip install -r packages.txt


clean:
	@rm -rf $(NAME)/__pycache__/	2> /dev/null || true
	@rm -rf car_price_parameters.txt			2> /dev/null || true
	@rm -rf __pycache__/		2> /dev/null || true

re : clean all

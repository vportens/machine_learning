import regression_lineaire.core as core
import argparse

class CarPrice:
    def __init__(self):
        self.theta0 = 0.0
        self.theta1 = 0.0 
        self.load_parameters() 

    def prediction(self, km):
        return self.theta0 * km + self.theta1
    
    def train(self, dataset, visual = False):
        self.theta0, self.theta1 = core.linear_regression(dataset, visual)
        self.theta0 = self.theta0[0]
        self.theta1 = self.theta1[0]
        self.save_parameters(self.theta0, self.theta1)

    def save_parameters(self, theta0, theta1):
        with open('car_price_parameters.txt', 'w') as f:
            print(theta0, theta1)
            f.write(f"{theta0},{theta1}")

    def load_parameters(self):
        try:
            with open('car_price_parameters.txt', 'r') as f:
                params = f.read().split(',')
                if len(params) != 2:
                    return (print("Error: invalid parameter file."))
                try:
                    self.theta0 = float(params[0].strip())
                    self.theta1 = float(params[1].strip())
                except ValueError:
                    print("Error: invalid value in parameter file.")
        except FileNotFoundError:
            # le fichier n'existe pas encore, ne rien faire
            pass

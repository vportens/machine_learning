import regression_lineaire.core as core
import argparse
from reg import CarPrice
import sys


car = CarPrice()

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please enter the command train or predict")
        exit(1)
    if (sys.argv[1] == "train"):
        if (len(sys.argv) < 3):
            print("Please enter the path of the dataset, if you want to see the graph enter -visual as a third argument")
            exit(1)
        if (len(sys.argv) == 4 and sys.argv[3] == "-visual"):
            car.train(sys.argv[2], True)
        else : 
            car.train(sys.argv[2])

    if (sys.argv[1] == "predict"):
        if (len(sys.argv) != 3):
            print("Please enter the path of the dataset and the number of kilometers of the car")
            exit(1)
        try :
            km = int(sys.argv[2])
            print(car.prediction(int(sys.argv[2])))
        except ValueError as e:
            print("error: ", str(e))
            exit(1)

    if (sys.argv[1] != "train" and sys.argv[1] != "predict"):
        print("Please enter the command train or predict")


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
        print(car.prediction(int(sys.argv[2])))


#    parser = argparse.ArgumentParser(description='this program try to estimate the price of a car')

#    parser.add_argument("km", type=int, help="km of the car")

#    args = parser.parse_args()

#    if args.km :
#        core.linear_regression('./data.csv', args.km)
#    else:
#        print("Please enter the number of kilometers of the car")
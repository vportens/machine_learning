import numpy as np
from regression_lineaire.read_dataset import read_dataset
from regression_lineaire.gradiant_descente import gradient_descent
from regression_lineaire.model import model
from regression_lineaire.visual import show_model, show_data
from regression_lineaire.coefficient_derivation import coef_det

def linear_regression(dataset, visual = False):
    theta = np.zeros((2, 1))
    try :
        x, y = read_dataset(dataset)

        x = x.reshape(x.shape[0], 1)
        y = y.reshape(y.shape[0], 1)

        mean = x[0:].mean()
        std = x[0:].std()

        x_std = (x[0:] - mean) / std


        X = np.hstack((x_std, np.ones(x.shape)))
        theta_final = gradient_descent(X, y, theta, learning_rate= 0.015, n_ite = 1900)
        prediction = model(X, theta_final)


    

        a = (prediction[1] - prediction[0]) / (x[1] - x[0])
        b = prediction[1] - a*x[1]
        if (visual == True) :
            show_data(x, y)
            show_model(x, y, prediction)
    
        print("coef det: ", coef_det(y, prediction)) 

        return (a, b)
    except ValueError as e:
        print("error: ", str(e))
        exit(1)
#    show_model(x, y, prediction)
#    print("estimate price of the car: ", theta_final[0] * km + theta_final[1]) 
    

    #print("estimate price of the car: ", theta_final[0,0] * km + theta_final[0,1])



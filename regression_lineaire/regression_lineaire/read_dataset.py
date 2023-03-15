import pandas as pd
import regression_lineaire.visual as v
import os

def read_dataset(dataset, visual=False):
    try:
        if (os.path.isfile(dataset) == False):
            raise ValueError("Le fichier data.csv n'existe pas.")
        data = pd.read_csv(dataset, delimiter=",")
        if len(data) == 0:
            raise ValueError("Le fichier data.csv est corrompu.")
   # except ValueError as e:
    #    print(str(e))
        x = data.iloc[0:, 0].values
        y = data.iloc[0:, 1].values

        if (visual == True):
            v.show_data(x, y)
        return x, y
    except ValueError as e:
        print("error: ", str(e))
        exit(1)


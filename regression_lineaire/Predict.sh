#!/bin/bash

# Vérifiez si exactement un argument a été fourni
if [ "$#" -ne 1 ]; then
    echo "Usage: ./Predict.sh <value>"
    exit 1
fi

# Exécutez le script Python avec l'argument
python3 reg_lineaire.py predict $1
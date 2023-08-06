#!/bin/bash

# Vérifiez si au moins un argument a été fourni
if [ "$#" -lt 1 ]; then
    echo "Usage: ./Train.sh <csv_file> [-visual]"
    exit 1
fi

# Exécutez le script Python avec les arguments
if [ "$#" -eq 2 ]; then
    python3 reg_lineaire.py train $1 $2
else
    python3 reg_lineaire.py train $1
fi


import matplotlib.pyplot as plt
import numpy as np
from .model import model


def remove_plot(plot):
  if plot:
    line = plot.pop(0)
    line.remove()

def on_close(event):
  plt.figure(1)
  plt.close()

class My_event():
  def __init__(self):
    self.skip = False

  def on_click(self, event):
    self.skip = True

def show_data(x, y, theta_hist, X):

  fig = plt.figure(1)
  plt.title("Linear Regression over dataset")
  plt.xlabel("Mileage (km)")
  plt.ylabel("Prices (USD)")
  kms = list(x)
  prices = list(y)
  plt.scatter(kms, prices, color = "pink", label="original dataset values")
  plt.pause(0.001)
  fig.canvas.mpl_connect('close_event', on_close)
  plt.waitforbuttonpress()

  return fig


def show_model(x, y, prediction):
  plt.scatter(x, y, marker='x')
  plt.plot(x, prediction, c = 'r')
  plt.title('Linear Regression')
  plt.xlabel('kilometers vehicle')
  plt.ylabel('price in eur')
  plt.show()


def print_fct(x, y, a, b, fig, hist, X):
  skip = My_event()
  line = None
  print("Loading...")

  colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
  i = 0
  for theta in hist:
    remove_plot(line)
    if skip.skip:
      break
    prediction = model(X, theta)
    line = plt.plot(x, prediction, color=colors[i % len(colors)])
    plt.pause(0.01)
    fig.canvas.mpl_connect('close_event', on_close)
    fig.canvas.mpl_connect('button_press_event', skip.on_click)
    i = i + 1
  print("Done !")
  plt.clf()
  plt.title("Linear Regression over dataset")
  plt.xlabel("Normalized Mileage")
  plt.ylabel("Normalized Prices")
  kms = list(x)
  prices = list(y)
  y = a * x + b 
  plt.plot(x, y, "-g")
  plt.scatter(kms, prices, color = "red", label="Normalized dataset values")
  plt.legend()
  plt.grid(True)
  plt.pause(0.001)
  fig.canvas.mpl_connect('close_event', on_close)
  plt.waitforbuttonpress()
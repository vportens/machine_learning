import matplotlib.pyplot as plt

def show_data(x, y):
  plt.scatter(x, y, marker='x')
  plt.title('Dataset')
  plt.xlabel('kilometers vehicle')
  plt.ylabel('price in eur')
  plt.show()

def show_model(x, y, prediction):
  plt.scatter(x, y, marker='x')
  plt.plot(x, prediction, c = 'r')
  plt.title('Linear Regression')
  plt.xlabel('kilometers vehicle')
  plt.ylabel('price in eur')
  plt.show()


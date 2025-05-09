import numpy as np
import matplotlib.pyplot as plt
#generate dataset

def generate_dataset(num_examples):
  np.random.seed(42)
  X = np.random.rand(num_examples,2)*2-1
  y = (X[:,0]+X[:,1]>0).astype(int)
  return X,y
  #train perceptron
def perceptron_train(X,y,learning_rate,epochs):
  num_examples,num_features = X.shape
  weights = np.random.rand(num_features)
  bias = np.random.rand()
  for epoch in range(epochs):
    for i in range(num_examples):
      prediction = np.dot(X[i],weights)+bias
      error = y[i] -(prediction>0)
      if error!=0:
        weights +=learning_rate*error*X[i]
        bias+=learning_rate*error
    return weights,bias

#predict function
def perceptron_predict(X,weights,bias):
  return(np.dot(X,weights)+bias)>=0

  #plot decision boundary
def plot_decision_boundary(X,y,weights,bias,title):
  plt.figure(figsize=(8,4))
  x_min,x_max = X[:,0].min()-0.1,X[:,0].max()+0.1
  y_min,y_max = X[:,1].min()-0.1,X[:,1].max()+0.1
  xx,yy =np.meshgrid(np.linspace(x_min,x_max,100),np.linspace(y_min,y_max,100))
  Z = perceptron_predict(np.c_[xx.ravel(),yy.ravel()],weights,bias)
  Z = Z.reshape(xx.shape)
  plt.contourf(xx,yy,Z,alpha=0.8,cmap=plt.cm.Paired)
  plt.scatter(X[:,0],X[:,1],c=y,edgecolors = 'k',cmap=plt.cm.Paired)
  plt.title(title)
  plt.xlabel('Feature1')
  plt.ylabel('Feature2')
  plt.show()

size = 30
lr =0.3
epoch = 5

#generating dataset
X,y = generate_dataset(size)
weights,bias= perceptron_train(X,y,lr,epoch)
title = f'Dataset Size:{size},Learning Rate:{lr},Epochs:{epoch}'
plot_decision_boundary(X,y,weights,bias,title)

#printing predictions
predictions = perceptron_predict(X,weights,bias)
input_predictions = [(X[i],int(predictions[i])) for i in range(size)]
input_predictions

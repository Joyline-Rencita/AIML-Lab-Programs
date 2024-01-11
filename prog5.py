## prog : 5   ANN
import numpy as np

x = np.array(([2,6],[1,5],[3,6]),dtype=float)
y = np.array(([92],[86],[89]),dtype=float)

x = x/np.amax(x, axis=0)
y = y/100

def sigmoid(x):
  return 1/(1+np.exp(-x))

def derivatives_sigmoid(x):
  return x*(1-x)

epoch = 5000
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
outputlayer_neurons = 1

wh = np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh = np.random.uniform(size=(1,hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons,outputlayer_neurons))
bout = np.random.uniform(size=(1,outputlayer_neurons))

for i in range(epoch):
  hinp1 = np.dot(x,wh)
  hinp = hinp1 + bh
  hlayer_act = sigmoid(hinp)
  outinp1 = np.dot(hlayer_act,wout)
  outinp = outinp1 + bout
  output = sigmoid(outinp)

  EO = y - output
  outgrad = derivatives_sigmoid(output)
  d_output = EO * outgrad

  EH = d_output.dot(wout.T)
  hiddengrad = derivatives_sigmoid(hlayer_act)
  d_hidden = EH * hiddengrad

  wh+= x.T.dot(d_hidden)*lr
  wout+=hlayer_act.T.dot(d_output)*lr


print('Input : '+str(x))
print('Actual Output : '+str(y))
print('Predicted output : ',output)

output:

Input : [[0.66666667 1.        ]
 [0.33333333 0.83333333]
 [1.         1.        ]]
Actual Output : [[0.92]
 [0.86]
 [0.89]]
Predicted output :  [[0.89092599]
 [0.88353052]
 [0.8955073 ]]

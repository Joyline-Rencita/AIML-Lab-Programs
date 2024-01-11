## prog 6  Naive Bayes

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# load the data
data = pd.read_csv('/content/drive/MyDrive/contents/tennis - tennis.csv')
print('The entire dataset is : \n',data.head())

# print 5 cols
X = data.iloc[:,:-1]
print('\nThe train data is : \n',X.head())
y = data.iloc[:,-1]
print('\nThe train output is : \n',y.head())

## now replace with nums using label encoder
le_Outlook = LabelEncoder()
X.Outlook = le_Outlook.fit_transform(X.Outlook)

le_Temperature = LabelEncoder()
X.Temperature = le_Temperature.fit_transform(X.Temperature)

le_Humidity = LabelEncoder()
X.Humidity = le_Humidity.fit_transform(X.Humidity)

le_Wind = LabelEncoder()
X.Wind = le_Wind.fit_transform(X. Wind)

print('The trained dataset is: \n',X.head())

le_PlayTennis = LabelEncoder()
y = le_PlayTennis.fit_transform(y)
print("\nNow the Train output is\n",y)

print('The trained data is: \n',y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,  y_test = train_test_split(X,y,test_size = 0.2)

# Print shapes
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print('\n\n')

classifier = GaussianNB()
classifier.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
print('Accuracy is: \n', accuracy_score(classifier.predict(X_test),y_test))
print('\n\n')


output:

The entire dataset is : 
     Outlook Temperature Humidity    Wind PlayTennis
0     Sunny         Hot     High    Weak         No
1     Sunny         Hot     High  Strong         No
2  Overcast         Hot     High    Weak        Yes
3      Rain        Mild     High    Weak        Yes
4      Rain        Cool   Normal    Weak        Yes

The train data is : 
     Outlook Temperature Humidity    Wind
0     Sunny         Hot     High    Weak
1     Sunny         Hot     High  Strong
2  Overcast         Hot     High    Weak
3      Rain        Mild     High    Weak
4      Rain        Cool   Normal    Weak

The train output is : 
 0     No
1     No
2    Yes
3    Yes
4    Yes
Name: PlayTennis, dtype: object
The trained dataset is: 
    Outlook  Temperature  Humidity  Wind
0        2            1         0     1
1        2            1         0     0
2        0            1         0     1
3        1            2         0     1
4        1            0         1     1

Now the Train output is
 [0 0 1 1 1 0 1 0 1 1 1 1 1 0]
The trained data is: 
 [0 0 1 1 1 0 1 0 1 1 1 1 1 0]
X_train shape: (11, 4)
y_train shape: (11,)


Accuracy is: 
 0.6666666666666666

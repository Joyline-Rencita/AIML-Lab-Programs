## prog 4 ID3

import pandas as pd
df_tennis = pd.read_csv('/content/drive/MyDrive/contents/prog4.csv')
print("\n Giveen Play Tennis Data set:\n\n",df_tennis)

def entropy(probs):
    import math
    return sum([-prob*math.log(prob,2) for prob in probs])

def entropy_of_list(a_list):
    from collections import Counter
    cnt = Counter(x for x in a_list)
    num_instances = len(a_list)*1.0
    probs = [x / num_instances for x in cnt.values()]
    return entropy(probs)

def information_gain(df, split_attribute_name, target_attribute_name, trace=0):
   df_split = df.groupby(split_attribute_name)
   nobs = len(df.index) * 1.0
   df_agg_ent = df_split.agg({target_attribute_name:[entropy_of_list, lambda x:
   len(x)/nobs] })[target_attribute_name]
   df_agg_ent.columns = ['Entropy', 'PropObservations']
   new_entropy = sum( df_agg_ent['Entropy'] * df_agg_ent['PropObservations'] )
   old_entropy = entropy_of_list(df[target_attribute_name])
   return old_entropy - new_entropy

def id3(df, target_attribute_name, attribute_names, default_class=None):
    from collections import Counter
    cnt = Counter(x for x in df[target_attribute_name])
    print(cnt)
    if len(cnt) == 1:
        print(len(cnt))
        return next(iter(cnt))
    elif df.empty or (not attribute_names):
        return default_class
    else:
        default_class=max(cnt.keys())
        gainz = [information_gain(df, attr, target_attribute_name) for attr in attribute_names]
        print("Gain=",gainz)
        index_of_max=gainz.index(max(gainz))
        best_attr = attribute_names[index_of_max]
        print("Best Attribute:",best_attr)
        tree = {best_attr:{}}
        remaining_attribute_names = [i for i in attribute_names if i != best_attr]

        for attr_val, data_subset in df.groupby(best_attr):
            subtree = id3(data_subset,
                        target_attribute_name,
                        remaining_attribute_names,
                        default_class)
            tree[best_attr][attr_val] = subtree
        return tree

attribute_names = list(df_tennis.columns)
print("\n\nList of Attributes:", attribute_names)
attribute_names.remove('PlayTennis')
print("\nPredicting Attributes: \n", attribute_names)

from pprint import pprint
tree = id3(df_tennis,'PlayTennis',attribute_names)
print("\n\nThe resultant Decision Tree is : \n")
pprint(tree)

Output:

 Giveen Play Tennis Data set:

    PlayTennis   Outlook Temperature Humidity    Wind
0          No     Sunny         Hot     High    Weak
1          No     Sunny         Hot     High  Strong
2         Yes  Overcast         Hot     High    Weak
3         Yes      Rain        Mild     High    Weak
4         Yes      Rain        Cool   Normal    Weak
5          No      Rain        Cool   Normal  Strong
6         Yes  Overcast        Cool   Normal  Strong
7          No     Sunny        Mild     High    Weak
8         Yes     Sunny        Cool   Normal    Weak
9         Yes      Rain        Mild   Normal    Weak
10        Yes     Sunny        Mild   Normal  Strong
11        Yes  Overcast        Mild     High  Strong
12        Yes  Overcast         Hot   Normal    Weak
13         No      Rain        Mild     High  Strong


List of Attributes: ['PlayTennis', 'Outlook', 'Temperature', 'Humidity', 'Wind']

Predicting Attributes: 
 ['Outlook', 'Temperature', 'Humidity', 'Wind']
Counter({'Yes': 9, 'No': 5})
Gain= [0.2467498197744391, 0.029222565658954647, 0.15183550136234136, 0.04812703040826927]
Best Attribute: Outlook
Counter({'Yes': 4})
1
Counter({'Yes': 3, 'No': 2})
Gain= [0.01997309402197489, 0.01997309402197489, 0.9709505944546686]
Best Attribute: Wind
Counter({'No': 2})
1
Counter({'Yes': 3})
1
Counter({'No': 3, 'Yes': 2})
Gain= [0.5709505944546686, 0.9709505944546686, 0.01997309402197489]
Best Attribute: Humidity
Counter({'No': 3})
1
Counter({'Yes': 2})
1


The resultant Decision Tree is : 

{'Outlook': {'Overcast': 'Yes',
             'Rain': {'Wind': {'Strong': 'No', 'Weak': 'Yes'}},
             'Sunny': {'Humidity': {'High': 'No', 'Normal': 'Yes'}}}}

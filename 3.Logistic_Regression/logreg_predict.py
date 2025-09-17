import sys
import pandas as pd
import math
import json
from utils import check_train,enter_values
with open("scaling.json", "r") as f:
    scaling = json.load(f)
means = scaling["means"]
stds = scaling["stds"]


Subjects = ["Herbology", "Defense Against the Dark Arts", "Divination", "Potions", "Charms", "Flying"]
df = pd.read_csv(sys.argv[1])
df = df.ffill()
X = []
house = []
for i in range(len(df)):
    student_scores = []
    s = 0
    for subject in Subjects:
        score = df[subject][i]
        student_scores.append((score - means[s]) / stds[s])
        s += 1
    X.append(student_scores)
house = check_train(X)
with open("houses.csv", 'w') as f:
    f.write('Index' + ',' + 'Hogwarts House' + '\n')
    pass
enter_values(house)

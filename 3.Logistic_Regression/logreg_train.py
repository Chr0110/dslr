import sys
import pandas as pd
import random
import json
from utils2 import train_house_G,train_house_H,train_house_R,train_house_S,check_train, calculate_accuracy

df = pd.read_csv(sys.argv[1])
df = df.dropna(subset=['Charms', 'Flying', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Potions'])
df = df.reset_index(drop=True)


Subjects = ["Herbology", "Defense Against the Dark Arts", "Divination", "Potions", "Charms", "Flying"]
X = []
y = []
first_X = []
first_y = []
all_thetas = []

with open("weights.txt", 'w') as f:
    pass
means = []
stds = []

for subject in Subjects:
    subject_scores = []
    for i in range(len(df)):
        score = df[subject][i]
        subject_scores.append(score)
    mean = sum(subject_scores) / len(subject_scores)
    variance = sum((x - mean) ** 2 for x in subject_scores) / len(subject_scores)
    std = variance ** 0.5
    
    means.append(mean)
    stds.append(std)
import json

with open("scaling.json", "w") as f:
    json.dump({"means": means, "stds": stds}, f)
for j in random.sample(range(len(df)), int(len(df) * 70 / 100)):
    student_scores = []
    s = 0
    for subject in Subjects:
        score = df[subject][j]
        student_scores.append((score - means[s]) / stds[s])
        s += 1
    first_X.append(student_scores)
    house_name = df['Hogwarts House'][j]
    if house_name == "Gryffindor":
        house_num = 0
    elif house_name == "Hufflepuff":
        house_num = 1
    elif house_name == "Ravenclaw":
        house_num = 2
    else:
        house_num = 3
    first_y.append(house_num)

train_house_G(first_X, first_y, 0.01 , 500)
train_house_H(first_X, first_y, 0.01 , 500)
train_house_R(first_X, first_y, 0.01 , 500)
train_house_S(first_X, first_y, 0.01 , 500)
house = check_train(first_X, first_y)
accuracy = calculate_accuracy(house, first_y)
print(f"Accuracy: {accuracy:.4f} or {accuracy*100:.2f}%")
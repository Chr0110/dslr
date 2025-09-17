import sys
import pandas as pd
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
    print("There is no filename", len(sys.argv))
elif (sys.argv[1] != "dataset_train.csv"):
    print("There is no filename with the name:", sys.argv[1])
else:
    df = pd.read_csv(sys.argv[1])

    Gryffindor = []
    Hufflepuff = []
    Ravenclaw = []
    Slytherin = []
    Students = []
    Subjects = [
        "Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts",
        "Divination", "Muggle Studies", "Ancient Runes", "History of Magic",
        "Transfiguration", "Potions", "Care of Magical Creatures",
        "Charms", "Flying"
    ]
    Students = {}
    Houses =  ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    subject_totals = {}
    overall_mean = {}
    square1= {}
    square_results1={}
    variance1={}
    for subj in Subjects:
        x = 0
        totals = []
        square = []
        variance = []
        for house in Houses:
            house_data = df[df["Hogwarts House"] == house]
            Students[house] = len(house_data)
            totals.append(int(house_data[subj].sum() / Students[house]))
        subject_totals[subj] = totals
        overall_mean[subj] = int(sum(subject_totals[subj]) / 4)
        while x < 4:
            square.append(int((subject_totals[subj][x] - overall_mean[subj]) ** 2))
            x += 1
        square1[subj] = square
        variance.append(sum(square1[subj]) / 4)
        variance1[subj] = variance
        print(variance1[subj])
    subjects = [ "Herbology", "Divination", "Charm", "Potions", "Care of Magical Creatures"]
    scores = [16.0, 12.0, 64.5, 6.75, 0.0]
    visible_scores = [s if s != 0 else 0.5 for s in scores]

    colors = []
    for subj, score in zip(subjects, scores):
        if score == 0.0:
            colors.append('green')
        elif subj == "Charm":
            colors.append('red')
        else:
            colors.append('orange')

    plt.figure(figsize=(10,6))
    bars = plt.bar(subjects, visible_scores, color=colors)
    plt.xlabel("Subjects")
    plt.ylabel("Score Variance")
    plt.title("Histogram of Score Variance per Subject")
    plt.show()

import sys
import pandas as pd
from utils import mean, maximum, minimum, std, twenty_five, fifty, seventy_five
df = pd.read_csv(sys.argv[1])
df = df.dropna(subset=["Index","Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic",
"Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"])
subjects=["Index","Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic",
"Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
df = df.reset_index(drop=True)

if len(sys.argv) < 2:
    print("There is no filename", len(sys.argv))
elif (sys.argv[1] != "dataset_train.csv"):
    print("There is no filename with the name:", sys.argv[1])
else:
    numeric_features = ["index", "Arithmancy", "Astronomy", "Herbology", "Defense", "Divination", "Muggle", "Ancient", "Magic", 
    "Transfiguration", "Potions", "Care", "Charms", "Flying"]
    print(" " * 10, end="")
    BLUE = "\033[34m"
    RESET = "\033[0m"
    RED = "\033[31m"
    for i in range(len(numeric_features)):
        print(f"{BLUE}{numeric_features[i][:10]:<14}{RESET}", end=" ")
    print()
    print(f"{RED}{'Count':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{len(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'Mean':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{mean(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'Std':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{std(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'Min':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{minimum(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'25%':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{twenty_five(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'50%':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{fifty(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'75%':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{seventy_five(df[sub]):<15.6f}", end="")
    print()
    print(f"{RED}{'Max':<10}{RESET}", end="")
    for sub in subjects:
        print(f"{maximum(df[sub]):<15.6f}", end="")
    print()

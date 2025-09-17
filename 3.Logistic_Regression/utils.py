import math

def safe_sigmoid(z):
    return 1 / (1 + math.exp(-z))
def the_house(house):
    max_index = 0
    max_value = house[0]
    
    for i in range(1, 4):
        if house[i] > max_value:
            max_value = house[i]
            max_index = i
    
    return max_index
def load_weights(filename):
    all_thetas = []
    with open(filename, 'r') as f:
        for line in f:
            theta = [float(x) for x in line.strip().split(',')]
            all_thetas.append(theta)
    return all_thetas
def check_train(X):
    all_thetas = load_weights("weights.txt")
    predictions = []
    house = []
    m = len(X)
    for s in range(m):
        student = []
        for h in range(4):
            z = all_thetas[h][0]
            for j in range (6):
                z += all_thetas[h][j + 1]*X[s][j]
            student.append(safe_sigmoid(z))
        predictions.append(student)
    for p in range(len(predictions)):
        max = the_house(predictions[p])
        house.append(max)
    return house 
def enter_values(house):
    i = 0
    Hagward = ""
    with open("houses.csv", 'a') as f:
        for i in range(len(house)):
            if house[i] == 0:
                Hagward = "Gryffindor"
            elif house[i] == 1:
                Hagward = "Hufflepuff"
            elif house[i] == 2:
                Hagward = "Ravenclaw"
            else:
                Hagward = "Slytherin"
            f.write(str(i) + ',' + Hagward + '\n')
import math
def calculate_cost(predictions, y_binary, m):
    cost = 0
    for i in range(m):
        p = max(min(predictions[i], 0.999999), 0.000001)
        
        if y_binary[i] == 1:
            cost += -math.log(p)
        else:
            cost += -math.log(1 - p)
    return cost / m


def safe_sigmoid(z):
    return 1 / (1 + math.exp(-z))
def load_weights(filename):
    all_thetas = []
    with open(filename, 'r') as f:
        for line in f:
            theta = [float(x) for x in line.strip().split(',')]
            all_thetas.append(theta)
    return all_thetas

def the_house(house):
    max_index = 0
    max_value = house[0]
    
    for i in range(1, 4):
        if house[i] > max_value:
            max_value = house[i]
            max_index = i
    
    return max_index

def calculate_accuracy(predicted, actual):
    correct = 0
    total = len(predicted)
    
    for i in range(total):
        if predicted[i] == actual[i]:
            correct += 1
    
    accuracy = correct / total
    return accuracy

def check_train(X, Y):
    all_thetas = load_weights("./weights.txt")
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

def save_theta(theta, filename):
    with open(filename, 'a') as f:
        f.write(','.join([str(x) for x in theta]) + '\n')


def train_house_G(X, y, learning_rate, max_iterations):
    theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    m = len(X)
    # cost = 0
    for iteration in range(max_iterations):
        predictions = []
        for i in range(m):
            z = theta[0]
            for j in range (6):
                z += theta[j + 1]*X[i][j]
            h = safe_sigmoid(z)
            predictions.append(h)
        # if iteration % 100 == 0:
            # y_binary = [1 if y[i] == 0 else 0 for i in range(m)]
            # cost = calculate_cost(predictions, y_binary, m)
            # print(f"Gryffindor - Iteration {iteration}, Cost: {cost:.4f}")
        l = 0
        for j in range(7):
            gradiant = 0
            for i in range(m):
                if j == 0:
                    if y[i] == 0:
                        gradiant += (predictions[i] - 1) * 1
                    else:
                        gradiant += (predictions[i] - 0) * 1
                else:
                    if y[i] == 0:
                        gradiant += (predictions[i] - 1) *X[i][j - 1]
                    else:
                        gradiant += (predictions[i] - 0) *X[i][j - 1]
            theta[j] -= learning_rate * gradiant / m
    save_theta(theta, "weights.txt")
    return theta


def train_house_H(X, y, learning_rate, max_iterations):
    theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    m = len(X)
    for iteration in range(max_iterations):
        predictions = []
        for i in range(m):
            z = theta[0]
            for j in range (6):
                z += theta[j + 1]*X[i][j]
            h = safe_sigmoid(z)
            predictions.append(h)
        for j in range(7):
            gradiant = 0
            for i in range(m):
                if j == 0:
                    if y[i] == 1:
                        gradiant += (predictions[i] - 1) * 1
                    else:
                        gradiant += (predictions[i] - 0) * 1
                else:
                    if y[i] == 1:
                        gradiant += (predictions[i] - 1) *X[i][j - 1]
                    else:
                        gradiant += (predictions[i] - 0) *X[i][j - 1]
            theta[j] -= learning_rate * gradiant / m
    save_theta(theta, "weights.txt")
    return theta


def train_house_R(X, y, learning_rate, max_iterations):
    theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    m = len(X)
    for iteration in range(max_iterations):
        predictions = []
        for i in range(m):
            z = theta[0]
            for j in range (6):
                z += theta[j + 1]*X[i][j]
            h = safe_sigmoid(z)
            predictions.append(h)
        for j in range(7):
            gradiant = 0
            for i in range(m):
                if j == 0:
                    if y[i] == 2:
                        gradiant += (predictions[i] - 1) * 1
                    else:
                        gradiant += (predictions[i] - 0) * 1
                else:
                    if y[i] == 2:
                        gradiant += (predictions[i] - 1) *X[i][j - 1]
                    else:
                        gradiant += (predictions[i] - 0) *X[i][j - 1]
            theta[j] -= learning_rate * gradiant / m
    save_theta(theta, "weights.txt")
    return theta


def train_house_S(X, y, learning_rate, max_iterations):
    theta = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    m = len(X)
    for iteration in range(max_iterations):
        predictions = []
        for i in range(m):
            z = theta[0]
            for j in range (6):
                z += theta[j + 1]*X[i][j]
            h = safe_sigmoid(z)
            predictions.append(h)
        for j in range(7):
            gradiant = 0
            for i in range(m):
                if j == 0:
                    if y[i] == 3:
                        gradiant += (predictions[i] - 1) * 1
                    else:
                        gradiant += (predictions[i] - 0) * 1
                else:
                    if y[i] == 3:
                        gradiant += (predictions[i] - 1) *X[i][j - 1]
                    else:
                        gradiant += (predictions[i] - 0) *X[i][j - 1]
            theta[j] -= learning_rate * gradiant / m
    save_theta(theta, "weights.txt")
    return theta
<<<<<<< HEAD
weights = [-0.2, 0.4]
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 1, 1, 1]
lr = -0.2
=======
weights = [0.3, -0.2]
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 1, 1, 1]
lr = -0.02
epochs = 15

def sigmoid(x):
    return 1 / (1 + pow(2.71828, -x))
>>>>>>> b1a90484f68f9ec8a996957867e8018e519443c5

def calculate_loss():
    correct = 0
    for i in range(len(inputs)):
        pred = 0
        for j in range(len(weights)):
            pred += weights[j] * inputs[i][j]
<<<<<<< HEAD
        if ((pred > 0 and outputs[i] == 1) or pred == outputs[i]):
            correct += 1
            print("Correct prediction", pred, outputs[i], weights)
            continue
=======
        pred = sigmoid(pred)
        pred = 1 if pred > 0.5 else 0
        if ((pred > 0 and outputs[i] == 1) or pred == outputs[i]):
            correct += 1
>>>>>>> b1a90484f68f9ec8a996957867e8018e519443c5
        else:
            loss = (pred - outputs[i])
            for i in range(len(weights)):
                weights[i] = weights[i] + (lr * loss * inputs[i][j])
    return correct

<<<<<<< HEAD
calculate_loss()
=======
for i in range(epochs):
    correct = calculate_loss()
    print("Epoch: ", i, "Correct: ", correct)
>>>>>>> b1a90484f68f9ec8a996957867e8018e519443c5

pred = []
for i in range(len(inputs)):
    tmp = 0
    for j in range(len(weights)):
        tmp += weights[j] * inputs[i][j]
<<<<<<< HEAD
=======
    tmp = sigmoid(tmp)
    tmp = 1 if tmp > 0.5 else 0
>>>>>>> b1a90484f68f9ec8a996957867e8018e519443c5
    pred.append(tmp)
        
for i in range(len(outputs)):
    print("Input: ", inputs[i], "Output: ", outputs[i], "Predicted: ", pred[i])
            
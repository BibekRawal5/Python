weights = [-0.2, 0.4]
inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 1, 1, 1]
lr = -0.2

def calculate_loss():
    correct = 0
    for i in range(len(inputs)):
        pred = 0
        for j in range(len(weights)):
            pred += weights[j] * inputs[i][j]
        if ((pred > 0 and outputs[i] == 1) or pred == outputs[i]):
            correct += 1
            print("Correct prediction", pred, outputs[i], weights)
            continue
        else:
            loss = (pred - outputs[i])
            for i in range(len(weights)):
                weights[i] = weights[i] + (lr * loss * inputs[i][j])
    return correct

calculate_loss()

pred = []
for i in range(len(inputs)):
    tmp = 0
    for j in range(len(weights)):
        tmp += weights[j] * inputs[i][j]
    pred.append(tmp)
        
for i in range(len(outputs)):
    print("Input: ", inputs[i], "Output: ", outputs[i], "Predicted: ", pred[i])
            
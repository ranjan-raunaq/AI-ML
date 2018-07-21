import random

# Fix inputBias
biasInput = -1
learningRate = 0.2

# Pass input & output
inputA = [0, 0, 1, 1]
inputB = [0, 1, 0, 1]
output = [0, 0, 0, 1]

# initialize weights
biasWeight = random.random()
weightA = random.random()
weightB = random.random()

# Define Input Funtion
def summation(biasInput, biasWeight, inputA, weightA, inputB, weightB):
    sigma = [0, 0, 0, 0]
    
    for i in range(4):
        sigma[i] = (biasInput * biasWeight) + (inputA[i] * weightA) + (inputB[i] * weightB)
        
        res = GreaterThanOne(sigma[i])
        if (res != output[i]):
            # Calculate error and change weights
            error = output[i] - res
            biasWeight += (learningRate * error * biasInput)
            weightA += (learningRate * error * inputA[i])
            weightB += (learningRate * error * inputB[i])

            sigma[i] = summation(biasInput, biasWeight, inputA, weightA, inputB, weightB)

    return (biasWeight, weightA, weightB)

# Define Activation Function
def GreaterThanOne(sigma):
    if (sigma > 1):
        return 1
    else:
        return 0

thetaWeights = [0, 0, 0]
thetaWeights = summation(biasInput, biasWeight, inputA, weightA, inputB, weightB)
print (thetaWeights)

def perceptron(biasInput, inputA, inputB, thetaWeights):
    for i in range(4):
        print ((biasInput * thetaWeights[0]) + (inputA[i] * thetaWeights[1]) + (inputB[i] * thetaWeights[2]))

perceptron(biasInput, inputA, inputB, thetaWeights)

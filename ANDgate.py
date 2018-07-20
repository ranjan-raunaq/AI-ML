'''
Author: Raunaq  Date: July 19th, 2018
AND GATE Perceptron/Neural N/W

0   0   =>  0
0   1   =>  0
1   0   =>  0
1   1   =>  1

'''
print ("AND GATE PERCEPTRON!!!")

# Fix inputBias as 1 and WeightBias as -1
biasInput = 1
biasWeight = -1

# Pass input & output
inputA = [0, 0, 1, 1]
inputB = [0, 1, 0, 1]
output = [0, 0, 0, 1]

# Initialize weights for inputs
weightA = 1
weightB = 1

# Define Input Function
def SigmaAddition(biasInput, biasWeight, inputA, weightA, inputB, weightB):
    summmation = [0, 0, 0, 0]
    for i in range(4):
        summmation[i] = (biasInput * biasWeight) + (inputA[i] * weightA) + (inputB[i] * weightB)               
    print (summmation)

    for i in range(4):
        if (summmation[i] == 1):
            ActivationFunction(summmation[i])
        else:
            print ("AND returns 0")

# Activation function
def ActivationFunction(netInput):
    print ("AND returns 1 => Input 1 1")

# Call SigmaAddition
SigmaAddition(biasInput, biasWeight, inputA, weightA, inputB, weightB)

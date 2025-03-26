import math

baza = [
    [23, 75, 176],
    [25, 67, 180],
    [28, 120, 175],
    [22, 65, 165],
    [46, 70, 187],
    [50, 68, 180],
    [48, 97, 178]
]

def sigmoid(x):
    fact = 1/(1 + (math.exp(-x)))
    return fact

def forwardPass(wiek, waga, wzrost):
    hidden1 = ((wiek * -0.46122) + (waga * 0.97314) + (wzrost * -0.39203) + 0.80109)
    hidden1_po_aktywacji = (sigmoid(hidden1) * -0.81546)
    hidden2 = ((wiek * 0.78548) + (waga * 2.10584) + (wzrost * -0.57847) + 0.43529)
    hidden2_po_aktywacji = (sigmoid(hidden2) * 1.03775)
    output = hidden1_po_aktywacji + hidden2_po_aktywacji - 0.2368
    return output

outputArr = []
for i in baza:
    outputArr.append(forwardPass(i[0], i[1], i[2]))

print(outputArr)
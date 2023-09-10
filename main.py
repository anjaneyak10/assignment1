import numpy as np
import csv
import matplotlib.pyplot as plt

"""
    learningStrings takes a String as an input and then converts it into uppercase
    :param s: String input
    :return: None
    """
def learningStrings(s):
    print("original text-", s)
    print("In uppercase-", s.upper())
    s = "Unsupervised learning does not need a target."
    print("Corrected sentence ",s)
"""
    learningIntegers takes two integers as an input and then increments their value by 1
    :param i: variable 1 
    :param j : variable 2
    return: None
    """
def learningIntegers(i, j):
    print("variable 1 =", i, "Variable 2 = ", j)
    print("After Incrementing the values")
    i += 1
    j += 1
    print("variable 1 =", i, "Variable 2 = ", j)
"""
    learningListsAndDict initializes 2 lists names and age and then prints a few properties
    after doing that it sorts the names and age according to age. We then convert this list into dictionary and then update the ages. 
    :param: None
    :return: None
"""
def learningListsAndDict():
    l1 = ["Saka", "White", "Gabi", "Xhaka", "Ram"]
    l2 = [21, 25, 20, 30, 26]
    print("length of the list = ", len(l1))
    print("type of l1 list", type(l1), " type of l2 list ", type(l2))
    print("max age = ", max(l2))
    print("sum of all ages", sum(l2))
    print("printing alternate elements")
    for i in range(0, len(l1), 2):
        print(l1[i], l2[i])
    info = list(zip(l1, l2))
    info = sorted(info, key=lambda i: i[1])
    print("sorted by ages", info)
    dictionary = dict(info)
    print("dictionary = ", dictionary)
    for i in dictionary.keys():
        dictionary[i] += 1
    print(("dictionary with updated values", dictionary))
"""
    deviationFromAverage calculates the average of a list and then gives the absolute dff between the average and individual 
    elements 
    :param l2: list 
    :return: None
"""
def deviationFromAverage(l2):
    print("Original List", l2)
    avg = sum(l2) // len(l2)
    print("average = ", avg)
    l3 = list()
    for i in range(len(l2)):
        l3.append(abs(avg - l2[i]))
    print("updated list", l3)
"""
    deviationFromAverageUsingComprehension calculates the average of a list and then gives the absolute dff between the average and individual 
    elements 
    :param l2: list 
    :return: None
"""
def deviationFromAverageUsingComprehension(l2):
    print("Original List", l2)
    avg = sum(l2) // len(l2)
    print("average = ", avg)
    l3 = [abs(avg - i) for i in l2]
    print("updated list", l3)
"""
    learningNumpy initializing a numpy array, reshaping it and then performing a few operations
    :param : None
    :return: None
"""
def learningNumpy():
    numpyArray = np.array([])
    # initializing the array with first 50 whole numbers
    for i in range(50):
        numpyArray = np.append(numpyArray, i)
    # Reshaping the array
    numpyArray = numpyArray.reshape(10, 5)
    print("the third column of the numpy array")
    print(numpyArray[:, 2])
    print("square of each elements of the numpy array")
    print(np.square(numpyArray))
    print("multiplying each elements of the numpy array with 3")
    print(numpyArray * 3)
    # creating a new array such that all the elements are greater than 10
    newArray = numpyArray[5:, :]
    print("new array = ", newArray)
    print("sum of new array = ", np.sum(newArray))
    print("stats")
    print("mean over axes 1,2  = ", np.mean(newArray, axis=(0, 1)))
    print("max")
    print(np.max(newArray, axis=(0)), np.max(newArray, axis=(1)), np.max(newArray, axis=(0, 1)))
    print("median")
    print(np.median(newArray, axis=(0)), np.median(newArray, axis=(1)), np.median(newArray, axis=(0, 1)))
"""
    readFile reading the csv file
    :param fileName: String
    :return: list of what is read from Csv file
"""
def readFile(fileName):
    with open(fileName, mode='r') as file:
        csvReader = csv.reader(file)
        csvList = list(csvReader)
        return (csvList)
"""
    csvOperations calling a read function. Divide the 3-D list into 3 lists and then plot a histogram 
    :param : None
    :return: None
"""
def csvOperations():
    babyData = readFile('yob1993.csv')
    babyNames = list()
    babyCount = list()
    babyGender = list()
    for i in babyData:
        babyNames.append(i[0])
        babyGender.append(i[1])
        babyCount.append(i[2])
    plt.bar(babyNames[:10], babyCount[:10])
    plt.show()

if __name__ == '__main__':
    print("q 1.1")
    learningStrings('Unsupervised learning needs a target.')
    print()
    learningIntegers(7, 8)
    print("------------------------------------------------------------------")
    print("q 1.2")
    learningListsAndDict()
    print()
    l2 = [8, 9, 1, 3, 5, 11, 3, 4, 5]
    deviationFromAverage(l2)
    print()
    l2 = [7, 6, 8, 9, 0, 33, 6]
    deviationFromAverageUsingComprehension(l2)
    print("------------------------------------------------------------------")
    print("q 1.3")
    learningNumpy()
    print("------------------------------------------------------------------")
    print("q 1.4")
    csvOperations()

#Defining a list
myFruitList = ["apple", "banana", "cherry",7]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])

#Change values in list 
myFruitList[2] = "Orange"
myFruitList.pop(0)
print(myFruitList)
myFruitList.insert(2,"apple")
print(myFruitList)
print(myFruitList.count("apple"))

#tuple type
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])

#dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])


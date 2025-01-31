#LAB 2(1)

#Python Sets

myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Python - Access Set Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Python - Add Set Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#Python Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  #Python - Join Sets

  set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Python - Access Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

x = thisdict.get("model")

x = thisdict.keys()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  
  x = car.keys()
  
  print(x) #before the change
  
  car["color"] = "white"
  
  print(x) #after the change

  x = thisdict.values()

  car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
  x = car.values()
    
    print(x) #before the change
    
    car["year"] = 2020
    
    print(x) #after the change

    car = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
      }
      
      x = car.values()
      
      print(x) #before the change
      
      car["color"] = "red"
      
      print(x) #after the change

      car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
        }
        
        x = car.values()
        
        print(x) #before the change
        
        car["color"] = "red"
        
        print(x) #after the change

        car = {
          "brand": "Ford",
          "model": "Mustang",
          "year": 1964
          }
          
          x = car.items()
          
          print(x) #before the change
          
          car["year"] = 2020
          
          print(x) #after the change

          car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
            
            x = car.items()
            
            print(x) #before the change
            
            car["color"] = "red"
            
            print(x) #after the change

            thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
            }
            if "model" in thisdict:
              print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Python - Change Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Python - Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Python - Remove Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Python - Loop Dictionaries

for x in thisdict:
  print(x)

  for x in thisdict:
  print(thisdict[x])

  for x in thisdict.values():
  print(x)

  for x in thisdict.keys():
  print(x)

  for x, y in thisdict.items():
  print(x, y)

  #Python - Copy Dictionaries

  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  mydict = thisdict.copy()
  print(mydict)

  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  mydict = dict(thisdict)
  print(mydict)

  #Python - Nested Dictionaries

  myfamily = {
    "child1" : {
      "name" : "Emil",
      "year" : 2004
    },
    "child2" : {
      "name" : "Tobias",
      "year" : 2007
    },
    "child3" : {
      "name" : "Linus",
      "year" : 2011
    }
  }

  child1 = {
    "name" : "Emil",
    "year" : 2004
  }
  child2 = {
    "name" : "Tobias",
    "year" : 2007
  }
  child3 = {
    "name" : "Linus",
    "year" : 2011
  }
  
  myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
  }

  print(myfamily["child2"]["name"])

  for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


#Python If ... Else

a = 33
b = 200
if b > a:
  print("b is greater than a")

  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  if a > b: print("a is greater than b")

  a = 2
b = 330
print("A") if a > b else print("B")

 a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

  a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    a = 33
b = 200

if b > a:
  pass

#Python While Loops

i = 1
while i < 6:
  print(i)
  i += 1

  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  for x in "banana":
  print(x)

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  for x in range(6):
  print(x)

  for x in range(2, 6):
  print(x)

  for x in range(2, 30, 3):
  print(x)

  for x in range(6):
  print(x)
else:
  print("Finally finished!")

  for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    for x in [0, 1, 2]:
  pass


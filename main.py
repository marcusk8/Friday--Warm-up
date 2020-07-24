# Variable - nickname for a value
score = 0
item = "bannas"


#Lists/ arrays - a way to store multipal values

grocery_list = ["apples", "pears", "cherries", "oreos"]
# grocery_list

# add an item
for i in grocery_list:
  print(i, "2.99")
  print("on sale")



grocery_list.append(item)
grocery_list.append("youguart")
print(grocery_list)


#remove an item
grocery_list.pop(0)
grocery_list.pop(4)
grocery_list.remove("oreos")
print(grocery_list)

for i in grocery_list:
  print("Hi")
  for i in range(3):
    print("inside of 3 loop")

# Functions: instruction to do an action
def list_num():
  counter = 0
  for i in grocery_list:
    counter +=1
  print (counter)


list_num()

# Conditional: used for decision making, test if condition is true

if "apples" in grocery_list:
  print("apple red")
elif "cherries" in grocery_list:
  print("cherry red")
else: 
  print("item not in list")
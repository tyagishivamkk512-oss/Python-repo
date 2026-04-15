# List[] is Ordered and changable, duplicates are ok

vegetable = ["aaloo","gobhi","gajar","matar","Tamatar"]

print(vegetable)
print(vegetable[::2])
print(vegetable[:4:2])

#for i in vegetable:
#    print(i)
# to print in same line use print(i,end = " ")


#print(dir(vegetables))  will print all functions that could be apply on out list
#print(help(vegetables)) will print description of all functions

print(len(vegetable)) 
print("gobhi" in vegetable) #will return true or false

vegetable[2] = "mooli"

vegetable.append("bhindi") #will add element at last

vegetable.remove("mooli") 

vegetable.insert(2,"loki") #will add loki at index 2

# vegetable.sort() sort by alphabatical order

#vegetable.reverse()

#vegetable.clear()  to clear list
#vegetable.index()  to find index of an element
#vegetable.count()  to find how many of them are there 

# %%
'''Write a python program to create, append, and remove etc. operation on dictionary and tuple'''
#tuple
tup=(2,4,6,8,4,10)
print("Number of times 4 is present ",tup.count(4))#count function
print("Index of 6: ",tup.index(6))#index function
sor= sorted(tup)#sorted function
print("Sorted tuple ",sor)
print("Length of tuple ",len(tup))#length function
total=sum(tup)#sum fucntion
print("Sum of tuple ",total)
# %%
#dictionary
d={"Name":"Rucha","Roll no.":5,"Branch":"CSE CSF","Marks":95}
print (d)
print("All Keys in Dictionary: ",d.keys())#keys function
print("All Values in Dictionary: ",d.values())#values function
print("All items in Dictionary: ",d.items())#items function
print("Getting the value of a key ",d.get("Branch"))#get function
d.update({"Roll no.":6})#update function
print("Updated Dictionary using update function ", d)
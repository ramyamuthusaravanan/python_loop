#write a python program that takes a list of words and returns the longest one.

a=input("Enter list of words with comma=")
b=a.split(",")
print("list of names")
print(b)
print("numer of items in list=")
print(len(b))
print("first name of the list and length")
print(b[0])
print(len(b[0]))

c=""
for i in range(0,len(b)):
    #print("each words len")
    #print(len(b[i]))
    if i==0:
        c=b[i]
    else:
        if len(b[i])>len(c):
            c=b[i]
print("the longest word")
print(c)
'''Pattern Printing Technique'''
#📘 Common Pattern Types


#1. Square / Rectangle Patterns
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
for i in range(5):
    for j in range(5):
        print("* ", end='')
    print()

#2 Right Triangle
print("___________________________") 
'''
*
* *
* * *
* * * *
* * * * *
'''
#(a)
n=5
for i in range(1, n+1):
    for j in range(i):
        print("* ", end = '')
    print()

#(b)
for i in range(1, n+1):
    print("* " * i)


print("___________________________")
#Inverted Triangle
'''
* * * * *
* * * *
* * *
* *
*
'''
for i in range(n):
    for j in range(n+1,i,-1):
        print("* ", end='')
    print()
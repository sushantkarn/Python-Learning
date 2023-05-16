# Write a python program to enter the marks of six students and print them in shorted manner

m1 = int(input("Enter the mark of the 1 student: "))
m2 = int(input("Enter the mark of the 2 student: "))
m3 = int(input("Enter the mark of the 3 student: "))
m4 = int(input("Enter the mark of the 4 student: "))
m5 = int(input("Enter the mark of the 5 student: "))
m6 = int(input("Enter the mark of the 6 student: "))

mymarklist = [m1, m2, m3, m4, m5, m6]
mymarklist.sort()
print(mymarklist)
mymarklist.reverse()
print(mymarklist)

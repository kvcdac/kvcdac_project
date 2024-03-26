'''
#For Loop
myList=[12,3,490]
for i in range(len(myList)):
    #print ("Indexes ", i)
    #print ("Nos :", myList[i])
    print (i, "", myList[i])
print ("")

#Printing Nos 1 to 7
print ("Printing Odd Nos using For Loop")
for i in range(1,8,2):
   print (i)
print ("")

#While Loop
print ("While Loop Printing 0-2 with Break")
x=0
while(x<9):
    print (x)
    x=x+1
    if(x==3):
        break
print ("")

    
print ("While Loop With Continue")
x=0
while(x<9):
    #print (x)
    x=x+1
    if(x==3):
        continue
    print (x)
print ("")


for i in range(10):
    if(i==3):
        continue
    print (i)
print ("")




x=0
for x in range(1,10):
    print ("Before ", x)
    x=x+1
    if(x==3):
        continue
    #print ("After ", x)
print ("")
    


#nested Loops
for num1 in range(1):
    for num2 in range(2):
        for num3 in range(3):
            print(num1,num2,num3)

#Print Nos in Rows and Columns
n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()


'''
#Q 9
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
x=color_list_1-color_list_2
print(x)
#*************************
#Q 1
sum=0
for x in range(0,20):
    if(x % 2 == 1):
        sum=sum+x
print("Sum of odd number is ",sum)
'''
#Q 8
'''
d1={0: 10, 1: 20}
d2={2:30}
d1.update(d2)
print(d1)
   '''
'''
#Q 7
d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d1.update(d2)
d1.update(d3)
print(d1)
 '''
#Q5
'''
for x in range(48,57+1):
    print(chr(x))
'''
#Q 4
'''
for x in range(65,90+1):
    print(chr(x)) 
   '''
#Q 6
'''
for x in range(97,122+1):
    print(x,chr(x)) 
 '''
#Q 2
'''
sum=0
for x in range(0,200):
    if(x>100 and x<200):
        sum=sum+x
print("Sum of odd number is ",sum)
'''
'''
sum=0
for x in range(0,20+1):
    if(x % 2 == 0):
        sum=sum+x
print("Sum of odd number is ",sum)
'''
for i in range(6):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

 

     



#Python program to generate Fibonacci Series until"n" value using while loop
n = int(input("Enter the value of 'n' :"))
a = 0
b = 1
sum = 1
count = 0
print("Fibonacci Series:",end = " ")
while(count <= n):
    print(sum,end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b



    

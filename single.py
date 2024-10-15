'''
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
'''
set={3,1,5,4,2}
a=int(input("enter number if values"))
for i in range(a):
    n=int(input()) 
print(*set)

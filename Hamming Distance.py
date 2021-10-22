'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
'''
x = int(input())
y = int(input())
print(bin(x ^ y)[2:].count('1'))

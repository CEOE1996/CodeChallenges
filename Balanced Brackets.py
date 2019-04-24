#!/bin/python3

#Hacker Rank Problem
#https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys

brackets = {"{" : "}", "[" : "]", "(" : ")"}

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for i in range(len(s)):
        if s[i] in brackets.keys():
            stack.append(s[i])
        else:
            l = len(stack)
            if l > 0 and s[i] == brackets[stack[l - 1]]:
                stack.pop()
            else:
                return "NO"
    
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + '\n')

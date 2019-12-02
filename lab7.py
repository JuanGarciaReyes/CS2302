# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:10:37 2019

@author: Eng
"""

def edit_distance(string1, string2, len1, len2):
    dp = [[0 for i in range(len2 + 1)] for i in range(len1 + 1)]

    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1])
    
    return dp[len1][len2]

def problem2 (triangle):
        if not triangle:
            return 0

        lastLevel = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                lastLevel[j] = min(lastLevel[j], lastLevel[j + 1]) + triangle[i][j]

        return lastLevel[0]



string1 = "monkey"
string2 = "mykong"
triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
print(edit_distance(string1, string2, len(string1), len(string2)))
print("problem 2")
print (problem2(triangle))

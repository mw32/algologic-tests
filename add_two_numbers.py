#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 23:01:24 2020

@author: martin.widjaja
"""

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryover = 0
        sum = l1.val + l2.val + carryover
        if (sum >= 10):
            sum = sum % 10
            carryover = 1
        
        finalResult = ListNode(sum)
        curResult = finalResult
        
        while (l1.next or l2.next):
            l1val = l2val = 0
            
            if l1.next:
                l1 = l1.next
                l1val = l1.val
                
            if l2.next:
                l2 = l2.next
                l2val = l2.val

            sum = l1val + l2val + carryover
            carryover = 0
            if (sum >= 10):
                sum = sum % 10
                carryover = 1
                
            res = ListNode(sum)
            curResult.next = res
            curResult = res
            
        if (carryover > 0):
            res = ListNode(carryover)
            curResult.next = res
            curResult = res
            
        return finalResult
                

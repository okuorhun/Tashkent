#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:17:24 2022

@author: murat
"""
class MyClass:
	def printList(self, data):
		for i in data:
			print(i)
	
	
	def sumList(self, data):
		k=0
		for i in data:
			k=k+i
		
		return k

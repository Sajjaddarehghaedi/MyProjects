#!/usr/bin/env python
# coding: utf-8

# In[104]:


from math import sin, cos
class Cal:
    def __init__(self,cha,*args):
        
        numbers = []
        for i in args:
            numbers.append(i)
            
        match cha:
            
            case '+':
                def add(numbers):
                    print(sum(numbers))
                add(numbers) 
                
            case '-':
                def mines(numbers):
                    results = 0
                    for i in numbers:
                        results -=i
                    print(results)
                mines(numbers)
                
            case '/':    
                def divide(numbers):
                    if len(numbers) <= 2:
                        results = numbers[0] / numbers[1]
                        print('%d / %d = %d'%(numbers[0],numbers[1],results))
                    else:
                        print('must be two numbers')
                divide(numbers)  
                
            case '*':
                
                
                def multiply(numbers):
                    results = 1
                    for i in args:
                        results *= i
                    print(results)
                multiply(numbers)
                
            case 'abs':    
                def absol(numbers):
                    abso = []
                    for i in numbers:
                            abso.append(abs(i))
                    print(abso)        
                absol(numbers)
                
            case 'sin':
                def sino(numbers):
                    sinos = []
                    for i in numbers:
                        sinos.append(sin(i))
                    print(sinos)    
                sino(numbers)
                
            case 'cos':
                    def cosin(numbers):
                        cosinos = []
                        for i in numbers:
                            cosinos.append(cos(i))
                        print(cosinos)
                    cosin(numbers)    
                     
            case _:
                print('none operation for this\nyou must use this operators( + - * / sin cos abs)')
    @classmethod
    def help(self):
        return print('this a simple calcolator\nyou must use this operators( + - * / sin cos abs)')
                


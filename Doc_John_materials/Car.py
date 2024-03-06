#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        
    def displayCar(self):
        print(self.color + " " + self.model)


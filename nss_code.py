# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:31:36 2020

@author: X541U
"""

import pandas as pd
import numpy as np
import xlwt

file = pd.read_excel('Final.xlsx', sheet_name = 'fubar_passeri40_1_NSS') #reads the file and sheet chosen
slac = (file['SLAC']) #choses the column
fel = (file['FEL'])
fubar = (file['FUBAR'])

lst_a = list(slac) #transforms the values into a list
lst_b = list(fel)
lst_c = list(fubar)


print(lst_a) #prints the list
print(lst_b)
print(lst_c)

#Creates variables that encapsulate the common elements between every two lists
x = ("Common elements between slac and fel:", (set(slac).intersection(fel)))

y = ("Common elements between slac and fubar:", (set(slac).intersection(fubar)))

z = ("Common elements between fubar and fel:", (set(fubar).intersection(fel)))


#Creates a variable that encapsulates the common elements in every list
w = ("Common values to all:", (set(x[1]).intersection(fubar)))


#Tranforms the tuples into lists
x1 = list(x[1])
y1 = list(y[1])
z1 = list(z[1])
w1 = list(w[1])

#Prints the list of lists
list1 = []
list1.append(x1)
list1.append(y1)
list1.append(z1)
list1.append(w1)


#Tranforms the list of lists into a list
flat_list = []
for sublist in list1:
    for item in sublist:
        flat_list.append(item)


arr = np.array(flat_list) #Tranforms the list into an array

uniqueValues = np.unique(arr) #Gets all the unique values from the numpy array


l = list(uniqueValues) #Creates a variable for the list of the unique values
ll = len(uniqueValues) #Creates a variable for the number of unique values

print('Unique values:', l) #Prints the unique values
print('Number of unique values:', ll) #Prints the number of unique values



workbook = xlwt.Workbook() #Creates an instance of xlwt.Workbook

#Adds an worksheet with the same name as the original file's sheet 
sheet = workbook.add_sheet("capri_chara_ardea 40l_NSS")


#Writting on specified sheet 
for i, value in enumerate(l): #Gets the index of the list
        sheet.write(i+1, 0, str(value)) #Writes the obtained unique values insucessive rows starting from the second row and first column
        
sheet.write(0, 0, "sites") #Writes "sites" on the first row and column
sheet.write(0, 1, "number of sites") #Writes "numer of sites" on the first row and second column
sheet.write(1, 1, ll) #Writes the number of unique values in the second row and second column 
  
workbook.save("DataMonkey_NSS.xls") #saves the workbook

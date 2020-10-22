# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:02:20 2020

@author: X541U
"""


import pandas as pd
import numpy as np
import xlwt

file = pd.read_excel('Final.xlsx', sheet_name = 'fubar_passeri40_1_PSS') #reads the file and sheet chosen
slac = (file['SLAC']) #choses the column
fel = (file['FEL'])
fubar = (file['FUBAR'])
meme = (file['MEME'])

lst_a = list(slac) #transforms the values into a list
lst_b = list(fel)
lst_c = list(fubar)
lst_d = list(meme)

print(lst_a) #prints the list
print(lst_b)
print(lst_c)
print(lst_d)

#Creates variables that encapsulate the common elements between every two lists
x = ("Common elements between slac and fel:", (set(slac).intersection(fel)))

y = ("Common elements between slac and fubar:", (set(slac).intersection(fubar)))

z = ("Common elements between fubar and fel:", (set(fubar).intersection(fel)))

#Creates variables that encapsulate the common elements between every three lists
k = ("Common values to slac, fel, fubar:", (set(x[1]).intersection(fubar)))
e = ("Common values to slac, fel, meme:", (set(x[1]).intersection(meme)))
f = ("Common values to slac, fubar, meme:", (set(y[1]).intersection(meme)))
g = ("Common values to fubar, fel, meme:", (set(z[1]).intersection(meme)))

#Creates a variable that encapsulates the common elements in every list
w = ("Common values to all:", (set(k[1]).intersection(meme)))


#Tranforms the sets back into lists
k1 = list(k[1])
e1 = list(e[1])
f1 = list(f[1])
g1 = list(g[1])
w1 = list(w[1])

#Prints list of lists
list1 = []
list1.append(k1)
list1.append(e1)
list1.append(f1)
list1.append(g1)
list1.append(w1)


#Converts the list of lists into a list
flat_list = []
for sublist in list1:
    for item in sublist:
        flat_list.append(item)


arr = np.array(flat_list) #Converts the list into an array

uniqueValues = np.unique(arr) #Gets all the unique values from the numpy array


l = list(uniqueValues) #Creates a variable for the list of the unique values
ll = len(uniqueValues) #Creates a variable for the number of unique values

print('Unique values:', l) #Prints the unique values
print('Number of unique values:', ll) #Prints the number of unique values



workbook = xlwt.Workbook() #Creates an instance of xlwt.Workbook

#Adds an worksheet with the same name as the original file's sheet 
sheet = workbook.add_sheet("capri_chara_ardea 40l_PSS")


#Writting on specified sheet 
for i, value in enumerate(l): #Gets the index of the list
        sheet.write(i+1, 0, str(value)) #writes the obtained unique values insucessive rows starting from the second row and first column
        
sheet.write(0, 0, "sites") #Writes "sites" on the first row and column
sheet.write(0, 1, "number of sites") #Writes "numer of sites" on the first row and second column
sheet.write(1, 1, ll) #Writes the number of unique values in the second row and second column 
  
workbook.save("DataMonkey_PSS.xls") #saves the workbook

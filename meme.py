# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:52:34 2020

@author: X541U
"""

import pandas as pd
import numpy as np


'''Reads files and chose values from Excel'''

file = 'meme_passeri40_1.xls' #Reads the first file
with pd.ExcelFile(file) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name='meme_passeri40_1') #Reads the sheet chosen
        #print(df.head())

#When the values from column p-value are under 0.05, get the value from column 'Site' in the same row             
pss_1 = df.loc[df['p-value'] < 0.05, 'Site']     
#print(pss)

pss_list_1 = list(pss_1) #Converts int64 into list
print('1st Sites:', pss_list_1) #Prints the PSS sites in the first file
print('1st Number of PSS sites:', len(pss_list_1)) #Prints the number of PSS sites in the first file



file = 'meme_passeri40_1.xls' #Reads the second file
with pd.ExcelFile(file) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name='meme_passeri40_1') #Reads the sheet chosen
        #print(df.head())

#When the values from column p-value are under 0.05, get the value from column 'Site' in the same row                     
pss_2 = df.loc[df['p-value'] < 0.05, 'Site']     
#print(pss)

pss_list_2 = list(pss_2) #Converts int64 into list
print('2nd Sites:', pss_list_2) #Prints the PSS sites in the second file
print('2nd Number of PSS sites:', len(pss_list_2)) #Prints the number of PSS sites in the second file



file = 'meme_passeri40_1.xls' #Reads the third file
with pd.ExcelFile(file) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name='meme_passeri40_1')  #Reads the sheet chosen
        #print(df.head())

#When the values from column p-value are under 0.05, get the value from column 'Site' in the same row             
pss_3 = df.loc[df['p-value'] < 0.05, 'Site']     
#print(pss)

pss_list_3 = list(pss_3)  #Converts int64 into list
print('3rd Sites:', pss_list_3) #Prints the PSS sites in the third file
print('3rd Number of PSS sites:', len(pss_list_3)) #Prints the number of PSS sites in the third file



'''Compares the lists and get a final list for PSS'''

#Creates variables that encapsulate the common elements between the lists of the three files
x = ("Common elements between pss_list_1 and pss_list_2:", (set(pss_list_1).intersection(pss_list_2)))
#print(x)
#print("Number of common elements between slac and fel:", len(x[1]))

y = ("Common elements between pss_list_1 and pss_list_3:", (set(pss_list_1).intersection(pss_list_3)))
#print(y)
#print("Number of common elements between slac and fubar:", len(y[1]))

z = ("Common elements between pss_list_2 and pss_list_3:", (set(pss_list_2).intersection(pss_list_3)))
#print(z)
#print("Number of common elements between fubar and fel:", len(z[1]))

#Creates a variable that encapsulates the common elements in every list
w = ("Common values to all:", (set(x[1]).intersection(pss_list_3)))
#print("Common values to all:", (w))
#print(len(w[1]))

#Tranforms the sets back into lists
x1 = list(x[1])
y1 = list(y[1])
z1 = list(z[1])
w1 = list(w[1])

#Prints list of lists
list1 = []
list1.append(x1)
list1.append(y1)
list1.append(z1)
list1.append(w1)
#print("List of lists:", list1)

#Tranforms the list of lists into a list
flat_list = []
for sublist in list1:
    for item in sublist:
        flat_list.append(item)
#print("Lista:", flat_list)

arr = np.array(flat_list) #Converts the list into an array

uniqueValues = np.unique(arr) #Get unique values from a numpy array
 
final = ', '.join(map(str, uniqueValues)) #Separate the valus with commas
        
print('Sites: ', final) #Prints the unique values

print('Number of sites:', len(uniqueValues)) #Prints the number of unique values

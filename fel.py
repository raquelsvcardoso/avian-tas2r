# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:06:29 2020

@author: X541U
"""

import pandas as pd
import numpy as np


'''Reads files and chose values from Excel'''

file = 'fel_passeri40_1.xls' #Reads the first file
with pd.ExcelFile(file) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name='fel_passeri40_1') #Reads the sheet chosen
        #print(df.head())
        
#When the values from column p-value are under or equal to 0.05, get the value from column 'Site' in the same row         
pss_1 = df.loc[df['p-value'] < 0.05, 'Site']    

#When the strings from column omega are equal to 'Infinity', get the value from column 'Site' in the same row   
pss_11 = (df.loc[df['omega'].str.contains('Infinity', na=False),'Site'])
#print(list(pss_11))


df.omega = pd.to_numeric(df.omega, errors='coerce') #Considers all cells from column "omega" as numeric
    
#When the strings from column omega are above 1, get the value from column 'Site' in the same row   
pss_2 = df.loc[df['omega'] > 1, 'Site']


x1 = (set(pss_1).intersection(pss_2)) #Get the values that comply to both conditions

x11 = (set(pss_1).intersection(pss_11)) #Get the values that comply to both conditions
#print(x11)

x1.update(x11)#Adds values from set x1 to set x11

print('1st Sites:', sorted(list(x1))) #Prints the sorted list

print('1st Number of PSS sites:', len(x1)) #Prints the number of PSS


#When the values from column p-value are under or equal to 0.05, get the value from column 'Site' in the same row
nss_1 = df.loc[df['p-value'] < 0.05, 'Site']

#When the strings from column omega are under 1, get the value from column 'Site' in the same row   
nss_2 = df.loc[df['omega'] < 1, 'Site']

x2 = (set(nss_1).intersection(nss_2)) #Gets the values that comply to both conditions

print('1st Sites:', sorted(list(x2))) #Prints the sorted list

print('1st Number of NSS sites:', len(x2)) #Prints the number of NSS



file = 'fel_passeri40_1.xls' #Reads the second file
with pd.ExcelFile(file) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name='fel_passeri40_1') #Reads the sheet chosen

#When the values from column p-value are under or equal to 0.05, get the value from column 'Site' in the same row           
pss_3 = df.loc[df['p-value'] < 0.05, 'Site']

#When the strings from column omega are equal to 'Infinity', get the value from column 'Site' in the same row     
pss_33 = (df.loc[df['omega'].str.contains('Infinity', na=False),'Site'])
#print(list(pss_11))

df.omega = pd.to_numeric(df.omega, errors='coerce') #Considers all cells from column "omega" as numeric
    
#When the strings from column omega are above 1, get the value from column 'Site' in the same row   
pss_4 = df.loc[df['omega'] > 1, 'Site']

y1 = (set(pss_3).intersection(pss_4)) #Get the values that comply to both conditions

y11 = (set(pss_3).intersection(pss_33)) #Get the values that comply to both conditions
#print(x11)

y1.update(y11) #Adds values from set x1 to set x11

print('2nd Sites:', sorted(list(y1))) #Prints the sorted list
print('2nd Number of PSS sites:', len(y1)) #Prints the number of PSS

#When the values from column p-value are under or equal to 0.05, get the value from column 'Site' in the same row
nss_3 = df.loc[df['p-value'] < 0.05, 'Site']

#When the strings from column omega are under 1, get the value from column 'Site' in the same row   
nss_4 = df.loc[df['omega'] < 1, 'Site']


y2 = (set(nss_3).intersection(nss_4)) #Gets the values that comply to both conditions

print('2nd Sites:', sorted(list(y2))) #Prints the sorted list
print('2nd Number of NSS sites:', len(y2)) #Prints the number of NSS



file = 'fel_passeri40_1.xls' #Reads the third file
with pd.ExcelFile(file) as xls:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(file, sheet_name='fel_passeri40_1') #Reads the sheet chosen

#When the values from column p-value are under or equal to 0.05, get the value from column 'Site' in the same row           
pss_5 = df.loc[df['p-value'] <= 0.05, 'Site']

#When the strings from column omega are equal to 'Infinity', get the value from column 'Site' in the same row     
pss_55 = (df.loc[df['omega'].str.contains('Infinity', na=False),'Site'])
#print(list(pss_11))

df.omega = pd.to_numeric(df.omega, errors='coerce') #Considers all cells from column "omega" as numeric
    
#When the strings from column omega are above 1, get the value from column 'Site' in the same row   
pss_6 = df.loc[df['omega'] > 1, 'Site']

z1 = (set(pss_5).intersection(pss_6)) #Get the values that comply to both conditions

z11 = (set(pss_5).intersection(pss_55)) #Get the values that comply to both conditions
#print(x11)
z1.update(z11) #Adds values from set z1 to set z11

print('3rd Sites:', sorted(list(z1))) #Prints the sorted list
print('3rd Number of PSS sites:', len(z1)) #Prints the number of PSS

#When the values from column p-value are under or equal to 0.05, get the value from column 'Site' in the same row
nss_5 = df.loc[df['p-value'] < 0.05, 'Site']

#When the strings from column omega are under 1, get the value from column 'Site' in the same row   
nss_6 = df.loc[df['omega'] < 1, 'Site']


z2 = (set(nss_5).intersection(nss_6)) #Gets the values that comply to both conditions
print('3rd Sites:', sorted(list(z2))) #Prints the sorted list
print('3rd Number of NSS sites:', len(z2)) #Prints the number of NSS


x3 = ("Common elements between pss_list_1 and pss_list_2:", (set(x1).intersection(y1)))
#print(x)
#print("Number of common elements between slac and fel:", len(x[1]))

y3 = ("Common elements between pss_list_1 and pss_list_3:", (set(x1).intersection(z1)))
#print(y)
#print("Number of common elements between slac and fubar:", len(y[1]))

z3 = ("Common elements between pss_list_2 and pss_list_3:", (set(y1).intersection(z1)))
#print(z)
#print("Number of common elements between fubar and fel:", len(z[1]))


w = ("Common values to all:", (set(x3[1]).intersection(z1)))
#print("Common values to all:", (w))
#print(len(w[1]))

#Tranforms the sets back into lists
x4 = list(x3[1])
y4 = list(y3[1])
z4 = list(z3[1])
w = list(w[1])

#Prints list of lists
list1 = []
list1.append(x4)
list1.append(y4)
list1.append(z4)
list1.append(w)
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


x5 = ("Common elements between nss_list_1 and nss_list_2:", (set(x2).intersection(y2)))
#print(x)
#print("Number of common elements between slac and fel:", len(x[1]))

y5 = ("Common elements between nss_list_1 and nss_list_3:", (set(x2).intersection(z2)))
#print(y)
#print("Number of common elements between slac and fubar:", len(y[1]))

z5 = ("Common elements between nss_list_2 and nss_list_3:", (set(y2).intersection(z2)))
#print(z)
#print("Number of common elements between fubar and fel:", len(z[1]))


w1 = ("Common values to all:", (set(x5[1]).intersection(z2)))
#print("Common values to all:", (w))
#print(len(w[1]))

#Tranforms the sets back into lists
x6 = list(x5[1])
y6 = list(y5[1])
z6 = list(z5[1])
w2 = list(w1[1])

#Prints list of lists
list2 = []
list2.append(x6)
list2.append(y6)
list2.append(z6)
list2.append(w2)
#print("List of lists:", list1)

#Tranforms the list of lists into a list
flat_list1 = []
for sublist1 in list2:
    for item in sublist1:
        flat_list1.append(item)
#print("Lista:", flat_list)

arr1 = np.array(flat_list1) #Converts the list into an array

uniqueValues1 = np.unique(arr1) #Get unique values from a numpy array
 
final = ', '.join(map(str, uniqueValues1)) #Separate the valus with commas
        
print('Sites: ', final) #Prints the unique values

print('Number of sites:', len(uniqueValues1)) #Prints the number of unique values

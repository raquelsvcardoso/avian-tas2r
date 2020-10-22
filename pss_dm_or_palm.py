# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:51:01 2020

@author: X541U
"""

import pandas as pd
import numpy as np
import xlwt

'''Reads files and chose values from Excel'''

file = pd.read_excel(r'C:\Users\X541U\Documents\Tese\analise_estatistica\analise_estatistica_habitat_9.xlsx', sheet_name = 'Water') #reads the file and sheet chosen



dm = (file['DM_PSS']) #choses the column
palm = (file['PALM_PSS'])

dm_1 = dm[np.logical_not(np.isnan(dm))]

palm_1 = palm[np.logical_not(np.isnan(palm))]

dm_2 = list(dm_1)
print('List of PSS found by DM:', dm_2)

palm_2 = list(palm_1)
print('List of PSS found by PALM:', palm_2)


result = (dm_2 + list(set(palm_2) - set(dm_2)))


result.sort()
print("Total:", list(result))
size = len(result)
print("Total number:", size)


workbook = xlwt.Workbook() #Creates an instance of xlwt.Workbook

#Adds an worksheet with the same name as the original file's sheet 
sheet = workbook.add_sheet("Passeri_6")

#Writting on specified sheet 
for i, value in enumerate(result): #Gets the index of the list
        sheet.write(i+1, 0, str(value)) #writes the obtained unique values insucessive rows starting from the second row and first column
        
sheet.write(0, 0, "sites") #Writes "sites" on the first row and column
sheet.write(0, 1, "number of sites") #Writes "number of sites" on the first row and second column
sheet.write(1, 1, size) #Writes the number of unique values in the second row and second column 
  
workbook.save(r'C:\Users\X541U\Documents\Tese\analise_estatistica\analise_estatistica_habitat_9.xls') #saves the workbook

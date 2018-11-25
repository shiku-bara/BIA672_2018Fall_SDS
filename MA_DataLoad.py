#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 08:12:03 2018

@author: shiasi
"""

import os
import glob
import re
import pandas as pd
from datetime import datetime as DT

class CollateData():
    
    def __init__ (self):
        
        self.weeklist = ['Weeks1','Weeks2']
        data_file_list = []
        
        for week in self.weeklist:
            raw_file_path = os.path.join(os.getcwd(), week)
            
            allFiles = glob.glob(raw_file_path + "/*.csv")
            
            # The following loop will extract the file date from the file name and add 
            # it as a column in the resulting dataframe        
            for file in allFiles:
                file_date = re.search("([0-9]{4}\-[0-9]{2}\-[0-9]{2})", file).group(1)
                df_from_each_file = pd.read_csv(file, sep="|", header=0)
                df_from_each_file.insert(0, 'FileName', DT.strptime(file_date, '%Y-%m-%d'))
                
                data_file_list.append(df_from_each_file)
            
        raw_data_file_df = pd.concat(data_file_list, axis=0, ignore_index=True)
                
        
        print(raw_data_file_df.shape)

if __name__ == "__main__":
    CollateData()

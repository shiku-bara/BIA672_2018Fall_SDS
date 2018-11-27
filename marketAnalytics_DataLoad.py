#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import re
import pandas as pd
import pickle
from datetime import datetime as DT

class CollateData():
    
    def __init__ (self):
        
        self.weeklist = ['Weeks1','Weeks2']
        self.data_file_list = []
        self.raw_data_file_df = []
        
                
    def concat_datafiles(self):
        for week in self.weeklist:
            raw_file_path = os.path.join(os.getcwd(), week)
            
            allFiles = glob.glob(raw_file_path + "/*.csv")
            
            # The following loop will extract the file date from the file name and add 
            # it as a column in the resulting dataframe        
            for file in allFiles:
                file_date = re.search("([0-9]{4}\-[0-9]{2}\-[0-9]{2})", file).group(1)
                df_from_each_file = pd.read_csv(file, sep="|", header=0)
                df_from_each_file.insert(0, 'FileName', DT.strptime(file_date, '%Y-%m-%d'))
                
                self.data_file_list.append(df_from_each_file)
            
        self.raw_data_file_df = pd.concat(self.data_file_list, axis=0, ignore_index=True)
                
    def write_pickle(self):
        pickle_file = "raw_data_file.pkl"
        max_bytes = 2**31 - 1
        
        #Write
        bytes_out = pickle.dumps(self.raw_data_file_df)
        
        with open(pickle_file, "wb") as f_out:
            for idx in range(0,len(bytes_out), max_bytes):
                f_out.write(bytes_out[idx:idx+max_bytes])
                
        print("Success in saving all the datafiles as a single pickle with dimensions: {}".format(self.raw_data_file_df.shape))


if __name__ == "__main__":
    CollateData()
    

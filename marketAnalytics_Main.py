#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from timeit import default_timer as timer
from marketAnalytics_DataLoad import CollateData
from marketAnalytics_ReconstructDF import ReconstructDataframe

class MainProgram():
    
    def __init__(self):
        self.raw_file = []
        
        self.get_rawfile_as_df()
        self.get_stats()
        
    def get_stats(self):
        print(self.raw_file.columns)
        print(self.raw_file.iloc[4])
        print(self.raw_file.MIX_COUP_SCAN_QTY.unique())
        
    def get_rawfile_as_df(self):
        self.pickle_file = os.path.join(os.getcwd(),"raw_data_file.pkl")
        
        print("Checking whether pickle object exists for the data file...")
        
        if not os.path.isfile(self.pickle_file):
            print("Pickle object doesn't exist. So, creating one...")
            start = timer()
            collate_data_obj = CollateData()
            collate_data_obj.concat_datafiles()
            collate_data_obj.write_pickle()
            end = timer()
            print("Time to create a pickle object: {}".format(end-start))
            
            print("Reconstructing the dataframe from the pickle obj...")
            start = timer()
            reconstruct_df_obj = ReconstructDataframe()
            self.raw_file = reconstruct_df_obj.reconstruct_df()
            end = timer()
            print("Time to reconstruct dataframe after creating pickle: {}".format(end-start))
            print ("Success in reconstructing the raw dataframe with dimensions: {}".format(self.raw_file.shape))
        
        else:
            print("Pickle object exists. So, just reconstructing the dataframe...")
            start = timer()
            reconstruct_df_obj = ReconstructDataframe()
            self.raw_file = reconstruct_df_obj.reconstruct_df()
            end = timer()
            print("Time to reconstruct dataframe without creating pickle: {}".format(end-start))
            print ("Success in reconstructing the raw dataframe with dimensions: {}".format(self.raw_file.shape))
        

       
if __name__ == "__main__":
    MainProgram()
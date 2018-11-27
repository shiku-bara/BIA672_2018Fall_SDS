#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pickle

class ReconstructDataframe():
    
    def __init__(self):
        self.raw_file_df = []

    def reconstruct_df(self):
        pickle_file = "raw_data_file.pkl"
        bytes_in = bytearray(0)
        max_bytes = 2**31 - 1
        input_size = os.path.getsize(pickle_file)
       
        with open(pickle_file, 'rb') as f_in:
            for idx in range (0, input_size, max_bytes):
                bytes_in += f_in.read(max_bytes)
        
        self.raw_file_df = pickle.loads(bytes_in)
        
        return self.raw_file_df
               

if __name__ == "__main__":
    ReconstructDataframe()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:36:16 2023

@author: jacobkeating3
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os 

os.chdir("/Users/jacobkeating3/Downloads")

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10_000
stat = "mean"


boot_stat = []
for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)

    if stat == "median":   
        boot_stat.append(float(boot_sample.median()))
        
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
        
    else:
        raise TypeError("Wrong statistic name")

boot_df = pd.DataFrame({'x': boot_stat})
 
(
 ggplot(boot_df, aes(x = 'x'))+
 geom_histogram()
)



#%%

class BootCI:
    
    def __init__ (self, stat, n_boot, boot_stat, ci_level, dat = None):
        
        self.stat = "mean"
        self.dat = dat
        self.n_boot = 0
        self.boot_stat = None
        self.ci_level = .95
        self.simulations = []
        
    def load_data(self, dat):
        self.dat = dat
    
    def simulation(self):
        
        for i in range(self.n_boot):
            boot_sample = self.dat.sample(self.n_boot, replace = True)

            if stat == "median":   
                self.simulations.append(float(boot_sample.median()))
                
            elif stat == "mean":
                self.simulations.append(float(boot_sample.mean()))
            
            elif stat == "std dev":
                self.simulations.append(float(boot_sample.std()))
            else:
                raise TypeError("Wrong statistic name")
        
    def clear_simulation(self):
        
        self.simulations = []
        

        
        
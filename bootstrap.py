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
import numpy as np

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

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os 
import numpy as np

class BootCI:
    
    def __init__ (self, stat, n_boot, ci_level, dat = None):
        
        self.stat = "mean"
        self.dat = dat
        self.n_boot = n_boot
        self.ci_level = .95
        self.simulations = []
        
    def load_data(self, dat):
        self.dat = dat
        self._n = len(self.dat)
    
    def simulation(self):
        
        for i in range(self.n_boot):
            boot_sample = self.dat.sample(self._n, replace = True)

            if self.stat == "median":   
                self.simulations.append(float(boot_sample.median()))
                
            elif self.stat == "mean":
                self.simulations.append(float(boot_sample.mean()))
            
            elif self.stat == "std dev":
                self.simulations.append(float(boot_sample.std()))
            else:
                raise TypeError("Wrong statistic name")
        
    def clear_simulation(self):
        
        self.simulations = []
        
    def set_stat(self, stat):
        
        self.stat = stat
        self.simulations = []
    
    def plot(self):
        
        boot_df = pd.DataFrame({'x': self.simulations})
         
        p = (
         ggplot(boot_df, aes(x = 'x'))+
         geom_histogram() 
        )
        
        print(p)
    
    def conf_int(self, ll, ul):
        
        if self.simulations != 0:
            conf_level = np.percentile(self.simulations, [ll, ul])
            return conf_level
            
        else:
            raise TypeError("No Data")
            
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]
sim = BootCI("mean", 10000, .95)
sim.load_data(dat)
sim.simulation()     
sim.plot() 
       
    
    
    
    
    
    
    
    
    #%%
    1 - conf_int = a
        a / 2 = b
        conf_int + b = ul
        conf_int - b - ll

        
        
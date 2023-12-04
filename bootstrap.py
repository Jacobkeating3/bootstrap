#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:36:16 2023

@author: jacobkeating3
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os pimport numpy as np

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

#Importing pandas package
import pandas as pd

#Importing matplot package
import matplotlib.pyplot as plt

#Importing plotnine package
from plotnine import *

#Importing os package
import os 

#Importing numpy package
import numpy as np

class BootCI:
    
    def __init__ (self, stat, n_boot, ci_level, dat = None):
        """
        

        Parameters
        ----------
        stat : str
            mean, median, or std dev
        n_boot : int
            number of simulations
        ci_level : float
            confidence level
        dat : data pulled from a file

        Returns
        -------
        Initialized variables of stat, dat, n_boot, ci_level, and simulations

        """
        self.stat = "mean"
        self.dat = dat
        self.n_boot = n_boot
        self.ci_level = .95
        self.simulations = []
        
    def load_data(self, dat):
        """
        

        Parameters
        ----------
        dat : File in which data is being pulled from
            Data

        Returns
        -------
        data and n

        """
        self.dat = dat
        self._n = len(self.dat)
    
    def simulation(self):
        """
        

        Raises
        ------
        TypeError
            If the user types in an input that is not median, mean, or std dev,
            then an error will raise and tell the user to input a new string

        Returns
        -------
        Which simulation is used (median, mean, std dev)

        """
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
        """
        Clears the number of simulations

        Returns
        -------
        Returns a clear set of simulations

        """
        
        self.simulations = []
        
    def set_stat(self, stat):
        """
        Sets the stats

        Parameters
        ----------
        stat : str
            Median, mean, or std dev of data

        Returns
        -------
        inputed stat and a cleared set of simulations

        """
        
        self.stat = stat
        self.simulations = []
    
    def plot(self):
        """
        

        Returns
        -------
        Histogram of the data

        """
        boot_df = pd.DataFrame({'x': self.simulations})
         
        p = (
         ggplot(boot_df, aes(x = 'x'))+
         geom_histogram() 
        )
        
        print(p)
    
    def conf_int(self, ll, ul):
        """
        

        Parameters
        ----------
        ll : float between 0 and 1
            lower limit
        ul :float beteen 0 and 1
            upper limit

        Raises
        ------
        TypeError
            raises an error if there are no simulations

        Returns
        -------
        conf_level : float
            confidence level

        """
        if self.simulations != 0:
            conf_level = np.percentile(self.simulations, [ll, ul])
            return conf_level
            
        else:
            raise TypeError("No Data")

#Changes file directory
os.chdir("/Users/jacobkeating3/Downloads")

#Reads to file
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

#Takes specific data from file
dat = dat["Combined Mileage (mpg)"]

#Runs class
sim = BootCI("mean", 10000, .95)

#Loads data into class
sim.load_data(dat)

#Runs simulation in class
sim.simulation()     

#Runs plot in class
sim.plot() 

#Clears simuation in class
sim.clear_simulation()     
  
#Sets stat in class
sim.set_stat("mean") 

#Runs conf_int in class
sim.conf_int(.025,.975)   
    
    
    
    
    
    
    
    #%%
    1 - conf_int = a
        a / 2 = b
        conf_int + b = ul
        conf_int - b - ll

        
        
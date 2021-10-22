# !/usr/bin/python
# coding=utf-8
import pandas as pd
import numpy as np


class Data_Wrangler():
    
    def __init__(self): 
        pass     

    '''Returns a wrangled and merged dataframe of different csv files with infos on customers
    in a supermarkt.
    '''      
    def create_dataframe(self):
        monday = pd.read_csv("monday.csv", sep=";")
        tuesday = pd.read_csv("tuesday.csv", sep=";")
        wednesday = pd.read_csv("wednesday.csv", sep=";")
        thursday = pd.read_csv("thursday.csv", sep=";")
        friday = pd.read_csv("friday.csv", sep=";")
    
        all_days = [monday, tuesday, wednesday, thursday, friday]
        for weekday in all_days:
            weekday['timestamp'] = pd.to_datetime(weekday['timestamp'])
            weekday['hour'] = weekday['timestamp'].dt.hour

            all_customers = set(weekday.customer_no.values)
            checked_out_customers = set(weekday[weekday["location"] == "checkout"].customer_no.values)
            non_checked_out_customers = list(all_customers.difference(checked_out_customers))
            day = weekday[~weekday.loc[:, "customer_no"].isin(non_checked_out_customers)]

        monday["day"] = "monday"
        tuesday["day"] = "tuesday"
        wednesday["day"] = "wednesday"
        thursday["day"] = "thursday"
        friday["day"] = "friday"

        # combine the DataFrames
        weekdays = monday.append(tuesday.append(wednesday.append(thursday.append(friday))))
        #Change the customers_id's
        weekdays["customer_no"] = weekdays["customer_no"].astype(str) + "_" + weekdays["day"]
        
        return weekdays
    
    
    def get_trans_probs(self):
        '''Returns a 5*5 matrix with the transition probabilities.
        '''
        weekdays = self.create_dataframe()
        weekdays['following'] = weekdays.groupby('customer_no')['location'].shift(-1).to_frame()
        weekdays['following'].replace(np.NaN, 'checkout', inplace=True)



        return pd.crosstab(weekdays['location'], weekdays['following'], normalize='index')

    
    def select_random_id(self):
        '''Selects randomly a customer
        '''
        weekdays = self.create_dataframe()
        customer_id = weekdays['customer_no'].sample(n=1, replace=True).unique()
    
        return customer_id[0]

    
    def get_current_location(self, customer):
        '''Returns back the first location of the customer
        '''
        weekdays = self.create_dataframe()
        customer = self.select_random_id()

        return weekdays[weekdays['customer_no']==customer]['location']

        
    def __repr__(self):
        return ''
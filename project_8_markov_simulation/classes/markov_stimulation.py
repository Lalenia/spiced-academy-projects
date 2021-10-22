# !/usr/bin/python
# coding=utf-8
import pandas as pd
import numpy as np


STATES = ['dairy', 'drinks', 'fruit', 'spices', 'checkout']

class Supermarket:
    '''manages multiple Customer instances that are currently in the market.
    '''

    def __init__(self, name='Lidl'):
        self.customer = Customer()
        self.data = Data_Wrangler()
        self.name = name
        self.customers = []


    def generate_customers_moves(self):
        '''Generates the next moves for of random customers.'''
        
        customers = self.add_new_customers()
        cust_dict = {}
        for customer_id in customers:
            locations = self.customer.generate_next_states(customer_id)

            for loc in locations:
                cust_dict.update({customer_id : loc})
                self.print_customers(cust_dict)
                print(f"Customer {customer_id} is in {loc}.")
            
    
    def generate_customer_move(self):
        '''Generates the first move of a random customer.'''

        customer_id = self.customer.customer_id
        location = self.customer.generate_next_state(customer_id)
        print (f"Customer {customer_id} is in {location}.")


    def is_active(self, customer_id):
        '''If customer is at the checkout it returns false, else True.'''
        
        if customer_id != 'checkout':
            return True
        else:
            return False

    
    def add_customer(self): #create a customer
        '''Creates a list of customers for the Visualization part of the project.'''
        
        customer_id = self.customer.customer_id
        location = self.customer.location
        t_probs =self.customer.transition_probabilities
        self.customers = []
        self.customers.append(Customer(customer_id, location, t_probs))
        return self.customers
    
    def add_new_customers(self):
        """creates a list with random customers"""
        
        random_customers = []
        for customer in self.data.create_dataframe():
            customer = self.data.select_random_id()
            random_customers.append(customer)
    
        return random_customers
        
    def move_customers(self): #control our customers
        '''Moves customer to the next location.'''
        
        customer_id = self.data.select_random_id()
        for shopper in self.customers:
            shopper.generate_next_state(customer_id)

    
    def remove_existing_customers(self):
        """removes every customer that is not active any more."""
        
        customers = self.add_new_customers()
        for customer in customers:
            if is_active(customer) == False:
        #delete customer when he leaves the supermarket
                customers.pop(customer)
    

    def print_customers(self, dict):
        """print all customers with the current time and id in CSV format."""
        
        cust_dict = dict
        for customer_id, loc in cust_dict:
            result = self.data[self.data['customer_no']==customer_id]['timestamp']
        return  pd.row_to_csv('result.csv', index=False)


    def next_minute(self):
        pass

        
class Customer:
    
    def __init__(self): 
    #def __init__(self, customer_id, location, transition_probabilities): 
        '''Creates a customer for the supermarket simulation.'''
        
        self.data = Data_Wrangler()
        self.customer_id = self.data.select_random_id()
        self.location = self.data.get_current_location(self.customer_id)
        self.transition_probabilities = self.data.get_trans_probs()

 
    def generate_next_state(self, customer_id):#takes customer as parameter?
        '''Based on a calculated transition probabilities matrix, returns the next probable state for
    a given customer.'''

        customer_id = self.data.select_random_id()
        location = self.data.get_current_location(customer_id)
        state = location
        state = state.iloc[0]
        P = self.transition_probabilities
    
        return np.random.choice(STATES, p=P.loc[state])


    def generate_next_states(self, customer_id):#takes customer as parameter?
        '''Based on a calculated transition probabilities matrix, returns the next probable states for
    a given customer.'''

        customer_id = self.data.select_random_id()
        locations = self.data.get_locations(customer_id)

        all_states = []
        states = locations
        for state in states:

            next_state = state.iloc[0]
            P = self.transition_probabilities
            state_ = np.random.choice(STATES, p=P.loc[next_state])
            all_states.append(state_)
            if state_  != 'checkout':
                state_ = np.random.choice(STATES, p=P.loc[next_state])
            all_states.append(state_)
            elif state_ == 'checkout':
                all_states.append(state_)
    
            return all_states
        
    
    def __repr__(self):
        return f'Customer {self.name} is in location {self.location}'



class Data_Wrangler():
    
    def __init__(self): 
        pass     

    '''Returns a wrangled and merged dataframe of different csv files with infos on customers
    in a supermarkt.'''  
    
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
        '''Returns a 5*5 matrix with the transition probabilities.'''
        
        weekdays = self.create_dataframe()
        weekdays['following'] = weekdays.groupby('customer_no')['location'].shift(-1).to_frame()
        weekdays['following'].replace(np.NaN, 'checkout', inplace=True)



        return pd.crosstab(weekdays['location'], weekdays['following'], normalize='index')

    
    def select_random_id(self):
        '''Selects randomly a customer'''
        
        weekdays = self.create_dataframe()
        customer_id = weekdays['customer_no'].sample(n=1, replace=True).unique()
    
        return customer_id[0]

    
    def get_current_location(self, customer):
        '''Returns back the first location of the customer'''
        
        weekdays = self.create_dataframe()
        customer = self.select_random_id()

        return weekdays[weekdays['customer_no']==customer]['location']

        
    def __repr__(self):
        return ''


def main():

    customer = Customer()
    supermarket = Supermarket()
    #supermarket.generate_customer_moves()
    supermarket.generate_customer_move()
    supermarket.remove_existing_customers(self)


if __name__ == '__main__':



    main()

    
    
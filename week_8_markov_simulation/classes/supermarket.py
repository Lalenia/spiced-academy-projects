# !/usr/bin/python
# coding=utf-8
import pandas as pd
import numpy as np
from customer import Customer
from data_Wrangler import Data_Wrangler



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
                #work on progress, as well as the function it self!
                self.print_customers(cust_dict)
                print(f"Customer {customer_id} is in {loc}.")
            
    
    def generate_customer_move(self):
        '''Generates the first move of a random customer.'''

        customer_id = self.customer.customer_id
        #return self.customer.generate_next_state(customer_id)
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
                customers.pop(customer)

    def print_customers(self, dict):
        """print all customers with the current time and id in CSV format.
        """
        cust_dict = dict
        for customer_id, loc in cust_dict:
            result = self.data[self.data['customer_no']==customer_id]['timestamp']
        return  pd.row_to_csv('result.csv', index=False)



    def add_new_customers(self):
        """creates a list with random customers
        """
        random_customers = []
        for customer in self.data.create_dataframe():
            customer = self.data.select_random_id()
            random_customers.append(customer)
    
        return random_customers

    def next_minute(self):
        pass


def main():
    
    supermarket = Supermarket()
    customer = self.data.select_random_id()
    self.is_active(customer)
    supermarket.generate_customer_move()
    while True:
        supermarket.generate_customer_move()
        if False:
            self.remove_exitsting_customers(customer)
            self.print_customers(customer)
            



if __name__ == '__main__':



    main()
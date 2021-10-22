# !/usr/bin/python
# coding=utf-8
import pandas as pd
import numpy as np
from data_wrangler import Data_Wrangler


STATES = ['dairy', 'drinks', 'fruit', 'spices', 'checkout']

class Customer:
    
    def __init__(self): 
    #def __init__(self, customer_id, location, transition_probabilities): 
        '''Creates a customer for the supermarket simulation.
        '''
        self.data = Data_Wrangler()
        self.customer_id = self.data.select_random_id()
        self.location = self.data.get_current_location(self.customer_id)
        self.transition_probabilities = self.data.get_trans_probs()

 
    def generate_next_state(self, customer_id):#takes customer as parameter?
        '''Based on a calculated transition probabilities matrix, returns the next probable state for
    a given customer.
    '''

        customer_id = self.data.select_random_id()
        location = self.data.get_current_location(customer_id)
        state = location
        state = state.iloc[0]
        P = self.transition_probabilities
    
        return np.random.choice(STATES, p=P.loc[state])


    def generate_next_states(self, customer_id):#takes customer as parameter?
        '''Based on a calculated transition probabilities matrix, returns the next probable states for
    a given customer.
    '''

        customer_id = self.data.select_random_id()
        locations = self.data.get_locations(customer_id)

        all_states = []
        states = locations
        for state in states:

            next_state = state.iloc[0]
            P = self.transition_probabilities
            state_ = np.random.choice(STATES, p=P.loc[next_state])
            all_states.append(state_)
            #if state_  != 'checkout':
                #state_ = np.random.choice(STATES, p=P.loc[next_state])
            #all_states.append(state_)
            #elif state_ == 'checkout':
                #all_states.append(state_)
    
            return all_states
        
    
    def __repr__(self):
        return f'Customer {self.name} is in location {self.location}'


def main():

    customer = Customer()
    supermarket = Supermarket()
    #supermarket.generate_customer_moves()
    supermarket.generate_customer_move()
    #while True:


if __name__ == '__main__':



    main()

    
    
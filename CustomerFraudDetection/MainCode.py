# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:53:55 2022

@author: Shilpa
"""
import sys
import pandas as pd
import CustomerHistory
from datetime import datetime

class MainCode:
    
    customers = {}
    
    def csvreader(self, argv):
        
        file = argv[1]
        dateparse = lambda x: datetime.strptime(x, '%Y-%m-%d')
        
        for df in pd.read_csv(file, parse_dates = ['date'], date_parser=dateparse, lineterminator = '\n'):
            date = df['date']
            customerID = df['customerID']
            status = df['status']
            
            customer = self.customers.get(customerID)
            if(customer is None):
                customer = CustomerHistory(customerID)
                self.customers.update(customerID, customer)
            
            if(status == 'PURCHASE'):
                customer.addPurchase(date)
                print(date + "," + customerID + "," + customer.getStatus())
            elif(status == 'FRAUD_REPORT'):
                customer.addFraud(date)
            else:
                print("Invalid Report:" + status)
                
def main():
    MainCode().csvreader(sys.argv)
    
if __name__ == '__main__':
    main()
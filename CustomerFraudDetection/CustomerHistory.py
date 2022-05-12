# -*- coding: utf-8 -*-
"""
Created on Wed May 11 00:22:53 2022

@author: Shilpa
"""

class CustomerHistory:
    
    customerID = None
    purchaseHistory = []
    fraudHistory = []
    
    def __init__(self, customerID):
        self.customerID = customerID
    
    def getStatus(self):
        if (len(self.purchaseHistory) == 0) and (len(self.fraudHistory) == 0):
            return "NO_HISTORY"
        elif (len(self.fraudHistory) != 0):
            return "FRAUD_HISTORY:" + str(len(self.fraudHistory))
        else:
            confirmed = 0
            unconfirmed = 0
            currentPurchase = self.purchaseHistory.pop()
            for purchaseDate in self.purchaseHistory[:-1]:
                if (currentPurchase-purchaseDate).days < 90:
                    unconfirmed += 1
                else:
                    confirmed += 1
            if (confirmed == 0):
                return "UNCONFIRMED_HISTORY:" + str(unconfirmed)
            else:
                return "Good_History:" + str(confirmed)
    
    def addPurchase(self, date):
        self.purchaseHistory.append(date)
        
    def addFraud(self, date):
        self.fraudHistory.append(date)
        
    def getCustomerID(self):
        return self.customerID
    
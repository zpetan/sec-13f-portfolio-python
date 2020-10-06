"""
Author: Pepe Tan
Date: 2020-10-06
MIT License
"""


import pandas as pd
from bs4 import BeautifulSoup
from ticker_class import Ticker
from datetime import datetime



class Filing13F:
    """ 
        Class containing common stock portfolio information from an institutional investor.
        1. Parsed from 13F-HR filing from SEC Edgar database.

    """
    
    # If True prints out results in console
    debug = False
    
    
    def __init__(self,filepath=''):
        """ Initialize object """
        self.filepath = filepath # Path of file
        
        # Directly call parse_file() when filepath is provided with __init__
        if self.filepath:
            self.parse_file(self.filepath)
            

    def parse_file(self, filepath=''):
        """ Parses relevant information from 13F-HR text file """
        self.filepath = filepath # Path of file
        
        if self.debug:
            print(self.filepath)
            
        # Opens document and passes to BeautifulSoup object.
        doc = open(filepath)
        soup = BeautifulSoup(doc, 'html.parser') # OBS! XML parser will not work with SEC txt format
        
        # Print document structure and tags in console
        if self.debug:
            print(soup.prettify())
            
            for tag in soup.find_all(True):
                print(tag.name)
        
        ## --- Parse content using tag strings from txt document: <tag> content </tag>
        # OBS html.parser uses tags in lowercase
        
        # Name of filing company
        self.company = soup.find('filingmanager').find('name').string
        # Company identifier: Central Index Key
        self.CIK = soup.find('cik').string
        # Form type: 13F-HR
        self.formtype = soup.find('type').string
        # 13F-HR file number
        self.fileNumber = soup.find('form13ffilenumber').string
        # Reporting date (e.g. 03-31-2020)
        self.period_of_report_date = datetime.strptime(soup.find('periodofreport').string, '%m-%d-%Y').date()
        # Filing date (up to 45 days after reporting date)
        self.filing_date = datetime.strptime(soup.find('signaturedate').string, '%m-%d-%Y').date()
                
        ## --- Parse stock list: Each stock is marked with an infoTable parent tag
        stocklist = soup.find_all('infotable') # List of parent tag objects
        
        # Initialize lists
        name = []     # Company name
        cusip = []    # CUSIP identifier
        value = []    # Total value of holdings
        amount = []   # Amount of stocks
        price_per_share = []  # Share price on reporting day != purchase price
        poc = []      # Put/Call options
        symbol = []   # Trading symbol
        
        # Fill lists with each stock
        for s in stocklist:
            # Company name & Title of class (e.g. COM, Class A, etc)
            n = s.find("nameofissuer").string
            n = n.replace('.','') # Remove dots
            
            c = s.find("titleofclass").string
            if c != "COM":
                name.append(n+" ("+c+")")
            else:
                name.append(n)
                
            # CUSIP identifier
            cusip.append(s.find("cusip").string)
            # Total value of holdings
            v = int(s.find("value").string)
            value.append(v)
            # Amount of stocks
            ssh = int(s.find("shrsorprnamt").find("sshprnamt").string)
            amount.append(ssh)
            # Share price on reporting day (OBS! != purchase price)
            price_per_share.append(round(v*1000/ssh,2))    
            
            # Put/Call options
            put_or_call = s.find("putcall")
            if put_or_call:
                poc.append(put_or_call.string)
            else:
                poc.append('No')
            

        # Create dictionary        
        stock_dict = {"filed name":name,  "cusip":cusip, "value":value, "amount":amount,
                "price_per_share":price_per_share, "put_or_call":poc}
        # Store in dataframe
        data = pd.DataFrame(stock_dict)
        
        # Drop rows with put/call option
        indexes =  data[  data['put_or_call'] != 'No' ].index
        data.drop(indexes, inplace=True)
        # data.set_index('symbol', inplace=True)
        data.set_index('filed name', inplace=True)
        
        self.data = data
        
        return
    
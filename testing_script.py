"""
Author: Pepe Tan
Date: 2020-10-06
MIT License
"""

from Portfolio13FHR import Portfolio


symbols = {
  'JACK IN THE BOX INC': 'JACK',
  'QORVO INC':'QRVO',
  'BOEING CO': 'BA',
  'EBAY INC': 'EBAY',
  'HCA HEALTHCARE INC': 'HCA',
  'VERINT SYS INC': 'VRNT',
  'VENTAS INC': 'VTR',
  'SS&C TECHNOLOGIES HLDGS INC': 'SSNC',
  'VIASAT INC': 'VSAT',
  'BED BATH & BEYOND INC': 'BBBY',
  'DISCOVERY INC (COM SER A)': 'DISCA',
  'TRIP COM GROUP LTD (ADS)': 'TCOM',
  'COPA HOLDINGS SA (CL A)': 'CPA',
  'HELMERICH & PAYNE INC': 'HP',
  'RETAIL OPPORTUNITY INVTS COR': 'ROIC',
  'PRECISION DRILLING CORP (COM 2010)': 'PDS',
  'KIMBALL INTL INC (CL B)': 'KBAL'
}


#%%

CIK_1 = '0001649339'
Name_2 = 'ScionAssetManagement'

portfolio_1 = Portfolio(CIK_1,Name_2)


#%%

portfolio_1.compare_recent_changes()

portfolio_1.data_recent.head()

portfolio_1.plot_recent_shares_change(portfolio_1.data_recent)
portfolio_1.plot_recent_value_change(portfolio_1.data_recent)


# Most recent additions
print(portfolio_1.data_recent_additions[['value_current_perc','shares_change_perc']])

# portfolio_1.plot_recent_shares_change(portfolio_1.data_recent_additions)
# portfolio_1.plot_recent_value_change(portfolio_1.data_recent_additions)

#%%
OFFSET = 120

portfolio_1.analyze_stock('BED BATH & BEYOND INC', symbols['BED BATH & BEYOND INC']=OFFSET)
portfolio_1.analyze_stock('DISCOVERY INC (COM SER A)', symbols['DISCOVERY INC (COM SER A)']=OFFSET)
portfolio_1.analyze_stock('TRIP COM GROUP LTD (ADS)', symbols['TRIP COM GROUP LTD (ADS)']=OFFSET)
portfolio_1.analyze_stock('COPA HOLDINGS SA (CL A)', symbols['COPA HOLDINGS SA (CL A)']=OFFSET)
portfolio_1.analyze_stock('RETAIL OPPORTUNITY INVTS COR', symbols['RETAIL OPPORTUNITY INVTS COR']=OFFSET)
portfolio_1.analyze_stock('PRECISION DRILLING CORP (COM 2010)', symbols['PRECISION DRILLING CORP (COM 2010)']=OFFSET)
portfolio_1.analyze_stock('KIMBALL INTL INC (CL B)', symbols['KIMBALL INTL INC (CL B)']=OFFSET)


#%%

CIK_2 = '0001061768'
Name_2 = 'Baupost Group LLC/MA'

portfolio_2 = Portfolio(CIK_2,Name_2)

#%%
portfolio_2.compare_recent_changes()

portfolio_2.data_recent.head()

portfolio_2.plot_recent_shares_change(portfolio_2.data_recent)
portfolio_2.plot_recent_value_change(portfolio_2.data_recent)

# Most recent additions
print("Recent portfolio additions: \n",portfolio_2.data_recent_additions[['value_current_perc','shares_change_perc']])


#%%
OFFSET = 120

portfolio_2.analyze_stock('HCA HEALTHCARE INC', symbols['HCA HEALTHCARE INC'], PLOT_OFFSET=OFFSET)

portfolio_2.analyze_stock('VERINT SYS INC', symbols['VERINT SYS INC'], PLOT_OFFSET=OFFSET)

portfolio_2.analyze_stock('SS&C TECHNOLOGIES HLDGS INC', symbols['SS&C TECHNOLOGIES HLDGS INC'], PLOT_OFFSET=OFFSET)

portfolio_2.analyze_stock('VIASAT INC', symbols['VIASAT INC'], PLOT_OFFSET=OFFSET)



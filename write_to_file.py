# import pandas lib as pd
import pandas as pd
from ssl_checker import SSLChecker
from datetime import date
today = date.today()
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('sslautomation.xlsx')
header = ["f_name","l_name","email_id","curl","designation","Region"]
dataframe2=pd.read_csv('desire.csv')
list2=list(dataframe2['curl'])
subset = dataframe1[dataframe1['curl'].isin(list2)][header]
subset.to_excel('ssl_'+today+'.xlsx', index=False)

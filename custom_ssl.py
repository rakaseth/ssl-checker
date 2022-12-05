# import pandas lib as pd
import pandas as pd
import sys
filename=sys.argv[0]
from ssl_checker import SSLChecker 
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(filename)
#header = ["f_name","l_name","email_id","curl","designation","Region"]
#dataframe1.to_excel('ssl_1.xlsx', columns = header)
dataframe1['curl'].to_csv("output.csv",index=False)

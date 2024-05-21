# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:46:34 2024

<<<<<<< HEAD
@author: Trevor Gratz, trevor.gratz@piercecountywa.gov
=======
@author: Trevor Gratz, trevormgratz@gmail.com
>>>>>>> 5055f7fa5edbf2544cc7063c1bb85ba28724c693
"""

from HouseholdRollUpSQL_01312024 import sql_households
from HeadofHouseholdsSQL_01312024 import sql_hoh
from LiteralHomelessnessHistorySQL_01312024 import sql_lh

import pandas as pd
import pyodbc
from datetime import date

<<<<<<< HEAD
conn_str = (
    r'Driver=SQL Server;'
    r'Server=EC2AMAZ-KGSIV95.aws.piercecountywa.gov;'
    r'Database=County_Pierce_Reporting;'
    r'Trusted_Connection=yes;'
    )
cnxn = pyodbc.connect(conn_str)
today = date.today()

=======

today = date.today()

cnxn = {'XXX'}

>>>>>>> 5055f7fa5edbf2544cc7063c1bb85ba28724c693
##############################################################################

# Household Features
hhoutpath = r'..\..\..\Data\HouseholdFeatures'
hhoutpath += f'_{today}.pkl'
df_households = pd.read_sql(sql_households,cnxn)
df_households.to_pickle(hhoutpath)

# Head of Household Features
hohoutpath = r'..\..\..\Data\HeadofHousholdFeatures'
hohoutpath += f'_{today}.pkl'
df_hoh = pd.read_sql(sql_hoh,cnxn)
df_hoh.to_pickle(hohoutpath)
<<<<<<< HEAD
df_hoh[['HoH_EnrollmentID', 'HoH_PersonalID']].duplicated().sum()
df_hoh = df_hoh.sort_values(['HoH_EnrollmentID', 'HoH_PersonalID'])
=======
#df_hoh[['HoH_EnrollmentID', 'HoH_PersonalID']].duplicated().sum()
#df_hoh = df_hoh.sort_values(['HoH_EnrollmentID', 'HoH_PersonalID'])
>>>>>>> 5055f7fa5edbf2544cc7063c1bb85ba28724c693

# Literal Homeless History
lhoutpath = r'..\..\..\Data\HouseholdLiteralHomelessnessHistory'
lhoutpath += f'_{today}.pkl'
df_lh = pd.read_sql(sql_lh,cnxn)
df_lh.to_pickle(lhoutpath)

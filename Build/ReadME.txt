The code in this folder builds the initial analytic data set used to train a model predicting successful exit and retention of housing from homelessness. 

Files
1) BuildFeatures_02132024.py
  *  This file pulls in three SQL queries, queries HMIS, then saves the output. The SQL lines are stored in the files:
     * HeadofHouseholdsSQL_01312024.py
	* Using e_prod, limiting to HoH and CE Enrollments, then pulls in data on disability status as well as income and benefits. 
     * HouseholdRollUpSQL_01312024.py
        * Using much of the same data as above, it does not limit to HoH initially. Instead pulls in data on all of the household
          and then aggregates to the Household ID level.
     * LiteralHomelessnessHistorySQL_01312024.py 
<<<<<<< HEAD
        * Gets all literal homeless events occuring prior to a CE enrollment. 
=======
        * Gets all literal homeless events occurring prior to a CE enrollment. 
>>>>>>> 5055f7fa5edbf2544cc7063c1bb85ba28724c693

2) BuildInterventionsOutcomes_02132024.py
  * This file associates housing interventions with CE events, and using this data determines whether or not a household had a successful exit.
  * For details on how this is done see this file '..\..\..\Documentation\Project Generated\OutcomesInterventionDocumentation_02132024.xlsx'
  * Relies on some simple SQL pulls in the InterventionOutcomes_SQL_02122024.py file.

3) BuildAnalticDataSet_02142024.py
<<<<<<< HEAD
  * This file combines the data produced in 1) and 2) into an analytic dataset. It cleans categorical variables that are sparse and continous 
=======
  * This file combines the data produced in 1) and 2) into an analytic dataset. It cleans categorical variables that are sparse and continuous 
>>>>>>> 5055f7fa5edbf2544cc7063c1bb85ba28724c693
    variables that have values that shouldn't be allowed (e.g. negative ages). It exports a training and testing dataset to ensure there is 
    is no leakage.

4) PreprocessAnalyticDataSet_02292024.py
  * This file gets simple imputers, one hot encoders, and standard scalars for all variables. It then uses these to build different
<<<<<<< HEAD
    datasets based on the variables choosen to be included. In other words, it takes a standard dataset for data analysis into an 
=======
    datasets based on the variables chosen to be included. In other words, it takes a standard dataset for data analysis into an 
>>>>>>> 5055f7fa5edbf2544cc7063c1bb85ba28724c693
    array like object coded for ML.
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:58:00 2024

@author: tgratz
"""
# Remap if less than 100 obs or if categories are similar
remap = {'HoH_GenderName': {'More than one gender reported':'Other_Missing',
                            'Non-Binary':'Other_Missing',
                            'Missing_NoAnswer_DoesntKnow':'Other_Missing',
                            'Transgender': 'Other_Missing',
                            'Questioning': 'Other_Missing'},
         'HoH_SexualOrientationName': {'Missing_NoAnswer_DoesntKnow': 'Other_Missing',
                                       'Questioning/Unsure':'Other_Missing',
                                       'Other':'Other_Missing',
                                       'Gay':'Gay_Lesbian',
                                       'Lesbian':'Gay_Lesbian'},
         'HoH_LastGradeCompletedNameAtEntry': {'Grades 5-6':'Less than Grade 6',
                                               'Less than Grade 5':'Less than Grade 6'},
         'HoH_DomesticViolenceWhenOccurred': {None:'None_Missing',
                                              'Data not collected (HUD)':'None_Missing',
                                              'Client prefers not to answer (HUD)':'None_Missing',
                                              "Client doesn't know (HUD)":'None_Missing'},
         'HoH_DomesticViolenceCurrentlyFleeing': {None:'None_Other_Missing',
                                                  'Data not collected (HUD)':'None_Other_Missing',
                                                  'Client prefers not to answer (HUD)':'None_Other_Missing',
                                                  "Client doesn't know (HUD)":'None_Other_Missing'},
         'Household_Education': {'nan': 'Missing_NoAnswer_DoesntKnow',
                                 '0.0': 'Missing_NoAnswer_DoesntKnow',
                                 '1.0': 'Missing_NoAnswer_DoesntKnow',
                                 '2.0': 'Missing_NoAnswer_DoesntKnow',
                                 '3.0': 'Missing_NoAnswer_DoesntKnow',
                                 '8.0': 'Missing_NoAnswer_DoesntKnow',
                                 '4.0': 'Less than Grade 6',
                                 '5.0': 'Less than Grade 6'},
         'Household_MostRecentDomsticViolence' : {"NaN": '0.0'} 
         # Leaving HIVAID unchanged as the Yes category is near 100. No other 
         # healthconditions are similalry sparse, so no ability to 
         # reasonably combine them.
         
         }
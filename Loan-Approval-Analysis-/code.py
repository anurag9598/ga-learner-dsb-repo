# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
bank = pd.DataFrame(bank)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.replace(to_replace = np.nan , value = bank_mode)

#code ends here


# --------------
# Code starts here




avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc='mean')



# code ends here



# --------------
# code starts here


#Approved loan 
loan_approved_se = banks[(banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')].count()

loan_approved_nse = banks[(banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')].count()

percentage_se = (loan_approved_se[-1]*100)/614
print(percentage_se)
percentage_nse = (loan_approved_nse[-1]*100)/614
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)



big_loan_term = loan_term[loan_term>=25].count()


# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()

# code ends here



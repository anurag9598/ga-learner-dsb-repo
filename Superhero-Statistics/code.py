# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data = pd.DataFrame(data)
#Code starts here 
data['Gender'].replace('-','Agender')
gender_count = data['Gender'].value_counts()
plt.plot(gender_count)



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

plt.pie(alignment)
plt.title("Character Alignment")


# --------------
#Code starts here
import scipy.stats

sc_df = data[['Strength','Combat']]

sc_covariance=sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)
ic_df = data[['Intelligence','Combat']]

ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)



# --------------
#Code starts here

total_high = data['Total'].quantile(q=0.99)
super_best = data[data['Total']>total_high]

super_best_names = [i for i in super_best['Name']]
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(1,3,figsize=(20,20))

ax_1.set(title='Intelligence')
ax_2.set(title='Speed')
ax_3.set(title='Power')




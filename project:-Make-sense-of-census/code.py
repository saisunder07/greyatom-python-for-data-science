# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("\nData: \n\n",data)
print("\nType of data: \n\n", type(data))
#Code starts here
census=np.concatenate([data,new_record])
age=census[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)



high=census[census[:,1]>10]
avg_pay_high=high[:,7].mean()
print(avg_pay_high)
low=census[census[:,1]<=10]
avg_pay_low=low[:,7].mean()
print(avg_pay_low)






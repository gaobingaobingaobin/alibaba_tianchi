#calculate the buy numbers everyday

# Imports
from datetime import datetime
from datetime import timedelta
# pandas
import pandas as pd
from pandas import Series,DataFrame

# numpy, matplotlib, seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

train_user_df=pd.read_csv("tianchi_fresh_comp_train_user.csv")
train_item_df=pd.read_csv("tianchi_fresh_comp_train_item.csv")
print("--------------------user-info---------------")
train_user_df.info()
print("--------------------item-info---------------")
train_item_df.info()
train_user_df.drop(['user_geohash'],axis=1,inplace=True)
time_series=train_user_df['time']

train_user_df['time']=[datetime.strptime(x.split()[0],"%Y-%m-%d") for x in time_series]
bought_count=[]
for i_days in range(19):
	start_time=datetime(2014,11,18)
	delta_days=timedelta(i_days)
	test_days=start_time+delta_days
	bought_array=train_user_df[train_user_df['time']==test_days]
	#bought_array=guodu_array[guodu_array['behavior_type']==4]
	b_count=np.shape(bought_array)[0]
	print test_days
	print b_count
	bought_count.append(b_count)
sum_count=sum(bought_count)
print "sum number:"
print sum_count
	


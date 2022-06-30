#  Loading the required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

fifa = pd.read_csv('players_20.csv')
# print(fifa.head())
# for col in fifa.columns:
    # print(col)
# print(fifa.shape)  
#  to know records and column
# value_counts gives the frequency counts of the different category
c1 = fifa['nationality'].value_counts() 
# top five
d1 = fifa['nationality'].value_counts()[0:5] 

# print(d1) 

# Bar plot using matplotlib and submodule pyplot

plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color='g')
# plt.show()
player_salary = fifa[['short_name','wage_eur']]
player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)
# print(player_salary.head())
plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color='r')
# plt.show()
Germany = fifa[fifa['nationality']=='Germany']
# print(Germany.head(5))
Germany1=Germany.sort_values(by=['height_cm'],ascending=False).head(10)
# print(Germany1)
List_Wage = Germany.sort_values(by = ['wage_eur'],ascending= False).head()
# print(List_Wage)

# Portugal
Portugal = fifa[fifa['nationality']=='Portugal']
Portugal_Player= Portugal.sort_values(by=['wage_eur'],ascending=False).head()
print(Portugal_Player)
plt.figure(figsize=(8,8))
plt.bar(list(Portugal_Player['short_name'])[0:5],list(Portugal_Player['wage_eur'])[0:5],color=['red','yellow','blue','pink','green'])
# plt.show()
# print(Portugal)


#Shooting of the player
player_shooting = fifa[['short_name','shooting','club']]
player_shooting1 = player_shooting.sort_values(by=['shooting'],ascending=False).head()
print(player_shooting1)

# Defending of the player
player_defending = fifa[['short_name','nationality','club','defending']]
player_defending1 = player_defending.sort_values(by=['defending'],ascending= False).head()
print (player_defending1)


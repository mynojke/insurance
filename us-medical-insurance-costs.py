#!/usr/bin/env python
# coding: utf-8

# In[97]:


# U.S. Medical Insurance Costs (age,sex,bmi,children,smoker,region,charges) clean data nothing missing rows equal
# smoker bmi dependancy linear regression 
# are there more smokers in south or north 
# avg age in with kids 
# smokers with kids
# how insurance cost increase with age

import csv

def write_data(file):
    age, sex, bmi, children, smoker, region, charges = [], [], [], [], [], [], []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            age.append(row['age'])
            sex.append(row['sex'])
            bmi.append(row['bmi'])
            children.append(row['children'])
            smoker.append(row['smoker'])
            region.append(row['region'])
            charges.append(row['charges'])
    return age,sex,bmi,children,smoker,region,charges

class Data:
    def __init__(self,age,sex,bmi,children,smoker,region,charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges
        
    def smokers_by_reg(self):
        total_smoker_ne, total_smoker_se = 0, 0 
        total_smoker_nw, total_smoker_sw = 0, 0
        population = 0
        for person in range(len(self.smoker)):
            population += 1
            if self.smoker[person] == 'yes':
                if self.region[person] == 'northeast':
                    total_smoker_ne += 1
                elif self.region[person] == 'southeast':
                    total_smoker_se += 1
                elif self.region[person] == 'northwest':
                    total_smoker_nw += 1
                else:
                    total_smoker_sw += 1   
        return print(f"""
                    Total smokers in North-East region: {total_smoker_ne}. 
                    ({round((total_smoker_ne/population*100), 1)}% of insured patients) \n
                    Total smokers in South-East region: {total_smoker_se}.
                    ({round((total_smoker_se/population*100), 1)}% of insured patients) \n
                    Total smokers in North-West region: {total_smoker_nw}.
                    ({round((total_smoker_nw/population*100), 1)}% of insured patients) \n
                    Total smokers in South-West region: {total_smoker_sw}.
                    ({round((total_smoker_sw/population*100), 1)}% of insured patients) \n
                    """)
    
    def avg_age_with_kids(self):
        total_with, count = 0, 0
        for person in range(len(self.age)):
            if int(children[person]) > 0:
                total_with += int(age[person])
                count += 1
        return print(f'''
                    Out of {len(age)} insured patients - {count} ({round((count/(len(self.age))*100), 1)}%) with kids.
                    Average age of insured patients with kids: {round((total_with/count), 1)} years old.
                    ''')
    def linear_regression_age_to_charges(self):
        x_mean = sum([int(n) for n in self.age])/len(self.age)
        y_mean = sum([float(n) for n in self.charges])/len(self.charges)
        
        x = self.age
        y = self.charges
        deviations_xy = [(int(x[i]) - x_mean) * ((float(y[i])) - y_mean) for i in range(len(x))]
        deviations_x_squared = [((int(x[i])) - x_mean) ** 2 for i in range(len(x))]

        b1 = sum(deviations_xy) / sum(deviations_x_squared)
        b0 = y_mean - b1 * x_mean

        return print(f'''
                    The linear regression equation is: y = {round((b0), 2)} + {round((b1), 2)}x (b0, b1 rounded to 2 decimal place).
                    ''')
        
        
        
data_file = Data(*(write_data('insurance.csv')))

data_file.smokers_by_reg()
data_file.avg_age_with_kids()
data_file.linear_regression_age_to_charges()

                 


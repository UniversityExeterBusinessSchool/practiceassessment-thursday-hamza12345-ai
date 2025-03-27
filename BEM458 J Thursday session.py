#######################################################################################################################################################
# 
# Name: Hamza Bin Adeel
# SID: 740099526
# Exam Date: 27/03/2025
# Module: BEMM458
# Github link for this assignment:https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-hamza12345-ai  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""
# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments.
 
# MY SID is 740099526, so the first digit is 7 and the last digit is 6.
allocated_keys=[7,6]
# Initialize an empty list to store (start, end) positions
my_list = []
# Initiating a for loop that finds the position of my allocated words according to my allocated keys.
for i in allocated_keys:
    # My allocated word according to my allocated key
    word=key_comments[i]
    # Using the find command to find the start position of my allocated word in the string.
    start=customer_feedback.find(word)
    end=start+len(word)
    # Appending the empty tuple to fill the start and end position of my allocated words
    my_list.append((start,end))
    # Using the print statement to print the positions of my allocated words 
print(f'The position of my allocated words are {my_list}') 
#Output will be as follows:
# The position of my allocated words are [(129, 136), (18, 28)
##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 26
# As I don't know the formulas for the following metrics, I used AI for the formulas that are mentioned below: 
# Write your code for Operating Profit Margin
# Using the define function to create a formula
def operating_profit_margin(operating_income,revenue):
    return (operating_income/revenue)*100
# Write your code for Revenue per Customer
# Using the define function to create a formula
def revenue_per_customer(total_revenue,number_of_customers):
    return (total_revenue/number_of_customers)
# Write your code for Customer Churn Rate
# Using the define function to create a formula
def customer_churn_rate(lost_customers,total_customers):
    return (lost_customers/total_customers)*100
# Write your code for Average Order Value
# Using the define function to create a formula
def average_order_value (total_revenue,number_of_orders):
    return (total_revenue/number_of_orders)
# Call your designed functions here
# Using the print statement to call the functions here using the first two and last two digits of my SID (74,26) as inputs:
print('The Operating Profit Margin is', operating_profit_margin(74,26))
print('The Revenue Per Customer is', revenue_per_customer(74,26))
print('The Customer Churn Rate is', customer_churn_rate(74,26))
print('The Average Order Value is', average_order_value(74,26))
# The output is as follows:
# The Operating Profit Margin is 284.61538461538464
# The Revenue Per Customer is 2.8461538461538463
# The Customer Churn Rate is 284.61538461538464
# The Average Order Value is 2.8461538461538463

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
# Importing the required libraries for the code
import numpy as np 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

# Defining the price and demand
price = np.array([20,25,30,35,40,45,50,55,60,65,70]).reshape(-1,1)
demand = np.array([300,280,260,240,210,190,160,140,120,100,85])
# Creating a Linear Regression Model and then fitting the model
model = LinearRegression()
model.fit(price,demand)
# Calculating the slope and intercept of the regression because it is required to caluclate the optimal price to maximize revenue
slope = model.coef_[0]
intercept = model.intercept_
# Calculating the average demand
average_demand = np.mean(demand)  
#Calculating the optimal price to maximize revenue using the formula given to me by AI ( Average demand - Intercept)/ Slope
optimal_price = (average_demand-intercept)/slope
print(f"The optimal price at which the revenue is maximized is {optimal_price}.")
# Predicting the demand at £52
predicted_demand = model.predict(np.array([[52]]))
print(f"The predicted demand at £52 is {predicted_demand[0]}.")
# Now we are going to plot the regression line and the predicted demand
# Creating a scatter plot for price vs demand
plt.scatter(price,demand,color='blue',label='Data Points')
#Plotting the regression line
plt.plot(price,model.predict(price),color='red',label='Regression Line')
# Showing the demand on the final output
plt.scatter(52,predicted_demand,color='green',label='Predicted demand')
# Setting the xlabel
plt.xlabel("Price")
# Setting the ylabel
plt.ylabel("Demand")
# Setting the title
plt.title("Linear Regression of Price and Demand")
# Showing the legend
plt.legend()
# Displaying the plot
plt.show()

# Output is as follows:
# The optimal price at which the revenue is maximized is 45.0.
#The predicted demand at £52 is 158.17272727272726.
# The graph is shown in the word file.


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number

# Correcting the variable name and type of conversion
max_value = int(input("Enter your Student ID: "))

random_numbers = [random.randint(1, max_value) for i in range(0,100)]
# Plotting the numbers in a line chart

# Correcting the marker format, attribute name, marker edge color and label spelling and correcting the syntac (removing the ; at the end of the code)
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
# Adding quotes in the title
plt.title("Line Chart of 100 Random Numbers")
# Fixing the xlabel and ylabel assignment
plt.xlabel("Index")
plt.ylabel("Random Number")
# Correcting the legend below 
plt.legend()
plt.grid(True)
plt.show()

# All my corrections/debugging is mentioned as comments in the above code.
# Output is attached in word file



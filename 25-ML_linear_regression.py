#Theory of this code:

#This code demonstrates a simple Linear Regression model using Scikit-learn
#to predict marks based on the number of hours studied. 
#First, LinearRegression is imported from sklearn.linear_model, 
#while the time module is used to create delays during the program execution.
#The X dataset contains the input values representing hours studied,
#and y contains the corresponding marks. A LinearRegression() model is then 
#created and stored in the variable model. The model.fit(X, y) 
#function trains the model by learning the relationship between hours studied 
#and marks. After training, time.sleep(3) pauses the program for three seconds 
#to simulate a training phase. The model.predict([[8]]) function then uses the 
#trained model to predict the marks for a student who studied for 8 hours. 
#Another three-second delay is added to simulate the prediction phase. 
#Finally, print("Predicted Marks:", prediction[0]) displays the predicted marks. 
#Based on the given data, the relationship is perfectly linear, so studying 8 hours 
#results in a predicted score of 110 marks. The [[6]] written at the end is not used 
#by the program; if you want to predict marks for 6 hours, you should use model.predict([[6]]). 
#Overall, this code demonstrates the basic workflow of creating, training, and using a Linear Regression model for prediction.







from sklearn.linear_model import LinearRegression
import time

# Sample dataset
X = [[1], [2], [3], [4], [5]]   # Input (Hours Studied)
y = [40, 50, 60, 70, 80]


# create linear regression model

model = LinearRegression()


#train model
model.fit(X, y)

print("################ model is in training phase #############")
time.sleep(3)


print("###################### predicting phase #################") 
# predict model
prediction = model.predict([[8]])
time.sleep(3)

print("Predicted Marks:", prediction[0])


[[6]]
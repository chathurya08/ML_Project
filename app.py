# Front end reference taken from 
# https://github.com/taruntiwarihp/Projects_DS/blob/master/Phishing%20Site%20URLs%20Prediction/prediction_app.py
# Importing necessary libraries

import uvicorn  # For serving the API
from fastapi import FastAPI  # For creating API endpoints
import joblib  # For loading the trained model
import os  # For handling file paths and directories

# Creating the FastAPI app
app = FastAPI()

# Loading the trained machine learning model
phish_model = open('new_phishing.pkl', 'rb')  # Opening the file in binary mode
phish_model_ls = joblib.load(phish_model)  # Loading the model from the file

# Creating the API endpoint for making predictions
@app.get('/Detector/{feature}')  # Declaring the endpoint and the URL path parameter
async def predict(features):
	# Creating a list to hold the feature value to be predicted
	X_predict = []
	X_predict.append(str(features))  # Adding the value to the list and converting it to a string

	# Making the prediction using the loaded machine learning model
	y_Predict = phish_model_ls.predict(X_predict)

	# Generating the response message based on the prediction result
	if y_Predict == 'bad':
		result = "PHISHING SITE"
	else:
		result = "NOT A PHISHING SITE"

	# Returning the prediction result as a tuple containing the original feature value and the generated response message
	return (features, result)

# Starting the API server
if __name__ == '__main__':
	uvicorn.run(app, host="127.0.0.1", port=8000)



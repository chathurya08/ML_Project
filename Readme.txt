Phishing Website/URL Detector

This is a project that detects whether a URL is a phishing site or not. It is implemented using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python. Logistic Regression is the Algorithm used to build the Machine Learning model.

Dataset Used :

The dataset used for training the machine learning model is a public dataset called Phishing Websites Data Set from the UCI Machine Learning Repository.

https://archive.ics.uci.edu/ml/datasets/phishing+websites

Platform and Tools Used :

IDE: VS Code
Programming language: Python 3.10.5

Installation Required :

All the imported Python libraries from the code need to be installed using the pip install command on the terminal.

Steps of execution :

Extract the folder from the zipped file.
In VS Code, open the folder 'Chathurya_ML'.
Run the new_final_anti_phish.ipynb file. Run all.
This will create the pickled data, after pre-processing and fitting of the data in the ML model.
This pickled file, will be exported to our front-end application created using FASTAPT.
Now, run the app.py code which will give you the link to the FastAPI webpage.
Please go to: http://127.0.0.1:8000/docs#/default/Detector 
The web interface has a form where you can enter a URL to check whether it is a phishing site or not.
Click on 'Try it Out' then enter the URL you want to test.

Link to video : https://drive.google.com/drive/folders/1aRil4MAZU5z_PlU7GPMp4A3uMV_IECfm?usp=sharing
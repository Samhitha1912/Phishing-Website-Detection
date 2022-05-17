# Phishing-Website-Detection

This project aims to analyse how different ML algorithms can be utilized to predict if a website is legitimate or a phishing one.

### Project Structure
The project has four major parts :

1. phishing_website.py - This contains the code for our Machine Learning model to predict if a website is legitimate or not, based on training data in 'dataset.csv' file.
2. app.py - This contains Flask APIs that receives details about the various features of a website through GUI or API calls, determines if it is phishing or legitimate based on our model and returns the value.
3. requirements.txt - This text file has information about all the libraries, modules and packages that have been used while developing this project.
4. stream.py - This is used to create a webpage using Streamlit library that allows users to enter features of the website and displays the predicted nature of website.

### Dataset

Dataset used can be dowloaded from [here](hhttps://www.kaggle.com/code/elgroup/mainnotebook-website/data) 

### Model
Libraries Involved: 

1. Numpy
2. Pandas
3. sklearn
4. matplotlib.pyplot
5. seaborn 
6. time

ML algorithms used:

1. Logistic Regression
2. Naive Bayes
3. Decision Tree Classifier
4. Random Forest

Steps Involved: 

1. Importing the libraries
2. Loading the dataset
3. Data visualization using countplot and heatmap
4. Training and testing the models
5. Conclusion

Results:
```
	Model	Accuracy	Training time (sec)
0	DecisionTreeClassifier	0.954778	0.44
1	RandomForestClassifier	0.950558	0.55
2	LogisticRegression	0.925837	0.07
3	BernoulliNB	0.903527	0.02
```
1. The highest accuracy obtained is 95.478% using Decision tree classifier while least time for training a model is 0.02s using Naive Bayes.
2. The least accuracy obtained is 90.352% using Naive Bayes while highest time for training a model is 0.55s using Random Forest.

### Deploying the model

1. Ensure that you are in the project home directory. Install all the requirements using the command:
```
pip install -r requirements.txt
```
2. Create the machine learning model by running below command:
```
python phishing_website.py
```
This would create a serialized version of our model into a file model.pkl

3. Run app.py using below command to start Flask API
```
python app.py
```

4. You will be navigated to the appropriate URL

You should be able to view the webpage titled 'Phishing Website Detection'. 

Enter valid numerical values(1:completely phished or -1:legitimate or 0:partially phished) in all the input boxes comprising of various features of the website.

If everything goes well, you should be able to see the predcited nature of website on page!

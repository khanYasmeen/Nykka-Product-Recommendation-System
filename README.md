# Nykka-Product-Recommendation-System

# Introduction:- 
In a competitive online retail space, providing personalized recommendations enhances customer experience and increases sales. This project develops a product recommendation system for Nykka using NLP techniques, Python, and a Flask application. The system allows users to input search queries and receive relevant product recommendations.

# Objectives:- 
•	Build a Flask-based front end with a search bar to capture user input.
•	Preprocess product data using tokenization and TF-IDF techniques.
•	Implement Cosine Similarity to generate product recommendations.
•	Display the top 10 product recommendations to users.

# Data Sources:-
I got this data from Kaggle, a popular platform known for its datasets

# Problem Statement:-
•	With the vast number of products available, customers often face challenges in finding the right items. By using NLP and machine learning techniques, the system helps customers discover products efficiently based on their queries
•	Employ exploratory data analysis (EDA) techniques to gain insights into the dataset and identify important features. 

# Data Preprocessing:-
•	Feature Selection: Select relevant features like product names, descriptions, and categories.
•	Feature Combination: Combine the selected features into a single text field for better representation.
•	Tokenization & Vectorization: Apply CountVectorizer to convert the text data into a document-term matrix.
•	Array Conversion: Convert the CountVectorizer output into an array for efficient computation

# Feature Engineering:-
Textual features from product descriptions and categories are used to enhance recommendation accuracy.

# Model Selection:-
Use Cosine Similarity on the array of vectorized product descriptions to recommend the top 10 most similar products.

# Flask Application:-
Build a simple front-end using Flask that takes user queries and provides real-time product recommendations.

# Risks and Challenges:-
•	Managing sparse or missing product data. 
•	Handling scalability as the number of products increases.

# Conclusion:-
The recommendation system is designed to improve product discovery on Nykka by leveraging NLP techniques and providing users with personalized product suggestions.





from flask import Flask, render_template,request
import pickle
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Define the base directory and the path to the pickle file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pkl_path = os.path.join(BASE_DIR, 'products.pkl')

# Load the DataFrame from the pickle file
with open(pkl_path, 'rb') as f:
    df = pickle.load(f)


def content_based_recommendation(user_input, count=10):
    def get_title_from_index(df, index):
        return df[df.index == index]["Product_Name"].values[0]

    i = 0
    cv = CountVectorizer()
    product_list = []

    if user_input.strip() == "":
        return ['Please Enter something']
    else:
        # Create a new row as a DataFrame and use pd.concat to add it
        new_row = pd.DataFrame({"Product_Name": ["external"], "combined_features": [user_input]})
        df_copy = pd.concat([df, new_row], ignore_index=True)

        count_matrix = cv.fit_transform(df_copy["combined_features"])
        cosine_sim = cosine_similarity(count_matrix)

        # Compare the last row (newly added input) with all other rows
        similar_products = list(enumerate(cosine_sim[-1]))
        similarity = sorted(similar_products, key=lambda x: x[1], reverse=True)

        for products in similarity[1:]:
            product_list.append(get_title_from_index(df_copy, products[0]))
            i += 1
            if i >= count:
                break

        return product_list


@app.route('/', methods=['GET', 'POST'])
def recommendations():
    content_based_rec = []
    error_message = None  # Initialize error message
    prod = ''

    if request.method == 'POST':
        prod = request.form.get('prod')  # Get product name from input
        if prod.strip() == "":
            error_message = "Please Enter something"
        else:
            content_based_rec = content_based_recommendation(prod, count=10)

    return render_template('index.html', content_based_rec=content_based_rec, error_message=error_message,prod=prod)
    # return render_template('index.html', content_based_rec=[], error_message=None, prod="")

if __name__ == "__main__":
    app.run(debug=True)
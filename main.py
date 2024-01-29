import pandas as pd
from src import prepare_data, feature_extractor, train_and_evaluate_model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from flask import Flask, request, jsonify
from src.apis import prediction  # Assuming your function is in a file named predict_sentiment.py

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the comment from the POST request
    data = request.json

    # Ensure that the request contains a "comment" field
    if 'comment' not in data:
        return jsonify({'error': 'No comment field provided.'}), 400

    # Extract the comment
    comment = data['comment']

    try:
        # Use the predict_sentiment function to predict the sentiment
        prediction_result = prediction.predict_sentiment(comment, model, vectorizer)

        # Extract sentiment label and probability
        print("here it is ", prediction_result)
        sentiment_label = prediction_result[0][0]  # Access the first element of the first array
        sentiment_probability = prediction_result[1][0]  # Access the first element of the second array

        print("Sentiment is: ", sentiment_label)
        print("Probability is: ", sentiment_probability)
        print("Type is", type(sentiment_label))

        # Return the prediction as a JSON response
        return jsonify({'sentiment': sentiment_label, 'probability': float(sentiment_probability)}), 200

    except Exception as e:
        # If an error occurs, return an error message
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Assuming the CSV file is in the same directory as your script
    dataframe = prepare_data.load_and_preprocess_data("data/sentiment_dataset.csv")
    tfidf_features, tfidf_feature_names, vectorizer = feature_extractor.extract_features(dataframe)

    # TF-IDF features are in sparse matrix format, to view them in DataFrame format:
    tfidf_df = pd.DataFrame(tfidf_features.toarray(), columns=tfidf_feature_names)

    y = dataframe['Sentiment']

    # Split the dataset into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(tfidf_features, y, test_size=0.2, random_state=42)
    # Assuming X_train, y_train, X_test, and y_test are already defined
    model, test_predictions = train_and_evaluate_model.train_and_evaluate(X_train, y_train, X_test, y_test)

    accuracy = accuracy_score(y_test, test_predictions)

    # Generate a classification report
    report = classification_report(y_test, test_predictions, zero_division=0)

    # Generate a confusion matrix
    conf_matrix = confusion_matrix(y_test, test_predictions)

    app.run(debug=True, host='0.0.0.0', port=5000)

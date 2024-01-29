import numpy as np

from src import prepare_data


def predict_sentiment(comment, model, vectorizer):
    # Preprocess the comment
    preprocessed_comment = prepare_data.preprocess_text(comment)

    # Transform the preprocessed comment into the same feature space as the model was trained on
    features_2d = vectorizer.transform([preprocessed_comment])

    # Use the model to predict the class probabilities.
    probabilities = model.predict_proba(features_2d)

    # Get the predicted class with the highest probability.
    predicted_class = model.classes_[np.argmax(probabilities, axis=1)]

    # Get the confidence (probability) of the predicted class.
    confidence = np.max(probabilities, axis=1)

    prediction = (predicted_class, confidence)
    return prediction

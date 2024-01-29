import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_features(dataframe, max_features=1000):
    # Initialize a TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(max_features=max_features)

    # Fit and transform the preprocessed comments
    if type(dataframe) is str:
        series = pd.Series([dataframe])
    else:
        series = dataframe['Preprocessed Comment']
    features = tfidf_vectorizer.fit_transform(series)

    # Get the feature names for later use
    feature_names = tfidf_vectorizer.get_feature_names_out()

    return features, feature_names, tfidf_vectorizer

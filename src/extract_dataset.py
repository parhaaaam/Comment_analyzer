import pandas as pd
import nltk

# Ensure that NLTK's resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')


def load_data(filepath):
    # Load the dataset into a pandas DataFrame
    df = pd.read_csv(filepath)
    return df



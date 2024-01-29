import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import nltk

from src import extract_dataset

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_text(text, use_lemmatization=False):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    if use_lemmatization:
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    else:
        # Stemming
        stemmer = SnowballStemmer('english')
        tokens = [stemmer.stem(token) for token in tokens]

    # Join tokens back into a single string
    return ' '.join(tokens)


# Function to load and preprocess the data
def load_and_preprocess_data(filepath, use_lemmatization=False):
    # Load the dataset into a pandas DataFrame
    df = extract_dataset.load_data(filepath)
    # Apply the preprocessing to each comment
    df['Preprocessed Comment'] = df['Comment'].apply(lambda x: preprocess_text(x, use_lemmatization))
    return df

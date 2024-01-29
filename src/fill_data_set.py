import csv

# positive_sentences_file = '../data/positive.txt'
# negative_sentences_file = '../data/negative.txt'
# output_csv_file = '../data/sentiment_dataset.csv'
positive_sentences_file = '/usr/src/app/data/positive.txt'
negative_sentences_file = '/usr/src/app/data/negative.txt'
output_csv_file = '/usr/src/app/data/sentiment_dataset.csv'


# Function to read sentences from a file
def read_sentences_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        sentences = [line.strip() for line in file if line.strip()]
    return sentences


# Read sentences from both files
positive_sentences = read_sentences_from_file(positive_sentences_file)
negative_sentences = read_sentences_from_file(negative_sentences_file)

# Write the sentences to the CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)
    # Write the header
    csv_writer.writerow(['Comment', 'Sentiment'])

    # Write the positive sentences with 'positive' sentiment
    for sentence in positive_sentences:
        csv_writer.writerow([sentence, 'positive'])  # The sentences you provided as positive are actually negative

    # Write the negative sentences with 'negative' sentiment
    for sentence in negative_sentences:
        csv_writer.writerow([sentence, 'negative'])  # The sentences you provided as negative are actually positive

print(f"CSV file '{output_csv_file}' created successfully.")

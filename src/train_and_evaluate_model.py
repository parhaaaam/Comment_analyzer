from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def train_and_evaluate(X_train, y_train, X_test, y_test):
    # Initialize the Logistic Regression model
    model = LogisticRegression(max_iter=1000)

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Predict on the training data
    train_predictions = model.predict(X_train)
    train_accuracy = accuracy_score(y_train, train_predictions)
    print(f'Training Accuracy: {train_accuracy * 100:.2f}%')

    # Predict on the testing data
    test_predictions = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, test_predictions)
    print(f'Testing Accuracy: {test_accuracy * 100:.2f}%')

    # Generate and print a classification report
    report = classification_report(y_test, test_predictions, zero_division=0)
    print(report)

    # Return the trained model and the test predictions
    return model, test_predictions

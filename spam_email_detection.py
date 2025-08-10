import nltk
import random
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import SklearnClassifier
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download NLTK data
nltk.download("stopwords")
nltk.download("punkt")

# Sample dataset of spam and non-spam emails (feature: email text, label: spam or not)
emails = [
    ("Win a free iPhone", "spam"),
    ("Hi, when are we meeting?", "not spam"),
    ("Buy one get one free", "spam"),
    ("Lunch today at 1 PM?", "not spam"),
    ("Exclusive offer: 50% off on all products", "spam"),
    ("Reminder: Parent-Teacher meeting tomorrow", "not spam"),
    ("Congratulations! You've won a vacation package", "spam"),
    ("Invitation: Join us for a conference", "not spam"),
    ("Limited-time offer: Save big on electronics", "spam"),
    ("Meeting agenda for next week", "not spam"),
    ("Your account statement is ready", "spam"),
    ("Team building event this Saturday", "not spam"),
    ("Get rich quick with this investment opportunity", "spam"),
    ("Reminder: Pay your bills by the end of the month", "not spam"),
    ("Claim your prize by clicking the link", "spam"),
    ("Important update: Software security patch", "not spam"),
]

# Preprocess the data
stop_words = set(stopwords.words("english"))

def preprocess(email):
    words = word_tokenize(email.lower())  # Tokenize and convert to lowercase
    words = [word for word in words if word.isalpha()]  # Remove punctuation
    words = [word for word in words if word not in stop_words]  # Remove stop words
    return FreqDist(words)

# Extract features and labels
featuresets = [(preprocess(email), label) for (email, label) in emails]
print("Features : ", featuresets)


# Split data into training and testing sets
train_set, test_set = train_test_split(featuresets, test_size=0.2, random_state=42)
print("Training : ", train_set)
print("Test : ", test_set)


# Train the Naive Bayes classifier
classifier = SklearnClassifier(MultinomialNB())
classifier.train(train_set)

# Test the classifier
predictions = [classifier.classify(email) for (email, _) in test_set]
true_labels = [label for (_, label) in test_set]

print("Pred : ", predictions)
print("TL : ", true_labels)



# Evaluate the classifier
accuracy = accuracy_score(true_labels, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")
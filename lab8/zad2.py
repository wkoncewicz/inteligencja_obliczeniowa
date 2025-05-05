from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

with open("review1.txt", "r", encoding="utf-8") as f1:
    review1 = f1.read()

with open("review2.txt", "r", encoding="utf-8") as f2:
    review2 = f2.read()

scores1 = sia.polarity_scores(review1)
scores2 = sia.polarity_scores(review2)

print("Recenzja 1")
print(f"Pos: {scores1['pos']}")
print(f"Neg: {scores1['neg']}")
print(f"Neu: {scores1['neu']}")
print(f"Compound: {scores1['compound']}")
print("Recenzja 2")
print(f"Pos: {scores2['pos']}")
print(f"Neg: {scores2['neg']}")
print(f"Neu: {scores2['neu']}")
print(f"Compound: {scores2['compound']}")

# Recenzja 1
# Pos: 0.101
# Neg: 0.117
# Neu: 0.783
# Compound: -0.658
# Recenzja 2
# Pos: 0.395
# Neg: 0.0
# Neu: 0.605
# Compound: 0.9938
# Vader ma problemy z określeniem czy recenzja jest negatywna,
# pierwsza recenzja ma znacząco negatywne wybrzmienie jednak program określa ją jako neutralną
# Compound jednak wskazuje na negatywność
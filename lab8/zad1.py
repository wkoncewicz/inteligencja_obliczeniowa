import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

tokens = word_tokenize(text)
print("Liczba tokenów:", len(tokens))

words = [word for word in tokens if word.isalpha()]
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Liczba słów po usunięciu stop-words:", len(filtered_words))

my_stop_words = {'also', 'data'}
stop_words.update(my_stop_words)
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Liczba słów po usunięciu moich stop-words:", len(filtered_words))

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in filtered_words]
print("Liczba słów po lematyzacji:", len(lemmatized_words))

word_freq = Counter(lemmatized_words)
most_common = word_freq.most_common(10)
words_x, counts_y = zip(*most_common)

plt.figure(figsize=(10, 6))
plt.bar(words_x, counts_y, color='skyblue')
plt.xlabel("Słowa")
plt.ylabel("Liczba wystąpień")
plt.title("10 najczęściej występujących słów w artykule")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

text_for_wordcloud = ' '.join(lemmatized_words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Chmura tagów dla artykułu")
plt.show()
import text2emotion as te
import nltk

nltk.download('punkt_tab')

with open("review1.txt", "r", encoding="utf-8") as f1:
    review1 = f1.read()

with open("review2.txt", "r", encoding="utf-8") as f2:
    review2 = f2.read()

emotions1 = te.get_emotion(review1)
emotions2 = te.get_emotion(review2)

print("Recenzja 1:")
for emotion, score in emotions1.items():
    print(f"{emotion}: {score}")

print("Recenzja 2:")
for emotion, score in emotions2.items():
    print(f"{emotion}: {score}")

# Recenzja 1:
# Happy: 0.05
# Angry: 0.16
# Surprise: 0.26
# Sad: 0.32
# Fear: 0.21
# Recenzja 2:
# Happy: 0.44
# Angry: 0.06
# Surprise: 0.12
# Sad: 0.06
# Fear: 0.31
#
# Obu recenzentów program określa jako przestraszonych??? 1 recenzent ewidentnie nie jest zadowolony a 2 jest
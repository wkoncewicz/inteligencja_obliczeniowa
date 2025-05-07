import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

transactions = df.astype(str).values.tolist()

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
ohe_df = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(ohe_df, min_support=0.05, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)

survival_rules = rules[rules['consequents'].astype(str).str.contains("Yes|No")]

survival_rules = survival_rules.sort_values(by='lift', ascending=False)

print("\nTop survival-related rules sorted by lift:\n")
print(survival_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

top_rules = survival_rules.head(10)
plt.figure(figsize=(12, 6))
plt.barh(
    [str(rule) for rule in top_rules['antecedents']],
    top_rules['confidence'],
    color='skyblue'
)
plt.xlabel('Confidence')
plt.title('Top 10 Association Rules Predicting Survival')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


#Mało dzieci, więc nie ma dla nich przewidzianego niczego,
#im gorsza klasa tym większe wskazanie na śmierć lol
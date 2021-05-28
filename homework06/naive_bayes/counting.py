import typing as tp
import bayes
import find
from db import News, session

s = session()
rows = s.query(News).all()
stop_sign = int(0.7 * len(rows))  # 70:30
extracts = []
labels = []

for i in range(len(rows)):
    row = s.query(News).filter(News.id == (i + 1)).first()
    extracts.append(row.title)
    labels.append(row.label)

extracts = [find.clear(x).lower() for x in extracts]
X_train, X_test = extracts[:stop_sign], extracts[stop_sign:]
y_train, y_test = labels[:stop_sign], labels[stop_sign:]


model = bayes.NaiveBayesClassifier(alpha=0.05)
model.fit(X_train, y_train)


print("Классификатор: ", +  model.score(X_test, y_test))

import os
import pathlib
import pickle
import typing as tp

from bottle import redirect, request, route, run, template
from bayes import NaiveBayesClassifier
from db import News, session
from scraputils import get_news
import stemmer




@route("/")
def index() -> tp.Any:
    redirect("/news")


@route("/news")
def news_list() -> tp.Any:
    s = session()
    rows = s.query(News).filter(News.label == None).all()

    return template ("news_template.tpl", rows=rows)



@route("/add_label/")
def add_label():
    s = session()
    entry = s.query(News).filter(News.id == request.query["id"]).first()
    entry.label = request.query["label"]
    s.commit()
    redirect("/news")



@route("/update")
def update_news():
    new_arrivals = get_news("https://news.ycombinator.com/newest")
    s = session()
    marker = s.query(News).first()
    batch_size: int = 30
    for i, e in enumerate(new_arrivals):
        if e["title"] == marker.title and e["author"] == marker.author:
            batch_size = i
    new_arrivals = new_arrivals[:batch_size]
    for entry in new_arrivals:
        obj = News(
            title=entry["title"],
            author=entry["author"],
            url=entry["url"],
            comments=entry["comments"],
            points=entry["points"],
        )
        s.add(obj)
        s.commit()
    redirect("/news")



@route("/classify")
def classify_news():
    s = session()
    unclassified: tp.List[tp.Tuple[int, str]] = [
        (i.id, stemmer.clear(i.title))
        for i in s.query(News).filter(News.label == None).all()
    ]
    X = [i[1] for i in unclassified]
    if not pathlib.Path(
        f"{os.path.dirname(os.path.realpath(__file__))}/../model/model.pickle"
    ).is_file():
        raise ValueError(
            "Classifier is untrained! Please mark enough news to adequately train the model and run bayes.py to save it."
        )
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/../model/model.pickle", "rb"
    ) as model_file:
        model = NaiveBayesClassifier(alpha=0.1)
        model = pickle.load(model_file)
    labels = model.predict(X)
    for i, e in enumerate(unclassified):
        extract = s.query(News).filter(News.id == e[0]).first()
        extract.label = labels[i]
        s.commit()
    rows = s.query(News).filter(News.label != None).order_by(News.label).all()

    return template("classified_template.tpl", rows=rows)




if __name__ == "__main__":
    run(host="localhost", port=8080)

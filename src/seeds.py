import connect
from models import Tag, Authors, Quotes



def add_author(author: dict) -> Authors:
    author = Authors(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
        ).save()
    return author

def add_quote(quote: dict) -> Quotes:
    author = Authors.objects.get(fullname=quote["author"])
    tags = []
    for tag in quote['tags']:
        tags.append(Tag(name=tag))
    
    quote = Quotes(tags=tags,
                   author=author,
                   quote=quote['quote']).save()

    return quote


if __name__ == "__main__":
    import json

    json_authors_path = 'json/authors.json'
    json_qoutes_path = 'json/qoutes.json'

    with open(json_authors_path) as file:
        authors = json.load(file)

    try:
        for author in authors:
            add_author(author)
    except Exception as e:
        print(e)

    with open(json_qoutes_path) as file:
        qoutes = json.load(file)
    try:
        for qoute in qoutes:
            add_quote(qoute)
    except Exception as e:
        print(e)

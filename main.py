import re

import src.connect
from src.models import Authors, Quotes

def main():
    while True:
        input_cmd = input("Enter the command: ")
        
        if input_cmd.lower() == "exit":
            break

        try:
            cmd, args = re.split(":", input_cmd)
        except Exception as e:
            print("I don't understand you")
            continue

        if cmd.lower() == "name":
            try:
                author = Authors.objects.get(fullname = args)
            except Exception as e:
                print(e)
                continue
            
            quotes = Quotes.objects(author = author.id)
            for quote in quotes:
                print(quote.quote)

        elif cmd.lower() == "tag":
            quotes = Quotes.objects(tags__name=args)
            for quote in quotes:
                print(quote.quote)
        elif cmd.lower() == "tags":
            tags = re.split(",", args)
    
            quotes = Quotes.objects(tags__name__in=tags)
            for quote in quotes:
                print(quote.quote)
        else:
            print("I don't understand you")

if __name__ == "__main__":
    main()
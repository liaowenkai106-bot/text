from scrapling.parser import Selector


HTML = """
<html>
  <body>
    <div class="quote">
      <span class="text">“The world as we have created it is a process of our thinking.”</span>
      <small class="author">Albert Einstein</small>
    </div>
    <div class="quote">
      <span class="text">“It is our choices, Harry, that show what we truly are.”</span>
      <small class="author">J.K. Rowling</small>
    </div>
  </body>
</html>
"""


def main():
    page = Selector(HTML)
    quotes = page.css(".quote")

    print("共找到", len(quotes), "条名言\n")

    for i, quote in enumerate(quotes, start=1):
        text = quote.css(".text::text").get()
        author = quote.css(".author::text").get()
        print(f"{i}. {text} —— {author}")


if __name__ == "__main__":
    main()

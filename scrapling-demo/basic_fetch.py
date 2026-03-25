from scrapling.fetchers import Fetcher


def main():
    url = "https://quotes.toscrape.com/"
    page = Fetcher.get(url)

    print("页面标题:", page.css("title::text").get())
    print("前 5 条名言:\n")

    quotes = page.css(".quote")
    for i, quote in enumerate(quotes[:5], start=1):
        text = quote.css(".text::text").get()
        author = quote.css(".author::text").get()
        print(f"{i}. {text} —— {author}")


if __name__ == "__main__":
    main()

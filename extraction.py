from newspaper import Article

url = 'https://www.gazzetta.it/Calcio/Serie-A/Juventus/06-08-2019/dybala-altri-tesoretto-la-juve-andra-via-come-mandzukic-matuidi-3401461898595.shtml'
article = Article(url, language='en')
article.download()

article.parse()

print(article.title, "\n\n")
print(article.text)

# article.nlp()

# print(article.keywords)

with open("OUT.txt", "w") as text_file:
	text_file.write(article.text)
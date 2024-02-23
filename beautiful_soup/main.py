from bs4 import BeautifulSoup

with open("website.html") as file:
    conents = file.read()

soup = BeautifulSoup(conents, "html.parser")
print(soup.title)
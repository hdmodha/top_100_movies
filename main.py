from bs4 import BeautifulSoup


with open("movies_website.html") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
all_h3s = soup.find_all(name="h3")
movies100 = []
for item in all_h3s:
    movies100.append(item.getText())
movies100.reverse()
with open("movies.txt", "w") as file:
    for item in movies100:
        file.writelines(item)
        file.write("\n")

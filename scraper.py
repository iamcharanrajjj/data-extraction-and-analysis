import requests
from bs4 import BeautifulSoup
import pandas as pd

#  Excel file is in current directory
input_df = pd.read_excel("./Input.xlsx")

def extract_text(url):
    # Get the website content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the article title and text
    title = soup.find('h1').text
    paragraphs = soup.find_all('p')

    article_text = title + "\n"
    for paragraph in paragraphs:
        article_text += paragraph.text + "\n"
      
    return article_text

# Write the extracted text to a file
for i, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    article_text = extract_text(url)

    with open(f'extracted_texts/{url_id}.txt', 'w', encoding="utf-8") as file:
        file.write(article_text)

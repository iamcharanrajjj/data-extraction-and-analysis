# Text Data Extraction and Analysis 

This repository contains a Python project that aims to extract online articles from URLs and perform a basic Natural Language Processing analysis on the text.

The system performs two main tasks: (i) it extracts article texts from a list of URLs, and (ii) performs text analysis on the articles generating valuable insights.

It reads a list of URLs from an Excel file, then for each URL, it extracts the page's main content (excluding header, footer, etc.), and saves the text into independent text files. This is followed by an NLP analysis, in which the text is tokenized into sentences and words, cleaned of stop words, and then a set of scores/counts are generated for each article. 

### Requirements

The project uses Python 3.5+ and the following Python packages:

- Pandas
- Requests
- BeautifulSoup
- NLTK
- Textstat
- TextBlob

installation using pip:
```sh
pip install pandas requests beautifulsoup4 nltk textstat textblob
```

### Workflow

1. Read the URLs from an Excel file (input.xlsx)
2. For each URL, extract the title and the whole textual content of the article.
3. Each extracted text is saved into a .txt file.
4. Perform textual analysis on each saved text file. Compute various text metrics, including sentiment scores (polarity and subjectivity), word, sentence counts, Fog index, syllable count per word, and personal pronouns count.
5. The output of the analysis is saved into an Excel file (Output.xlsx).

### Scripts

- `scraper.py`: This script extracts the textual content of the online articles.
- `text_analyzer.py`: This script handles textual analysis and computation of scores.

### Variables

- Word Count: The total count of words in the article. 
- Sentence Count: The total count of sentences in the article.
- Average Sentence Length: The average length of sentences in the article.
- Complex Word Count: The count of complex words (a word with more than three syllables) in the article.
- Percentage of complex words: The percentage of complex words in the text.
- Polarity Score: Measure of how positive or negative the text sentiment is.
- Subjectivity Score: Measure of how subjective or objective the text is.
- Fog Index: The readability of the English writing (higher scores indicate material that is more difficult to read).
- Personal Pronouns: The count of first-person pronouns in the text.
- Average word length: The average length of words in the article.

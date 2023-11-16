

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words('english'))

def analyze_text(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '')

    sentences = sent_tokenize(data)
    words = word_tokenize(data)

    words = [word for word in words if not word in stop_words]

    word_count = len(words)
    sentence_count = len(sentences)
    average_sentence_length = word_count / sentence_count

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import textstat
from textblob import TextBlob

def sentiment_analysis(text: str):
    blob = TextBlob(text)

    return {
        'polarity_score': blob.sentiment.polarity,
        'subjectivity_score': blob.sentiment.subjectivity
    }

def analyze_text(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '')
    from textstat import syllable_count

def analyze_text(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = file.read().replace('\n', '')

    words = word_tokenize(data)

    complex_word_count = 0
    for word in words:
        if syllable_count(word) >= 3: 
            complex_word_count += 1

    percentage_complex_words = (complex_word_count / len(words)) * 100  
    sentiments = sentiment_analysis(data)

    sentences = sent_tokenize(data)
    words = word_tokenize(data)

    words = [word for word in words if not word in stop_words]

    syllable_count = textstat.syllable_count(data)
    sentences_count = len(sentences)
    word_count = len(words)
    avg_word_length = syllable_count / word_count

    positive_score = sentiments['polarity_score'] if sentiments['polarity_score'] > 0 else 0
    negative_score = abs(sentiments['polarity_score']) if sentiments['polarity_score'] < 0 else 0
    polarity_score = sentiments['polarity_score']
    subjectivity_score = sentiments['subjectivity_score']
    avg_sentence_length = word_count / sentences_count
    fog_index = textstat.gunning_fog(data)

    personal_pronouns = len(re.findall(r'\b(I|me|my|mine|we|us|our|ours)\b', data, re.IGNORECASE))

    return {
        'positive_score': positive_score,
        'negative_score': negative_score,
        'complex_word_count': complex_word_count,
        'percentage_of_complex_words': percentage_complex_words,
        'polarity_score': polarity_score,
        'subjectivity_score': subjectivity_score,
        'avg_sentence_length': avg_sentence_length,
        'fog_index': fog_index,
        'avg_number_words_per_sentence': avg_sentence_length,  # similar to avg_sentence_length
        'word_count': word_count,
        'syllable_per_word': syllable_count / word_count,
        'personal_pronouns': personal_pronouns,
        'avg_word_length': avg_word_length,
    }

output_df_columns = ["URL_ID", "URL", 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
                       'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE',
                       'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']
output_df = pd.DataFrame(columns=output_df_columns)

for i, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    word_count, sentence_count, average_sentence_length = analyze_text(f'extracted_texts/{url_id}.txt')

    output_df = output_df.append({"URL_ID": url_id, "URL": url, "WORD COUNT": word_count, 
                                  'AVG SENTENCE LENGTH': average_sentence_length}, ignore_index=True)

output_df.to_excel('./Output.xlsx', index=False)

from PyPDF2 import PdfReader
import nltk
import re

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def calculate_gulpease_index(text):
    words = nltk.word_tokenize(text)
    num_words = len(words)
    
    letters = sum(c.isalpha() for w in words for c in w)
    
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    
    if num_words != 0:
        LP = (letters * 100) / num_words
        FR = (num_sentences * 100) / num_words
        index = 89 - (LP / 10) + (3 * FR)
        if index > 100:
            index = 100
        return index
    else:
        return None

def main():
    file_name = input("Enter the name or path of PDF you want to analyze: ")

    try:
        text = extract_text_from_pdf(file_name)
        gulpease_index = calculate_gulpease_index(text)
        
        if gulpease_index is not None:
            print("Number of words in the document:", len(re.findall(r'\w+', text)))
            print("Number of letters in the document:", len(re.findall(r'\w', text)))
            print("Number of sentences in the document:", len(re.findall(r'[.]+|[;]+', text)))
            print("Gulpease index (restricted):", gulpease_index)
            print("Note: The restricted Gulpease index does not consider certain punctuation marks as sentence delimiters.")
        else:
            print("Error calculating Gulpease index.")
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    nltk.download('punkt')
    main()
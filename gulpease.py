from PyPDF2 import PdfReader
import re

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def calculate_gulpease_index(text):
    words = len(re.findall(r'\w+', text))
    letters = len(re.findall(r'\w', text))
    sentences = len(re.findall(r'[.]+|[;]+', text))

    if words != 0:
        index = 89 + ((300 * sentences) - (10 * letters)) / words
        if index > 100:
            index = 100
        return index
    else:
        return None

def main():
    file_name = input("Enter the name of the PDF file to calculate readability index: ")

    try:
        text = extract_text_from_pdf(file_name)
        gulpease_index = calculate_gulpease_index(text)
        
        if gulpease_index is not None:
            print("Number of words in the document:", len(re.findall(r'\w+', text)))
            print("Number of letters in the document:", len(re.findall(r'\w', text)))
            print("Number of sentences in the document:", len(re.findall(r'[.]+|[;]+', text)))
            print("")
            print("Gulpease Index (restricted):", gulpease_index)
            print("")
            print("Note: The restricted Gulpease index does not consider certain punctuation marks as sentence delimiters.")
        else:
            print("Error calculating Gulpease index.")
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()

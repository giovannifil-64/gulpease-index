# gulpease-index
The Gulpease index is a readability metric for the Italian language, but it's also widely used for other languages. The script takes a PDF file as input and calculates the Gulpease score, providing insight into the document's composition. It's a handy tool to measure the complexity of your written content. Feel free to clone the repository and use the script to analyze the readability of your documents.
The index is calculated with the following formula

$G = 89 + \left[\frac{{300 \times (\text{number of all phrases}) - 10 \times (\text{number of all letters})}}{{\text{number of words}}}\right]$

## Features:

- Accepts PDF files as input for parsing.
- Provides scores for words, letters and sentences.
- Easily integrated into existing projects or workflows.

## Usage
- Clone the repository to your local machine.
- Run the Python script with your desired text file as input.
- The Gulpease score will be printed in the therminal in this format:
```
Number of words in the document: 2825
Number of letters in the document: 13791
Number of sentences in the document: 1495

Gulpease Index (restricted): 100
Note: The restricted Gulpease index does not consider certain punctuation marks as sentence delimiters.
```

> [!IMPORTANT]
PyPDF2 is required to run this script. You can install it using the relative PiP command: ```pip install PyPDF2```

## License:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This code is released under the MIT License.

## Author:
Based on the repo [Indice-Gulpease](https://github.com/imriccardop/Indice-Gulpease) by imriccardop

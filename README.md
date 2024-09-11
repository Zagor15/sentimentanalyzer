# A sentiment analyzer for english texts

A program which analyze the emotions of a text (only in English) using NLTK : Natural Language Toolkit and vader lexicon.
The interface use Tkinter.

There is two versions:

- sentiment.py which allows the user to submit a text to analyze.

- sentimentweb which allows the user to submit an url. The text of the webpage will be wrapped using BeautifulSoup and then analyzed like in sentiment.py. Sentimentweb will wrap the whole page text and not just the article or blog paper, so it can reduce the precision of the analysis.

## Disclaimer : 

Use only sentimentweb on website autorizing wrapping



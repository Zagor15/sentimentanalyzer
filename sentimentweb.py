import requests
from bs4 import BeautifulSoup
import tkinter as tk
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

def get_page_text(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the request with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all text from the webpage
        text = soup.get_text(separator=' ', strip=True)
        return text
    else:
        return "Failed to retrieve the webpage"


# Give the value of the sentiment of the text using SentimentIntensityAnalyzer
def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Give the score of the sentiment analysis       
def get_sentiment_score(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    numscore = scores['compound']
    return numscore 


# Return the answer 
def chat_with_bot(input_text):
    sentiment = get_sentiment(input_text)
    score = get_sentiment_score(input_text)
    return f'{sentiment}, Score: {score}'



def collect_input():
    # This function will be called when the button is clicked
    input_value = input_box.get()  
    sentiment = chat_with_bot(input_value)
    output.delete("1.0", tk.END)  
    output.insert(tk.END, sentiment)
    
# Combine the functions of wrapping the text and analyzing it  
def combined_commands():
    url = url_input_box.get()
    page_text = get_page_text(url)
    if page_text.startswith("Error:") or page_text == "Failed to retrieve the webpage":
        output.delete("1.0", tk.END)
        output.insert(tk.END, page_text)
    else:
        input_box.delete(0, tk.END)
        input_box.insert(0, page_text)
        collect_input()  

# initialize the windows
root = tk.Tk()
root.title("sentiment analyzer")
root.geometry("500x400")

# URL Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_input_box = tk.Entry(root, width=50)
url_input_box.pack(padx=5, pady=5)

# collect to the user the text to analyze
input_label = tk.Label(root, text="text analyzed:")
input_label.pack()
input_box = tk.Text(root, height=2, width=50)
input_box.pack(padx=5, pady=5)

# Analyze Button
get_input_button = tk.Button(root, text='Analyze', width=50, command=combined_commands)
get_input_button.pack(pady=5)


# Show the result
output = tk.Text(root, height=2, width=50)
output.pack()


root.mainloop()




import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk

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

# initialize the windows
root = tk.Tk()
root.title("sentiment analyzer")
root.geometry("500x400")

# collect to the user the text to analyze
input_box = tk.Entry(root, width=50)
input_box.pack(padx=5, pady=5)
get_input_button = tk.Button(root, text='Analyze', width=50, command=collect_input)
get_input_button.pack(pady=5)

# Show the result
output = tk.Text(root, height=2, width=50)
output.pack()


root.mainloop()


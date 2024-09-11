import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import font

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
    input_value = input_box.get("1.0", tk.END).strip()  
    sentiment = chat_with_bot(input_value)
    output.delete("1.0", tk.END)  
    output.insert(tk.END, sentiment)

# initialize the windows
root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("800x600")
root.configure(bg="#7D6161")

#a custom font for the widgets
custom_font = font.Font(family="Helvetica", size=12)

#a frame for the input box and button
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

#a label for instructions
input_label = tk.Label(input_frame, text="Enter text to analyze:", bg="#f0f0f0", font=custom_font)
input_label.pack(anchor="w")

# Input box
input_box = tk.Text(input_frame, height=10, width=60, font=custom_font, bd=2, relief="solid", wrap="word")
input_box.pack(padx=5, pady=5)

# Analyze Button 
get_input_button = tk.Button(root, text='Analyze', width=20, font=custom_font, bg="#4CAF50", fg="white", activebackground="#45a049", bd=2, relief="raised", command=collect_input)
get_input_button.pack(pady=10)

# Frame for the output
output_frame = tk.Frame(root, bg="#f0f0f0")
output_frame.pack(pady=10)

# Output box label
output_label = tk.Label(output_frame, text="Sentiment Result:", bg="#f0f0f0", font=custom_font)
output_label.pack(anchor="w")

# Output Text
output = tk.Text(output_frame, height=2, width=50, font=custom_font, bd=2, relief="solid", wrap="word")
output.pack()

root.mainloop()


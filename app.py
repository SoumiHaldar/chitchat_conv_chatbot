from flask import Flask,render_template,request
import requests
import openai
import json
from dotenv import load_dotenv
load_dotenv()


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        user_input = request.form['user_input']
        print(user_input)
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=f"Please check the following text if it is a chitchat conversation:\n{user_input}",
            max_tokens=256,
            temperature=0
        )
        correct_sentence=response.choices[0].text
        return render_template('index.html',correct_sentence=correct_sentence)
    return render_template('index.html')

    
if __name__=='__main__':
    app.run(debug=True)
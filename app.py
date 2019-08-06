# python -m spacy download en_core_web_sm 
import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load('en_core_web_sm')
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/find_names', methods=['POST'])
def find_names():
	if request.method == 'POST':
		news = request.form['news']
		article = nlp(news)
		person = ' '.join([str(X) for X in article if X.ent_type_=='PERSON'])
	return render_template('result.html', person=person)


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
import pickle
import spacy
from scispacy.abbreviation import AbbreviationDetector

model = pickle.load(open('model1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get("text")
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("abbreviation_detector")
    doc = nlp(text)
    dict ={}
    for abrv in doc._.abbreviations:
        dict[f'{abrv}']=f'{abrv._.long_form}'
        # print(f"{abrv} \t ({abrv.start}, {abrv.end}) {abrv._.long_form}")
    return jsonify(dict)


if __name__ == "__main__":
    app.run(debug=True)

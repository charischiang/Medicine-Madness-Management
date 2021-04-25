import os
from flask import Flask, render_template, request
import numpy as np

try:
    from PIL import Image
except ImportError:
    import Image
    
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_core(filename,mode=3):
    text = pytesseract.image_to_string(Image.open(filename),config=f'--psm {mode}')
    return text

def fetch_instruction(text):
    for i in text.split('\n'):
        if "take" in i.lower():
            return i.split(".")[0].lower()
    return ""
def count_digits_percent(string):
    if not string:
        return 1
    return sum([char in "0123456789" for char in string])/len(string)

import json

with open('medicine_dict.json') as f:
    medicine_dict = json.load(f)

from scipy import spatial
def similarity(vector1,vector2):
    vector1=np.asarray(vector1, dtype='float64')
    vector2=np.asarray(vector2, dtype='float64')
    return 1 - spatial.distance.cosine(vector1, vector2)
def alphabet_vec(string):
    string=string.lower()
    vector=[]
    count_dict={}
    for i in string:
        if not count_dict.get(i,False):
            count_dict[i]=1
        else:
            count_dict[i]+=1
    for i in "abcdefghijklmnopqrstuvwxyz":
        vector.append(count_dict.get(i,0))
    return vector

import fasttext.util
#fasttext.util.download_model('en', if_exists='ignore')  # English
print("DONE")
ft = fasttext.load_model('cc.en.300.bin')



UPLOAD_FOLDER = '/static/uploads/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')
        if file and allowed_file(file.filename):
            test_sentence=ocr_core(file,3).split('\n')
            sentences=[]
            for i in test_sentence:
                if count_digits_percent(i)<0.3:
                    sentences.append(i)
            max_similarity=-1
            best_match=None
            for i in sentences:
                curr_vector=ft.get_word_vector(i.lower())
                curr_alpha_vector=alphabet_vec(i)
                for j in medicine_dict:
                    medicine_vector=medicine_dict[j]
                    medicine_alpha_vector=alphabet_vec(j)
                    curr_similarity=similarity(curr_vector,medicine_vector)+similarity(curr_alpha_vector,medicine_alpha_vector)
                    if curr_similarity>max_similarity:
                        max_similarity=curr_similarity
                        best_match=(i,j)
            extracted_text = "Instruction: "+fetch_instruction(ocr_core(file))+"\nMedicine Line Found: "+str(best_match[0])+"\nMedicine in Database: "+str(best_match[1])
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()

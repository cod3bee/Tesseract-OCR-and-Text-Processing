from tkinter import filedialog
from tkinter import *
from PIL import Image
import PIL
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select screenshot of Problem",filetypes = [("png files","*.png *.jpg"),("all files","*.*")])
path=root.filename
location=path.replace('/','\\\\')
root.destroy()
basewidth = 2500
import pytesseract
img=Image.open(location)
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
#filename = 'C:\\Users\\prashantkumar_g\\Desktop\metam.txt'
#file = open(filename, 'rt')
text = pytesseract.image_to_string(img)
#file.close()
sentences = sent_tokenize(text)
for i in range(len(sentences)):
    tokens = word_tokenize(sentences[i])
    tokens = [w.lower() for w in tokens]
    words = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    print(words)
    #print(words)

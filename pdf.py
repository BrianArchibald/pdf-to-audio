from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS

Tk().withdraw()  # not full GUI
filelocation = askopenfilename()  # open diaglog GUI

with open(filelocation, 'rb') as f:
    pdf = pdftotext.PDF(f)

string_of_text = ''
for text in pdf:
    string_of_text += text

final_file = gTTS(text=string_of_text, lang='en')
final_file.save('Generated Speech.mp3')

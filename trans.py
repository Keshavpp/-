# अनुवादक

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
screen = Tk()
screen.title('अनुवादक') #name of calculator
screen.configure(bg = 'gray') #backgroud colour of calc
screen.geometry('500x400')
screen.iconbitmap('logo.ico')

# language directory

langdir = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
# working functions
def func(event=None): #perform translate func.
	try:
		teex = TextBlob(var1.get())
		lan = teex.detect_language()
		lan_to_dic = ddl.get()
		lan2 = langdir[lan_to_dic] 
		teex = teex.translate(from_lang = lan, to=lan2)
		lab3.configure(text=teex)
		var2.set(teex)
	except:
		var2.set('Try another word')

def exit():  #perform exit func.
	ll = messagebox.askyesnocancel('Alert','Do you want to exit the application?',parent=screen)
	if(ll ==True):
		screen.destroy()




## dd list
langs = StringVar()
ddl = Combobox(screen, width=25,textvariable= langs,state = 'readonly' )
ddl['values'] = [j for j in langdir.keys()] 
ddl.current(37)
ddl.place(x=330,y=0)



##making of Entry box
var1 = StringVar()
b1 = Entry(screen,width=25,textvariable = var1, font=('arial',15,'bold'))
b1.place(x=200,y=40)


var2 = StringVar()
b2 = Entry(screen,width=25,textvariable = var2, font=('arial',15,'bold'),relief = 'ridge')
b2.place(x=200,y=100)

### Text Labels
lab1= Label(screen,text = 'Enter Text',font=('arial',15,'bold'),bg='gray')
lab1.place(x=5,y=40)

lab2= Label(screen,text = 'Translated Text',font=('arial',15,'bold'),bg='gray')
lab2.place(x=5,y=100)

lab3= Label(screen,text = ' ',font=('arial',15,'bold'),bg='gray')
lab3.place(x=5,y=250)

#### Buttons
but1 = Button(screen,text='Translate',bd=6, bg='white',activebackground='yellow',width=8,font=('arial',15,'bold'),command=func )
but1.place(x=70,y=170)

but2 = Button(screen,text='Exit',bd=6, bg='white',activebackground='yellow',width=8,font=('arial',15,'bold'),command=exit)
but2.place(x=280,y=170)
screen.bind('<Return>',func)




screen.mainloop()
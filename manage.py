from flask import Flask ,render_template
from textblob import TextBlob
from gensim.summarization import summarize
from flask import request
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup


app = Flask(__name__)
def summarizemethod(content):
    stext=summarize(content,split=True)
    return stext

#var1=summarize(mytext,split=True)


@app.route('/',methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

@app.route('/text',methods=['GET', 'POST'])
def text():
    
    #var1=request.form['message']
    #return render_template('about.html',username=var1)
    content=request.form['mes']
    content='"""'+content+'"""'
    ln1=len(content)
    stext=summarize(content,split=True)
    ln2=len(str(stext))
    word=TextBlob(str(stext))
    f=word.translate(from_lang='en', to ='hi')
    
    #     p=str(f.filename)
    #     f.save(f.filename) 
    #     with open(p, "r") as fl:
    #         content1= fl.read()
    #         #content='"""'+content+'"""'
    #         #stext=summarize(content,split=True)
            
    #     if os.path.exists(p):
    #         os.remove(p)
    # #if request.form.get['link']:
     #   sitelink=request.form.get['link']
     #   htmlc = urlopen(sitelink).read().decode('utf-8')
     #   soup = BeautifulSoup(htmlc, 'lxml')
     #   content=soup.findAll('p')
     #   content=summarize(content,split=True)
    return render_template('about.html',username=stext,hindi=f,length1=ln1,length2=ln2)
@app.route('/about',methods=['GET', 'POST'])
def about():
    
    
    # f = request.files['txt']  
    # p=str(f.filename)
    # f.save(f.filename) 
    # with open(p, "r") as fl:
    #     content= fl.read()
    #     content='"""'+content+'"""'
    #     stext=summarize(content,split=True)
            
    # if os.path.exists(p):
    #     os.remove(p)
    content=request.form['message']
    content='"""'+content+'"""'
    stext=summarize(content,split=True)

    # url=request.form['link']
    # htmlc = urlopen(url).read().decode('utf-8')
    # soup = BeautifulSoup(htmlc, 'lxml')
    # content=soup.findAll('p')
    # content='"""'+content+'"""'
    # stext=summarize(content,split=True)


    # word=TextBlob(str(stext))
    # f=word.translate(from_lang='en', to ='hi')
    
    #summarizetext=summarizemethod(content)
    #summarize(mytext,ratio=0.2)
    
    
    return render_template('about.html',username=stext)
#@app.route('/query')
#def summarize():
    

  #  return render_template('about.html',name1=var1)
@app.route('/lnk',methods=['GET', 'POST'])
def lnk():
    
    
    url=str(request.form['web'])
    htmlc = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup("htmlc", "lxml")
    content=str(soup.findAll('p', {'id': 'a'}))
    # content='"""'+content+'"""'
    # stext=summarize(content,split=True)
        
    
    #summarizetext=summarizemethod(content)
    
    
    
    return render_template('about.html',username=content)
@app.route('/file',methods=['GET', 'POST'])
def file():
    
    
    f = request.files['txt']  
    p=str(f.filename)
    f.save(f.filename) 
    with open(p, "r") as fl:
        content= fl.read()
        content='"""'+content+'"""'
        ln1=len(content)
        stext=summarize(content,split=True)
        ln2=len(str(stext))
    if os.path.exists(p):
         os.remove(p)
    
        
    wrd=TextBlob(str(stext))
    f=wrd.translate(from_lang='en', to ='hi')  
    #summarizetext=summarizemethod(content)
    
    
    
    return render_template('about.html',username=stext,hindi=f,length1=ln1,length2=ln2)
@app.route('/ats',methods=['GET', 'POST'])
def ats():
    
    return render_template('ats.html')
@app.route('/new',methods=['GET', 'POST'])
def new():
    
    return render_template('new.html')


app.run()

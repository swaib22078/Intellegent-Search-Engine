from flask import Flask,render_template,request,url_for,redirect
import json
from function import url, text_extract, filter_2000, preprocess_dict, frequency, text_summary,Rank,summary
from evaluation import score
app=Flask(__name__)
def get_summary(q):

    link = url(q)
    text = text_extract(link)
    filter = filter_2000(text)
    dic = preprocess_dict(filter)
    fre = frequency(dic)
    fin_summary = text_summary(dic, fre)
    # res=summary(text)
    result=Rank(fin_summary,q)
    ans=score(text,result)
    
    #result = {(link,): summary}
    #len(summary)
    return ans
@app.route("/",methods=["GET","POST"])
def index():
 if request.method == "POST":
    query=request.form['q']
    return redirect(url_for('summary', query=query))
 else:
      return render_template('index.html')
  
@app.route('/summary/<query>',methods=["GET","POST"])
def summary(query):
    data=get_summary(query)
    return render_template('result.html', query=query,data=data)  

if __name__ == '__main__':
    app.run(debug=True,port=4000)  
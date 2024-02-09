import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("wqi.pkl","rb")
classifier=pickle.load(pickle_in)
p1 = open("temp.pkl","rb")
c1=pickle.load(p1)
p2 = open("do.pkl","rb")
c2=pickle.load(p2)
p3 = open("ph.pkl","rb")
c3=pickle.load(p3)
p4 = open("con.pkl","rb")
c4=pickle.load(p4)
p5 = open("bod.pkl","rb")
c5=pickle.load(p5)
p6 = open("nit.pkl","rb")
c6 =pickle.load(p6)
p7 = open("fec.pkl","rb")
c7 =pickle.load(p7)
p8 = open("tot.pkl","rb")
c8 =pickle.load(p8)

#with open('style.css') as f :
   #   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def welcome():
    return "Welcome All"

def temp(year):
     
    prediction=c1.predict([[year]])
    print(prediction)
    return prediction

def dox(year,temp):
     
    prediction=c2.predict([[year,temp]])
    print(prediction)
    return prediction

def pH(year,temp,do):
     
    prediction=c3.predict([[year,temp,do]])
    print(prediction)
    return prediction

def cond(year,temp,do,ph):
     
    prediction=c4.predict([[year,temp,do,ph]])
    print(prediction)
    return prediction
  
def biod(year,temp,do,ph,con):
     
    prediction=c5.predict([[year,temp,do,ph,con]])
    print(prediction)
    return prediction

def nitr(year,temp,do,ph,con,bod):
     
    prediction=c6.predict([[year,temp,do,ph,con,bod]])
    print(prediction)
    return prediction
  
def fecoli(year,temp,do,ph,con,bod,nit):
     
    prediction=c7.predict([[year,temp,do,ph,con,bod,nit]])
    print(prediction)
    return prediction  

def total(year,temp,do,ph,con,bod,nit,fec):
     
    prediction=c8.predict([[year,temp,do,ph,con,bod,nit,fec]])
    print(prediction)
    return prediction 

def wqix(year,temp,do,ph,con,bod,n,fec,tot):
     
    prediction=classifier.predict([[year,temp,do,ph,con,bod,n,fec,tot]])
    print(prediction)
    return prediction 
def main():
    html_temp = """
    <div style="background-color:skyblue;padding:10px;border-radius:5px">
    <h2 style="color:darkblue;text-align:center;font-family:Callibri;"><b>Tamil Nadu River Water Quality Prediction</b></h2>
    </div>
    <br></br>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    year = st.number_input("Year",step=1,min_value=2023,value=2023)
    #temp min - 24
    #temp = 30
    # do min - 5
    #do = 7.5
    #ph min - 6.8
    #ph = 8.5
    #con min - 435
    #con = 2800
    #bod min - 1.65
    #bod = 20
    #n min - 0.1
    #n = 2
    #fc min- 5000
    #fc = 3600000
    #tc min - 7800
    #tc = 8400000
    result=""
    if st.button("Predict"):
        tem = temp(year)
        do = dox(year,tem[0])
        ph = pH(year,tem[0],do[0])
        con = cond(year,tem[0],do[0],ph[0])
        bod= biod(year,tem[0],do[0],ph[0],con[0])
        nit = nitr(year,tem[0],do[0],ph[0],con[0],bod[0])
        fec = fecoli(year,tem[0],do[0],ph[0],con[0],bod[0],nit[0])
        tot = total(year,tem[0],do[0],ph[0],con[0],bod[0],nit[0],fec[0])
        c1,c2,c3 = st.columns(3)
        c1.write("**Physical Parameters :**")
        c2.text_area(label="Temperature", value="{:.2f}".format(tem[0]))
        c3.text_area(label="Conductivity", value="{:.2f}".format(con[0]))
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("**Chemical Parameters :**")
        c2.text_area(label="Dissolved Oxygen", value="{:.2f}".format(do[0]))
        c3.text_area(label="pH", value="{:.2f}".format(ph[0]))
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("")
        c1.write("**Biological Parameters :**")
        c2.text_area(label="Bio-chemical Oxygen Demand", value="{:.2f}".format(bod[0]))
        c3.text_area(label="Nitrate", value="{:.2f}".format(nit[0]))
        c2.text_area(label="Fecal Coliform", value="{:.2f}".format(fec[0]))
        c3.text_area(label="Total Coliform", value="{:.2f}".format(tot[0]))
        result = wqix(year,tem[0],do[0],ph[0],con[0],bod[0],nit[0],fec[0],tot[0])
        st.success('**The Water Quality Index of the river is {:.2f}.**'.format(result[0]))
        
        if result <= 25 :
          st.success('**The quality of the water is excellent**')  
          image = Image.open('Excellent.jpg')
          st.image(image, caption='Excellent')
        elif result >= 25 and result <= 50:
          st.success('**The quality of the water is good**')  
          image = Image.open('Good.jpg')
          st.image(image, caption='Good')
        elif result >= 50 and result <= 75:
          st.success('**The quality of the water is poor**')
          image = Image.open('Poor.jpg')
          st.image(image, caption='Poor')
        else:
          st.success('**The quality of the water is very poor**')
          image = Image.open('Very Poor.jpg')
          st.image(image, caption='Very Poor')

if __name__=='__main__':
    main()
    

import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 
import json
from streamlit_lottie import st_lottie
import requests
from streamlit.components.v1 import iframe

import pandas as pd
import numpy as np

#utils
import os
import joblib

#data viz pkgs
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath : str):
    with open(filepath,'r') as f:
        return json.load(f)




#Database
import sqlite3
conn=sqlite3.connect('user_data.db')
c=conn.cursor()



# Heading template
import streamlit as st


# Heading template
heading_html = """
    <div style="background-color:#F08080;padding:20px;border-radius:10px;">
        <h1 style="color:white;text-align:center;font-family: 'Montserrat', sans-serif;">Multiple Disease Predictor</h1>
        <h3 style="color:#FFD700;text-align:center;font-family: 'Amiri', serif;">D'predicto</h3>
    </div>
"""
st.markdown(heading_html, unsafe_allow_html=True)
image_html = """
    <div style="display:flex;justify-content:center;">
        <img src="https://image.freepik.com/free-vector/medical-appointment-concept-illustration_114360-621.jpg" 
        alt="doctor illustration" style="width:50%;height:50%;margin:20px;">
        <img src="https://image.freepik.com/free-vector/medical-appointment-concept-illustration_114360-623.jpg" 
        alt="doctor illustration" style="width:50%;height:50%;margin:20px;">
        
    </div>
"""

what_to_do_temp = """
    <div style="background-color:#E6FFE6;padding:20px;border-radius:10px;">
        <h3 style="text-align:center;">What should I do?</h3>
        <ul>
            <li><span style="color:#008000">&#10148;</span> Get prediction for desease</li>
            <li><span style="color:#008000">&#10148;</span> Get the prediction for diabetes, heart disease, and Parkinson's disease</li>
            <li><span style="color:#008000">&#10148;</span> Get a list of doctors for the predicted disease</li>
            <li><span style="color:#008000">&#10148;</span> Book an appointment with the doctor</li>
        </ul>
    </div>
    """
features_html = """
   <div style="background-color:#FFF7E6;padding:20px;border-radius:10px;">
    <h3 style="text-align:center;">Features</h3>
    <ul>
        <li><span style="color:#FFA500">&#10148;</span> Multiple disease prediction</li>
        <li><span style="color:#FFA500">&#10148;</span> Prediction for diabetes, heart disease, and Parkinson's disease</li>
        <li><span style="color:#FFA500">&#10148;</span> List of doctors for the predicted disease</li>
        <li><span style="color:#FFA500">&#10148;</span> Option to book an appointment with the doctor</li>
        <li><span style="color:#FFA500">&#10148;</span> Chatbot for guidance</li>
    </ul>
</div>
"""



prescriptive_message_temp = """
    <div style="background-color: #f7d794; border-radius: 5px; margin: 10px; padding: 20px;">
        <h3 style="text-align: justify; color: #1d3557; font-family: Arial, sans-serif;">Recommended Lifestyle Modifications</h3>
        <ul style="list-style-type: square; color: #1d3557; font-family: Arial, sans-serif; margin-top: 10px; margin-left: 20px;">
            <li>specialized doctors:</li>
            <li>Dr shubham murtadak  sm speciality hospital (cont:9322191339)</li>
            <li>Dr shubham murtadak  sm speciality hospital (cont:9322191339)</li>
            <li>Dr shubham murtadak  sm speciality hospital (cont:9322191339)</li>
            <li>Dr shubham murtadak  sm speciality hospital (cont:9322191339)</li>
        </ul>
        <h3 style="text-align: justify; color: #1d3557; font-family: Arial, sans-serif; margin-top: 20px;">Medical Management</h3>
        <ul style="list-style-type: square; color: #1d3557; font-family: Arial, sans-serif; margin-top: 10px; margin-left: 20px;">
            <li>Consult your doctor regularly</li>
            <li>Take your medications as prescribed</li>
            <li>Follow-up with your healthcare provider</li>
        </ul>
    </div>
"""
    
descriptive_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Definition</h3>
		<p>Hepatitis B is a viral infection that attacks the liver and can cause both acute and chronic disease.</p>
	</div>
	"""

#loading save model

diabetes_model=pickle.load(open('diabeties_model.sav','rb'))
heart_disease_model=pickle.load(open('heart_disease_model.sav','rb'))
perkinsons_model=pickle.load(open('perkinsons_model.sav','rb'))



def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES (?,?)',(username,password))
    conn.commit()
def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password = ?',(username,password))
    data=c.fetchall()
    return data
def main():
    """Multiple Diesease Prediction APP """
    #st.title("Multiple Diesease Predictor")
    #st.markdown(heading_html.format('royalblue'),unsafe_allow_html=True)
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home",'Login/Signup', 'Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction','Settings'], 
            icons=['house','person','activity','heart','person', 'gear'], menu_icon="cast", default_index=0)
    
    
    if selected=='Home':
        title, title_ani = st.columns([3,1])

        with title:
            st.title("Welcome To :blue[D'Predicto] ")
            st.text("")
            st.text("")
            st.markdown("*Empowering early disease detection and personalized prevention with our advanced Disease Prediction System*")


        wel_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_zpjfsp1e.json")
        #wel_lottie = load_lottiefile(r'C:\Users\DELL\Downloads\Generic.json')
        with title_ani :
            st_lottie(
                wel_lottie,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium",
                height = None,
                width = None,
                key = None,
            )

        st.text("")
        st.text("")
        st.subheader("Our Offerings")

        st.text("")
        st.text("")

        prediction, AptBk, Assis = st.columns(3)

        pred = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_gkgqj2yq.json")
        apt = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_hYRKYxxvdX.json")
        bot = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_g7zx4ni5.json")

        with prediction:
            st_lottie(
                pred,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium",
                height = 220
                )
        prediction.markdown('<h4 style = "text-align: center">Prediction System ', unsafe_allow_html = True)

        with AptBk:
            st_lottie(
                apt,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium"
                )
        AptBk.markdown('<h4 style = "text-align: center">Appointment Booking ', unsafe_allow_html = True)

        with Assis:
            st_lottie(
                bot,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium"
                )
        Assis.markdown('<h4 style = "text-align: center">Assistance', unsafe_allow_html = True)



        st.text('')
        st.text("")
        st.text("")

        st.subheader("Disease :red[Predicion]")
        st.text("")

        diab, heart, park = st.columns(3)

        dimg = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tbjuenb2.json")
        with diab:
            st.text("")
            st.text("")
            st.text("")
            st_lottie(
                dimg,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium"
                )
            st.text("")
            st.text("")
            st.text("")


        diab.markdown('<h4 style = "text-align: center">Diabetes', unsafe_allow_html = True)


        himg = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_a3ntzciy.json")
        with heart:
            st_lottie(
                himg,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium"
                )
        heart.markdown('<h4 style = "text-align: center">Heart Disease', unsafe_allow_html = True)

        pimg = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_9NxFrGo71i.json")
        with park:
            st_lottie(
                pimg,
                speed = 1,
                reverse = False,
                loop = True,
                quality = "medium"
                )

        park.markdown('<h4 style = "text-align: center">Parkinson Disease', unsafe_allow_html = True)


       
        
        #st.markdown(image_html, unsafe_allow_html=True)
        st.markdown(what_to_do_temp, unsafe_allow_html=True)
        st.markdown(features_html, unsafe_allow_html=True)
        chatbot_url = 'http://127.0.0.1:5000/'

        chatbot_visible = False

        if st.button('Chat with our assistant '):
        # Toggle the chatbot visibility when the button is clicked
            chatbot_visible = not chatbot_visible

# Show the chatbot iframe if chatbot_visible is True
        if chatbot_visible:
            st.write('## Chatbot')
            iframe(chatbot_url, width=500, height=600)
        
    elif selected=='Login/Signup':
         st.subheader('Login /Signup')
         menu=["select","Login","Signup"]
         choice=st.selectbox("Login/Signup",menu)
         if choice=='Login':
              st.subheader('Login Selection')
              username=st.text_input('User Name')
              password=st.text_input("Password",type='password')
              if st.checkbox('Login'):
                  create_usertable()
                  result=login_user(username, password)
                  if result:
                      st.success("Welcome {}".format(username))
         elif choice=='Signup':
             st.subheader('Create New Account')
             
             new_user=st.text_input('Username')
             new_password=st.text_input('Password',type='password')
             confirm_password=st.text_input('Confirm Password',type='password')
             
             if new_password==confirm_password:
                 st.success('Password Confirmed')
             else:
                 st.warning('Password Not Match !')
                 
             if st.button('Submit'):
                 create_usertable()
                 add_userdata(new_user, new_password)
                 st.success('You have successfully created a new Account')
                 st.info('Login to Get Started')
                 
                 
    elif (selected =='Diabetes Prediction'):
        #page title 
        st.title('Diabetes Predictor')
        
        #making input coloumn wise
        col1,col2,col3=st.columns(3)
        
        with col1:
            Pregnancies=st.text_input('Number of Pregnancies')
        with col2:
            Glucose=st.text_input('Glucose level')
        with col3:
            BloodPressure=st.text_input('BLoodpressure value')
        with col1:
            SkinThickness=st.text_input('SkinThickness value')
        with col2:
            Insulin=st.text_input('Insulin level')
        with col3:
            BMI=st.text_input('BMI VALUE')
        with col1:
            DibetesPedigreeFunction=st.text_input('Dibetes Pedigree Function value')
        with col2:
            Age=st.text_input('AGE of the person')
            
        diabetes_diagnosis=''
        if st.button('Diabetes Test Result'):
            diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DibetesPedigreeFunction,Age]])
            
            if(diab_prediction[0]==1):
                st.subheader(':red[The person is Diabetic]')
                st.subheader("Prescriptive Analytics")
                st.markdown(prescriptive_message_temp,unsafe_allow_html=True)

                
            else:
                st.info('The person is not Diabetic')
        
        
    elif(selected =='Heart Disease Prediction'):
        st.title('Heart Disease Predictor ')
        #taking input colwise
        col1,col2,col3=st.columns(3)
        
        #age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal 
        
        with col1:
            age=st.number_input('Age',7,100)
        with col2:
            sex=st.number_input('Sex 1-male,0-female',0,1)
        with col3:
            cp=st.number_input('cp')
        with col1:
            trestbps=st.number_input('trestbps')
        with col2:
            chol=st.number_input('chol')
        with col3:
            fbs=st.number_input('fbs')
        with col1:
            restecg=st.number_input('restecg')
        with col2:
            thalach=st.number_input('thalach')
        with col3:
            exang=st.number_input('exang')
        with col1:
            oldpeak=st.number_input('oldpeak')
        with col2:
            slope=st.number_input('slope')
        with col3:
            ca=st.number_input('ca')
        with col1:
            thal=st.number_input('thal')
            
        heart_diagnosis=''
         
         #creating a butoon for prediction
         
        if st.button('Heart_Diesease Test Result'):
             heart_prediction=heart_disease_model.predict([[age,sex, cp,  trestbps , chol,  fbs , restecg , thalach , exang,  oldpeak,  slope , ca , thal ]])
             
             if(heart_prediction[0]==1):
                 
                 st.subheader(':red[The person is Heart Dieseas patient]')
                 st.markdown(prescriptive_message_temp,unsafe_allow_html=True)
                 
             else:
                 st.subheader(':green[The person is not Heart Dieseas patient]')
        
        
        
        
    elif(selected =='Parkinsons Prediction'):
        
        st.title('Parkinsons Predictor ')
        
        #taking input colwise
        col1,col2,col3,col4,col5=st.columns(5)
        
        
      
        
        with col1:
            MDVPFo=st.text_input('MDVP:Fo(Hz)')
        with col2:
            MDVPFh=st.text_input('MDVP:Fhi(Hz)')
        with col3:
            MDVPFl=st.text_input('MDVP:Flo(Hz)')
        with col4:
            MDVPJ1=st.text_input('MDVP:Jitter(%)')
        with col5:
            MDVPJ2=st.text_input('MDVP:Jitter(Abs)')
        with col1:
            MDVPRAP=st.text_input('MDVP:RAP')
        with col2:
            MDVPPPQ=st.text_input('MDVP:PPQ')
        with col3:
            JitterDDP=st.text_input('Jitter:DDP')
        with col4:
            MDVPShimmer=st.text_input('MDVP:Shimmer')
        with col5:
            MDVPShimmer2=st.text_input('MDVP:Shimmer(dB)')
        with col1:
            ShimmerAPQ3=st.text_input('Shimmer:APQ3')
        with col2:
            ShimmerAPQ5=st.text_input('Shimmer:APQ5')
        with col3:
            MDVPAPQ=st.text_input('MDVP:APQ')
        with col4:
            ShimmerDDA=st.text_input('Shimmer:DDA')
        with col5:
            NHR=st.text_input('NHR')   
        with col1:
            HNR=st.text_input('HNR')
        with col2:
            RPDE=st.text_input('RPDE')
        with col3:
            D2=st.text_input('D2')
        with col4:
            DFA=st.text_input('DFA')
        with col5:
            spread1=st.text_input('spread1')
        with col1:
            spread2=st.text_input('spread2')
        with col2:
            PPE=st.text_input('PPE')
        perkinsons_diagnosis=''
          
          #creating a butoon for prediction
          
        if st.button('Perkinsons_Diesease Test Result'):
              perkinsons_prediction=perkinsons_model.predict([[MDVPFo, MDVPFh, MDVPFl, MDVPJ1, MDVPJ2,MDVPRAP,MDVPPPQ, MDVPPPQ,JitterDDP,MDVPShimmer, MDVPShimmer2,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR, HNR,RPDE,D2,DFA,spread1,spread2,PPE]])
              
              if(perkinsons_prediction[0]==1):
                  st.subheader(':red[The person is Perkinsons Dieseas patient]')
                  st.markdown(prescriptive_message_temp,unsafe_allow_html=True)
                  
              else:
                  st.subheader(':green[The person is not Parkinsons Dieseas patient]')
                  
       
        
         
         
                 
            
             








if __name__ == '__main__' :
    main()

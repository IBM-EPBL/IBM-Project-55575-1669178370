import pyrebase

def submit(name,email_id,phone_number,message):
   firebaseconfig={
    'apiKey': "AIzaSyATsq89CuDuLCt7ccZSTZs11sHO3OR7PAc",
  'authDomain': "tdlh-banking-feedback.firebaseapp.com",
    "databaseURL":"https://tdlh-banking-feedback-default-rtdb.firebaseio.com",
  'projectId': "tdlh-banking-feedback",
  'storageBucket': "tdlh-banking-feedback.appspot.com",
  'messagingSenderId': "336462584761",
  'appId': "1:336462584761:web:0a185c120d1fb303fe7468",
  'measurementId': "G-8F8FJRHXCK",
  "serviceAccount": "Key/key.json"
    }
   firebase=pyrebase.initialize_app(firebaseconfig)
   #auth=firebase.auth()
   db=firebase.database()
   feedback={'Name': name,'Phone Number': phone_number,'Email Id':email_id,'Feedback': message}
   db.push(feedback)


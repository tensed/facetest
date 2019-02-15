from django.shortcuts import render
from django.http import HttpResponse

import pyrebase

config = {
    'apiKey': "AIzaSyAEnPq4nHc_jxd4-j-x5AZR7gOUk6PKa8g",
    'authDomain': "facetest-7038e.firebaseapp.com",
    'databaseURL': "https://facetest-7038e.firebaseio.com",
    'projectId': "facetest-7038e",
    'storageBucket': "",
    'messagingSenderId': "349782289538"

}

firebase=pyrebase.initialize_app(config)

auth=firebase.auth()


def home(request):
    return  render(request,'login/home.html')

def login(request):
    return render(request,'login/login.html')

def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('pass')

    user = auth.sign_in_with_email_and_password(email, password)
    return render(request,'login/welcomepage.html')

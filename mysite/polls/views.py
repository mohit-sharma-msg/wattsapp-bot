from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.models import whatsappdb
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pywhatkit
from .forms import *
from twilio.rest import Client
from django.contrib import messages


# # Your Account SID from twilio.com/console
account_sid = ""
# # Your Auth Token from twilio.com/console
auth_token  = ""



# Create your views here.
def home(request):
    return render(request,'index.html')

def whatsapp(request):
    if request.method == 'POST':
        # name = request.GET['name']
        contact_number = request.POST['contact']
        # pdf_file = request.FILES['pdf']
        pdf_url = request.POST['pdf_url']
        # image = request.GET['image']
        # https://53b7-2401-4900-5acd-aadb-d51b-880d-1d15-7db.in.ngrok.io 

        detail = whatsappdb(contact=contact_number)
        detail.save()
        client = Client(account_sid, auth_token)
        
        message = client.messages \
                        .create(
                            body="Hii bro, always keep smile.",
                            media_url= pdf_url,
                            # find your virtual number from twilio
                            from_='whatsapp:',
                            to= 'whatsapp:{}'.format(contact_number)
                        )

        print(message.sid)
        
        return render(request,'index.html',{'text':"Message Send Successfully"})
    else:
    	messages.error(request, 'Files was not Submitted successfully!')
    	
    
    

from django.shortcuts import render

from opentok import OpenTok

opentok = OpenTok('45599482', 'ffede0e7ae95c1f8ae85cd154e9a5316a3ea2f92')
session = opentok.create_session()

# Create your views here.

def hello(request):
	key = '45599482'
	session_id = session.session_id
	token = opentok.generate_token(session_id)
	return render(request, 'hello.html' , { 'apikey' : key , 'session_id' :session_id , 'token' :token })


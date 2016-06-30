from django.shortcuts import render

from opentok import OpenTok

APIKey = '45615332'
secretkey = '67beb3b3f754ff681189f40258d81352ed8b1f10'
opentok = OpenTok(APIKey, secretkey)
session = opentok.create_session()


def session_view(request):
    session_id = session.session_id
    token = opentok.generate_token(session_id)
    context = {
        'apikey': APIKey,
        'session_id': session_id,
        'token': token,
    }
    return render(request, 'sessionScreen.html', context)

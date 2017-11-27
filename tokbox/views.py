from django.shortcuts import render

from opentok import OpenTok

APIKey = 'API_KEY'
secretkey = 'SECRET_KEY'
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

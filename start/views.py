from django.shortcuts import render

def index(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '01_index.html', {'username': username, })

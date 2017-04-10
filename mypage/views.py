from django.shortcuts import render

# Create your views here.

def mypage(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, 'undercons.html', {'username': username, })

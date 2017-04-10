from django.shortcuts import render

def counsel050101(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '05_counsel0101.html', {'username':username, })

def counsel050102(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '05_counsel0102.html', {'username':username, })

def counsel050201(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '05_counsel0201.html', {'username':username, })

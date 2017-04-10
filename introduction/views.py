from django.shortcuts import render

def company0201(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '02_company01.html', {'username': username, })

def company0202(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '02_company02.html', {'username': username, })

def company0203(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '02_company03.html', {'username': username, })

def company0204(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '02_company04.html', {'username': username, })
from django.shortcuts import render

def finance0301(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance01.html', {'username': username, })

def finance0302(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance02.html', {'username': username, })

def finance030301(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0301.html', {'username': username, })

def finance030302(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0302.html', {'username': username, })

def finance030303(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0303.html', {'username': username, })

def finance030304(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0304.html', {'username': username, })

def finance030305(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0305.html', {'username': username, })

def finance030306(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0306.html', {'username': username, })

def finance030401(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0401.html', {'username': username, })

def finance030501(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0501.html', {'username': username, })

def finance030502(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '03_finance0502.html', {'username': username, })
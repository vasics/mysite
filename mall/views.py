from django.shortcuts import render

def mall0601(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, 'undercons.html', {'username':username, })

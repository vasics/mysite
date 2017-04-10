from django.shortcuts import render
from django.contrib.auth.models import User


def choice(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '01_member_choice.html', {'username': username, })

def login_form(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '08_login_home.html', {'username': username, })

def check(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username =username)

            if user.check_password(password):
                request.session["username"] = username
                return render(request, '01_index.html', {'username': username, })
            else:
                status = "비밀번호가 틀려습니다."
                return render(request, '08_login_home.html', {'status': status, })
        except User.DoesNotExist:
            status = "존대하지 않는 아이디입니다."
            return render(request, '08_login_home.html', {'status': status, })


def terms(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '01_member_terms.html', {'username': username, })

def register(request):
    return render(request, '01_member_register.html')

def success(request):
    return render(request, '01_member_success.html')

def logout(request):
    username = request.session['username']
    return render(request, '08_logout_home.html', {'username': username, })

def logout_process(request):
    request.session['username'] = None

    return render(request, '01_index.html')
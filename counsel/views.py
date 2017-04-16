from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from counsel.models import Counsel01, Counsel02
from counsel.forms import Counsel01Form, Counsel02Form

def counsel050101(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    counsel_list = Counsel01.objects.all().order_by('-created_at')

    paginator = Paginator(counsel_list, 5)

    page = request.GET.get('page', 1)
    try:
        counsel = paginator.page(page)
    except PageNotAnInteger:
        counsel = paginator.page(1)
    except EmptyPage:
        counsel = paginator.page(paginator.num_pages)

    return render(request, '05_counsel0101.html', {'username':username, 'counsel': counsel, })

@csrf_exempt

def c01_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None
    form = Counsel01Form()
    if request.method == 'POST':
        form = Counsel01Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.photo = request.FILES["photo"]
            instance.save()
            new = Counsel01.objects.last()
            pk = new.id
            counsel_list = Counsel01.objects.filter(id__lte=pk).order_by('-created_at')
            return render(request, '05_counsel01_detail.html', {'pk': pk, 'counsel_list': counsel_list,
                                                                'username': username, })
        else:
            form = Counsel01Form()
    return render(request, '05_counsel01_write.html', {'form': form, 'username': username, })

def c01_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    specific = Counsel01.objects.filter(id=pk).get()
    counsel_list = Counsel01.objects.filter(id__lte=pk).order_by('-created_at')
    Counsel01.objects.filter(id=pk).update(hits=specific.hits + 1)

    return render(request, '05_counsel01_detail.html', {'counsel_list': counsel_list, 'pk': pk, 'username': username, })

@csrf_exempt

def c01_editpw(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    if request.method == 'POST':
        p1 = request.POST['password']
        p2 = Counsel01.objects.filter(id=pk).get()
        if p1 == p2.password :
            return render(request, '05_counsel01_edit.html', {'username': username, 'p2': p2, 'pk': pk, })
        return render(request, '05_counsel01_auth.html', {'username': username, 'pk': pk, })
    return render(request, '05_counsel01_editpw.html', {'username': username, 'pk': pk, })

def c01_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    p2 = Counsel01.objects.filter(id=pk).get()
    return render(request, '05_counsel01_edit.html', {'username': username, 'p2': p2, 'pk': pk, })

def c01_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    content = request.POST['content']
    title = request.POST['title']
    password = request.POST['password']
    Counsel01.objects.filter(id=pk).update(title=title, content=content, password=password)
    counsel_list = Counsel01.objects.filter(id__lte=pk).order_by('-created_at')

    return render(request, '05_counsel01_detail.html', {'username': username, 'counsel_list': counsel_list,
                                                        'pk': pk, })

def c01_auth(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '05_counsel01_auth.html', {'username': username, 'pk': pk, })

@csrf_exempt

def c01_deletepw(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    if request.method == 'POST':
        p1 = request.POST['password']
        p2 = Counsel01.objects.filter(id=pk).get()
        if p1 == p2.password :
            return render(request, '05_counsel01_delete.html', {'username': username, 'pk': pk, })
        return render(request, '05_counsel01_auth.html', {'username': username, 'pk': pk, })
    return render(request, '05_counsel01_deletepw.html', {'username': username, 'pk': pk, })

def c01_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    return render(request, '05_counsel01_delete.html', {'username': username, 'pk': pk, })

def c01_delete_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    d = Counsel01.objects.filter(id=pk).get()
    d.delete()

    return render(request, '05_counsel01_delete_db.html', {'username': username, 'pk': pk, })

@csrf_exempt

def counsel050201(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None
    if request.method == 'POST' :
        if request.POST['agree'] == "no" :
            msg = "동의를 하셔야 신청이 완료됩니다."
            return render(request, '05_counsel0201.html', {'username':username, 'msg':msg, })
        form = Counsel02()
        form.writer = request.POST['writer']
        form.birth = request.POST['birth']
        form.tel = request.POST['tel']
        form.email = request.POST['email']
        form.address = request.POST['address']
        form.job = request.POST['job']
        form.area = request.POST['area']
        form.starttime = request.POST['starttime']
        form.endtime = request.POST['endtime']
        form.fp = request.POST['fp']
        form.content = request.POST['content']
        form.agree = request.POST['agree']
        form.save()
        return redirect('counsel02save')
    return render(request, '05_counsel0201.html', {'username':username, })

@csrf_exempt

def counsel050202(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    specific = Counsel01.objects.filter(id=pk).get()
    fp = specific.fp
    if request.method == 'POST' :
        if request.POST['agree'] == "no" :
            msg = "동의를 하셔야 신청이 완료됩니다."
            return render(request, '05_counsel0201.html', {'username':username, 'msg':msg, })
        form = Counsel02()
        form.writer = request.POST['writer']
        form.birth = request.POST['birth']
        form.tel = request.POST['tel']
        form.email = request.POST['email']
        form.address = request.POST['address']
        form.job = request.POST['job']
        form.area = request.POST['area']
        form.starttime = request.POST['starttime']
        form.endtime = request.POST['endtime']
        form.fp = request.POST['fp']
        form.content = request.POST['content']
        form.agree = request.POST['agree']
        form.save()
        return redirect('counsel02save')
    return render(request, '05_counsel0201.html', {'username':username, 'fp': fp, })

def counsel02save(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None
    return render(request, '05_counsel0201save.html', {'username': username, })

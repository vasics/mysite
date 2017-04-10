from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from counsel.models import Counsel01
from counsel.forms import Counsel01Form

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

    form = Counsel01Form(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            new = Counsel01.objects.last()
            pk = new.id
            return render(request, '05_counsel01_detail.html', {'pk': pk, 'username': username, })
        else:
            form = Counsel01Form()
    return render(request, '05_counsel01_write.html', {'form':form, 'username': username, })

def c01_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    id =pk
    counsel_list = Counsel01.objects.filter(id__lte=id).order_by('-created_at')

    return render(request, '05_counsel01_detail.html', {'counsel_list': counsel_list,
    'pk': pk, 'username': username, })

def counsel050201(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '05_counsel0201.html', {'username':username, })

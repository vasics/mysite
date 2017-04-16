from django.shortcuts import render, render_to_response
from .models import Contacts, Contacts02, Contacts03, Contacts04, Contacts05, Contacts06q
from .models2 import Contacts06a
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from knowledge.forms import ContactsForm, Contacts02Form, Contacts03Form, Contacts04Form, Contacts05Form
from knowledge.forms import Contacts06qForm, Contacts06aForm
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.auth.models import User

def knowledge040101(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    contact_list = Contacts.objects.all().order_by('-created_at')

    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, '04_knowledge01.html', {'contacts': contacts, 'username': username })

@csrf_exempt

def board01_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = ContactsForm
    form = form_class(request.POST or None)

    total = Contacts.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '04_knowledge01_mustlogin.html')
        else:
            if form.is_valid():
                contacts = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                contacts.user_id = write.pk
                contacts.save()

                new = Contacts.objects.last()
                pk = new.id

                total = Contacts.objects.all().count()
                current = Contacts.objects.filter(pk=pk).order_by('created_at').count()
                page = (total - current) // 20 + 1

                return render(request, '04_knowledge01_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = ContactsForm()

    return render(request, '04_knowledge01_write.html', {'form':form, 'username': username, 'page': page, })

def board01_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board01 = Contacts.objects.get(id=pk)
    id = specific_board01.id

    total = Contacts.objects.all().count()
    c_count = Contacts.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    Contacts.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render (request, '04_knowledge01_detail.html', {'specific_board01': specific_board01, 'id': id,
                                                           'username': username, 'page': page, 'c_count': c_count })

@csrf_exempt

def board01_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard01 = Contacts.objects.get(id=pk)

        total = Contacts.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard01.user_id == user.id :
            return render(request, '04_knowledge01_edit.html', {'oldboard01': oldboard01, 'username': username, 'page': page, })
        else:
            return render(request, '04_knowledge01_different.html', {'username': username, })
    return render(request, '04_knowledge01_mustlogin.html', {'username':username, 'page': page, })

def board01_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if len(request.POST['content']) == 0:
        return HttpResponse('내용을 입력해주세요.')

    if len(request.POST['title']) == 0:
        return HttpResponse('제목을 입력해주세요.')

    else:
        content = request.POST['content']
        title = request.POST['title']

        Contacts.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '04_knowledge01_edit_db.html', {'pk': pk, 'username': username, })

def board01_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete01 = Contacts.objects.get(id=pk)
    delete01.delete()
    total = Contacts.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge01_delete.html', {'page': page, 'username': username, })

def search01list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.GET.get('search01') == None:
        return render_to_response('04_knowledge01_noresult.html', {'username': username, })

    searchStr = request.GET.get('search01')
    search01total = Contacts.objects.filter(title__contains=searchStr).count()

    if search01total == None:
        return render(ruquest, '04_knowledge01_noresult.html', {'username': username, })

    contacts = Contacts.objects.filter(title__contains=searchStr).all()
    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    return render_to_response('04_knowledge01_search01list.html', {'contacts': contacts,
        'search01total': search01total, 'searchStr':searchStr, 'username':username, })

def board01_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge01_complete.html', {'username': username, })

def board01_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge01_different.html', {'username': username, 'page': page, })

def board01_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete01 = Contacts.objects.get(id=pk)

        if delete01.user_id == user.id :
            total = Contacts.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge01_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Contacts.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge01_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Contacts.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge01_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

def knowledge040201(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    contact_list = Contacts02.objects.all().order_by('-created_at')

    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, '04_knowledge02.html', {'contacts': contacts, 'username': username })

@csrf_exempt

def board02_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Contacts02Form
    form = form_class(request.POST or None)

    total = Contacts02.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '04_knowledge02_mustlogin.html')
        else:
            if form.is_valid():
                contacts = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                contacts.user_id = write.pk
                contacts.save()

                new = Contacts02.objects.last()
                pk = new.id

                total = Contacts02.objects.all().count()
                page = total // 20
                page = page + 1

                return render(request, '04_knowledge02_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = Contacts02Form()

    return render(request, '04_knowledge02_write.html', {'form':form, 'username': username, 'page': page, })

def board02_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board02 = Contacts02.objects.get(id=pk)
    id = specific_board02.id
    tpl = loader.get_template('04_knowledge02_detail.html')

    total = Contacts02.objects.all().count()
    page = total // 20
    page = page + 1

    ctx = Context({'specific_board02': specific_board02, 'id': id, 'username': username, 'page': page, })

    Contacts02.objects.filter(id=pk).update(hits = specific_board02.hits+1)

    return HttpResponse(tpl.render(ctx))

@csrf_exempt

def board02_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard02 = Contacts02.objects.get(id=pk)

        total = Contacts02.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard02.user_id == user.id :
            return render(request, '04_knowledge02_edit.html', {'oldboard02': oldboard02, 'username': username, 'page': page, })
        else:
            return render(request, '04_knowledge02_different.html', {'username': username, })
    return render(request, '04_knowledge02_mustlogin.html', {'username':username, 'page': page, })

def board02_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if len(request.POST['content']) == 0:
        return HttpResponse('내용을 입력해주세요.')

    if len(request.POST['title']) == 0:
        return HttpResponse('제목을 입력해주세요.')

    else:
        content = request.POST['content']
        title = request.POST['title']

        Contacts02.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '04_knowledge02_edit_db.html', {'pk': pk, 'username': username, })

def board02_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete02 = Contacts02.objects.get(id=pk)
    delete02.delete()
    total = Contacts02.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge02_delete.html', {'page': page, 'username': username, })

def search02list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.GET.get('search02') == None:
        return render_to_response('04_knowledge02_noresult.html', {'username': username, })

    searchStr = request.GET.get('search02')
    search02total = Contacts02.objects.filter(title__contains=searchStr).count()

    if search02total == None:
        return render(ruquest, '04_knowledge02_noresult.html', {'username': username, })

    contacts = Contacts02.objects.filter(title__contains=searchStr).all()
    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    return render_to_response('04_knowledge02_search02list.html', {'contacts': contacts,
        'search02total': search02total, 'searchStr':searchStr, 'username':username, })

def board02_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge02_complete.html', {'username': username, })

def board02_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts02.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge02_different.html', {'username': username, 'page': page, })

def board02_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete02 = Contacts02.objects.get(id=pk)

        if delete02.user_id == user.id :
            total = Contacts02.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge02_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Contacts02.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge02_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Contacts02.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge02_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

def knowledge040301(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    contact_list = Contacts03.objects.all().order_by('-created_at')

    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, '04_knowledge03.html', {'contacts': contacts, 'username': username })

@csrf_exempt

def board03_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Contacts03Form
    form = form_class(request.POST or None)

    total = Contacts03.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '04_knowledge03_mustlogin.html')
        else:
            if form.is_valid():
                contacts = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                contacts.user_id = write.pk
                contacts.save()

                new = Contacts03.objects.last()
                pk = new.id

                total = Contacts03.objects.all().count()
                page = total // 20
                page = page + 1

                return render(request, '04_knowledge03_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = Contacts03Form()

    return render(request, '04_knowledge03_write.html', {'form':form, 'username': username, 'page': page, })

def board03_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board03 = Contacts03.objects.get(id=pk)
    id = specific_board03.id
    tpl = loader.get_template('04_knowledge03_detail.html')

    total = Contacts03.objects.all().count()
    page = total // 20
    page = page + 1

    ctx = Context({'specific_board03': specific_board03, 'id': id, 'username': username, 'page': page, })

    Contacts03.objects.filter(id=pk).update(hits = specific_board03.hits+1)

    return HttpResponse(tpl.render(ctx))

@csrf_exempt

def board03_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard03 = Contacts03.objects.get(id=pk)

        total = Contacts03.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard03.user_id == user.id :
            return render(request, '04_knowledge03_edit.html', {'oldboard03': oldboard03, 'username': username, 'page': page})
        else:
            return render(request, '04_knowledge03_different.html', {'username': username, })
    return render(request, '04_knowledge03_mustlogin.html', {'username':username, 'page': page, })

def board03_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if len(request.POST['content']) == 0:
        return HttpResponse('내용을 입력해주세요.')

    if len(request.POST['title']) == 0:
        return HttpResponse('제목을 입력해주세요.')

    else:
        content = request.POST['content']
        title = request.POST['title']

        Contacts03.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '04_knowledge03_edit_db.html', {'pk': pk, 'username': username, })

def board03_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete03 = Contacts03.objects.get(id=pk)
    delete03.delete()
    total = Contacts03.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge03_delete.html', {'page': page, 'username': username, })

def search03list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.GET.get('search03') == None:
        return render_to_response('04_knowledge03_noresult.html', {'username': username, })

    searchStr = request.GET.get('search03')
    search03total = Contacts03.objects.filter(title__contains=searchStr).count()

    if search03total == None:
        return render(ruquest, '04_knowledge03_noresult.html', {'username': username, })

    contacts = Contacts03.objects.filter(title__contains=searchStr).all()
    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    return render_to_response('04_knowledge03_search02list.html', {'contacts': contacts,
        'search03total': search03total, 'searchStr':searchStr, 'username':username, })

def board03_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge03_complete.html', {'username': username, })

def board03_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts03.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge03_different.html', {'username': username, 'page': page, })

def board03_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete03 = Contacts03.objects.get(id=pk)

        if delete03.user_id == user.id :
            total = Contacts03.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge03_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Contacts03.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge03_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Contacts03.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge03_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

def knowledge040401(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    contact_list = Contacts04.objects.all().order_by('-created_at')

    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, '04_knowledge04.html', {'contacts': contacts, 'username': username })

@csrf_exempt

def board04_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Contacts04Form
    form = form_class(request.POST or None)

    total = Contacts04.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '04_knowledge04_mustlogin.html')
        else:
            if form.is_valid():
                contacts = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                contacts.user_id = write.pk
                contacts.save()

                new = Contacts04.objects.last()
                pk = new.id

                total = Contacts04.objects.all().count()
                page = total // 20
                page = page + 1

                return render(request, '04_knowledge04_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = Contacts04Form()

    return render(request, '04_knowledge04_write.html', {'form':form, 'username': username, 'page': page, })

def board04_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board04 = Contacts04.objects.get(id=pk)
    id = specific_board04.id
    tpl = loader.get_template('04_knowledge04_detail.html')

    total = Contacts04.objects.all().count()
    page = total // 20
    page = page + 1

    ctx = Context({'specific_board04': specific_board04, 'id': id, 'username': username, 'page': page, })

    Contacts04.objects.filter(id=pk).update(hits = specific_board04.hits+1)

    return HttpResponse(tpl.render(ctx))

@csrf_exempt

def board04_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard04 = Contacts04.objects.get(id=pk)

        total = Contacts04.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard04.user_id == user.id :
            return render(request, '04_knowledge04_edit.html', {'oldboard04': oldboard04, 'username': username, 'page': page})
        else:
            return render(request, '04_knowledge04_different.html', {'username': username, })
    return render(request, '04_knowledge04_mustlogin.html', {'username':username, 'page': page, })

def board04_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if len(request.POST['content']) == 0:
        return HttpResponse('내용을 입력해주세요.')

    if len(request.POST['title']) == 0:
        return HttpResponse('제목을 입력해주세요.')

    else:
        content = request.POST['content']
        title = request.POST['title']

        Contacts04.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '04_knowledge04_edit_db.html', {'pk': pk, 'username': username, })

def board04_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete04 = Contacts04.objects.get(id=pk)
    delete04.delete()
    total = Contacts04.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge04_delete.html', {'page': page, 'username': username, })

def search04list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.GET.get('search04') == None:
        return render_to_response('04_knowledge04_noresult.html', {'username': username, })

    searchStr = request.GET.get('search04')
    search04total = Contacts04.objects.filter(title__contains=searchStr).count()

    if search04total == None:
        return render(ruquest, '04_knowledge04_noresult.html', {'username': username, })

    contacts = Contacts04.objects.filter(title__contains=searchStr).all()
    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    return render_to_response('04_knowledge04_search02list.html', {'contacts': contacts,
        'search04total': search04total, 'searchStr':searchStr, 'username':username, })

def board04_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge04_complete.html', {'username': username, })

def board04_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts04.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge04_different.html', {'username': username, 'page': page, })

def board04_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete04 = Contacts04.objects.get(id=pk)

        if delete04.user_id == user.id :
            total = Contacts04.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge04_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Contacts04.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge04_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Contacts04.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge04_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

def knowledge040501(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    contact_list = Contacts05.objects.all().order_by('-created_at')

    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, '04_knowledge05.html', {'contacts': contacts, 'username': username })

@csrf_exempt

def board05_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Contacts05Form
    form = form_class(request.POST or None)

    total = Contacts05.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '04_knowledge05_mustlogin.html')
        else:
            if form.is_valid():
                contacts = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                contacts.user_id = write.pk
                contacts.save()

                new = Contacts05.objects.last()
                pk = new.id

                total = Contacts05.objects.all().count()
                page = total // 20
                page = page + 1

                return render(request, '04_knowledge05_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = Contacts05Form()

    return render(request, '04_knowledge05_write.html', {'form':form, 'username': username, 'page': page, })

def board05_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board05 = Contacts05.objects.get(id=pk)
    id = specific_board05.id
    tpl = loader.get_template('04_knowledge05_detail.html')

    total = Contacts05.objects.all().count()
    page = total // 20
    page = page + 1

    ctx = Context({'specific_board05': specific_board05, 'id': id, 'username': username, 'page': page, })

    Contacts05.objects.filter(id=pk).update(hits = specific_board05.hits+1)

    return HttpResponse(tpl.render(ctx))

@csrf_exempt

def board05_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard05 = Contacts05.objects.get(id=pk)

        total = Contacts05.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard05.user_id == user.id :
            return render(request, '04_knowledge05_edit.html', {'oldboard05': oldboard05, 'username': username, 'page': page})
        else:
            return render(request, '04_knowledge05_different.html', {'username': username, })
    return render(request, '04_knowledge05_mustlogin.html', {'username':username, 'page': page, })

def board05_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if len(request.POST['content']) == 0:
        return HttpResponse('내용을 입력해주세요.')

    if len(request.POST['title']) == 0:
        return HttpResponse('제목을 입력해주세요.')

    else:
        content = request.POST['content']
        title = request.POST['title']

        Contacts05.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '04_knowledge05_edit_db.html', {'pk': pk, 'username': username, })

def board05_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete05 = Contacts05.objects.get(id=pk)
    delete05.delete()
    total = Contacts05.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge05_delete.html', {'page': page, 'username': username, })

def search05list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.GET.get('search05') == None:
        return render_to_response('04_knowledge05_noresult.html', {'username': username, })

    searchStr = request.GET.get('search05')
    search05total = Contacts05.objects.filter(title__contains=searchStr).count()

    if search05total == None:
        return render(ruquest, '04_knowledge05_noresult.html', {'username': username, })

    contacts = Contacts05.objects.filter(title__contains=searchStr).all()
    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    return render_to_response('04_knowledge05_search05list.html', {'contacts': contacts,
        'search05total': search05total, 'searchStr':searchStr, 'username':username, })

def board05_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge05_complete.html', {'username': username, })

def board05_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts05.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge05_different.html', {'username': username, 'page': page, })

def board05_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete05 = Contacts05.objects.get(id=pk)

        if delete05.user_id == user.id :
            total = Contacts05.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge05_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Contacts05.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge05_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Contacts05.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge05_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

def knowledge040601(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    customer_list = Contacts06q.objects.all().order_by('-created_at')

    paginator = Paginator(customer_list, 20)

    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, '04_knowledge06.html', {'contacts': contacts, 'username': username })

@csrf_exempt

def board06_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None
    total = Contacts06q.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        form = Contacts06qForm(request.POST)
        if form.is_valid():
            form.save()
            new = Contacts06q.objects.last()
            pk = new.id

            total = Contacts06q.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '04_knowledge06_complete.html', {'pk': pk, 'username': username, 'page': page, })

    else:
        form = Contacts06qForm()

    return render(request, '04_knowledge06_write.html', {'form':form, 'username': username, 'page': page, })

def board06_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board01 = Contacts06q.objects.get(id=pk)

    try:
        prev = specific_board01.get_previous_by_created_at()
    except :
        prev = None

    try:
        next = specific_board01.get_next_by_created_at()
    except :
        next = None

    r_form = Contacts06a.objects.filter(contacts06q_id=pk).last()

    total = Contacts06q.objects.all().count()
    page = total // 20
    page = page + 1
    pk = pk

    Contacts06q.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '04_knowledge06_detail.html', {'specific_board01': specific_board01,
    'username': username, 'page': page, 'prev': prev, 'next': next, 'pk': pk, 'r_form': r_form, })

@csrf_exempt

def board06_editconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific = Contacts06q.objects.filter(id=pk).get()
    pk = pk
    try:
        password = request.POST['password']
    except:
        password = None

    pw = specific.password

    if password :
        if password == pw :
            return render(request, '04_knowledge06_edit.html', {'username': username, 'pk': pk, 'specific': specific, })
        else :
            return render(request, '04_knowledge06_different.html', {'username': username, 'pk': pk, })

    return render(request, '04_knowledge06_editconfirm.html', {'username': username, 'pk': pk, 'specific': specific, })

@csrf_exempt

def board06_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    oldboard01 = Contacts06q.objects.get(id=pk)
    pk = pk

    return render(request, '04_knowledge06_edit.html', {'username': username, 'oldboard01': oldboard01,
                                                        'pk': pk, })

def board06_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if len(request.POST['content']) == 0:
        return HttpResponse('내용을 입력해주세요.')

    if len(request.POST['title']) == 0:
        return HttpResponse('제목을 입력해주세요.')

    else:
        content = request.POST['content']
        title = request.POST['title']

        Contacts06q.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '04_knowledge06_edit_db.html', {'pk': pk, 'username': username, })

def board06_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete06 = Contacts06q.objects.get(id=pk)
    delete06.delete()
    total = Contacts06q.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge06_delete.html', {'page': page, 'username': username, })

def search06list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.GET.get('search06') == None:
        return render_to_response('04_knowledge06_noresult.html', {'username': username, })

    searchStr = request.GET.get('search01')
    search06total = Contatcs06q.objects.filter(title__contains=searchStr).count()

    if search06total == None:
        return render(ruquest, '04_knowledge06_noresult.html', {'username': username, })

    customer = Contacts06q.objects.filter(title__contains=searchStr).all()
    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    return render_to_response('04_knowledge06_search06list.html', {'customer': customer,
        'search06total': search06total, 'searchStr':searchStr, 'username':username, })

def board06_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge06_complete.html', {'username': username, })

def board06_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts06q.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '04_knowledge06_different.html', {'username': username, 'page': page, })

@csrf_exempt

def board06_deleteconfirm1(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts06q.objects.all().count()
    page = total // 20
    page = page + 1

    specific = Contacts06q.objects.filter(id=pk).get()
    pk = pk
    try:
        password = request.POST['password']
    except:
        password = None

    pw = specific.password

    if password :
        if password == pw :
            return render(request, '04_knowledge06_deleteconfirm2.html', {'username': username, 'pk': pk,
                                                                          'specific': specific, 'page': page, })
        else :
            return render(request, '04_knowledge06_different.html', {'username': username, 'pk': pk, 'page': page, })

    return render(request, '04_knowledge06_deleteconfirm1.html', {'username': username, 'pk': pk, 'specific': specific, })

def board06_deleteconfirm2(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge06_deleteconfirm2.html', {'uesrname': username, 'pk': pk, })

@csrf_exempt

def board06_answer(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None
    pk = pk
    form_class = Contacts06aForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            r_form = form.save(commit=False)
            write = User.objects.filter(username=username).get()
            specific_board01 = Contacts06q.objects.filter(pk=pk).get()
            r_form.user_id = write.pk
            r_form.contacts06q_id = specific_board01.pk
            r_form.save()

            try:
                prev = specific_board01.get_previous_by_created_at()
            except:
                prev = None

            try:
                next = specific_board01.get_next_by_created_at()
            except:
                next = None

            return render(request, '04_knowledge06_detail.html', {'pk': pk, 'username': username, 'r_form': r_form,
                                                                  'specific_board01': specific_board01, 'prev': prev,
                                                                  'next': next, })

        else:
            form = Contacts06aForm()

    return render(request, '04_knowledge06_answer.html', {'form': form, 'username': username, })

@csrf_exempt

def board06_answeredit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Contacts06aForm
    form = form_class(request.POST or None)
    pk = pk
    specific = Contacts06a.objects.filter(contacts06q_id=pk).last()

    if request.method == 'POST':
        if form.is_valid():
            reply = request.POST['reply']
            question = Contacts06q.objects.filter(id=pk).get()

            Contacts06a.objects.filter(contacts06q_id=question.id).update(reply=reply)

            specific_board01 = Contacts06q.objects.filter(pk=pk).get()
            r_form = Contacts06a.objects.filter(contacts06q_id=question.id).last()

            try:
                prev = specific_board01.get_previous_by_created_at()
            except:
                prev = None

            try:
                next = specific_board01.get_next_by_created_at()
            except:
                next = None

            return render(request, '04_knowledge06_detail.html', {'pk': pk, 'username': username, 'r_form': r_form,
                                                                  'specific': specific, 'prev': prev, 'next': next, })

        else:
            form = Contacts06aForm()
    return render(request, '04_knowledge06_answeredit.html', {'username': username, 'pk': pk,
                                                              'form': form, 'specific': specific, })

def board06_answerdeletecon(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None
    pk = pk
    return render(request, '04_knowledge06_answerdeletecon.html', {'username': username, 'pk': pk, })

def board06_answerdelete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete = Contacts06a.objects.filter(contacts06q_id=pk).all()
    delete.delete()
    total = Contacts06q.objects.all().count()
    page = total // 20
    page = page + 1

    pk = pk

    return render(request, '04_knowledge06_answerdelete.html', {'page': page, 'username': username, 'pk': pk, })

from django.shortcuts import render, render_to_response, redirect
from .models import Contacts, Contacts02, Contacts03, Contacts04, Contacts05, Contacts06q
from .models2 import Contacts06a
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from knowledge.forms import ContactsForm, Contacts02Form, Contacts03Form, Contacts04Form, Contacts05Form
from knowledge.forms import Contacts06qForm, Contacts06aForm
from django.http import HttpResponse
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

    index = paginator.page_range.index(contacts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '04_knowledge01.html', {'contacts': contacts, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def board01_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = ContactsForm()

    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        write = User.objects.filter(username=username).get()
        contacts.user_id = write.pk
        contacts.save()

        new = Contacts.objects.last()
        pk = new.id

        return redirect(board01_detail, pk=pk)
    return render(request, '04_knowledge01_write.html', {'form':form, 'username': username, })

def board01_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    specific_board01 = Contacts.objects.get(id=pk)
    total = Contacts.objects.all().count()
    c_count = Contacts.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    Contacts.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '04_knowledge01_detail.html', {'specific_board01': specific_board01, 'pk': pk,
                                                           'username': username, 'page': page, })

@csrf_exempt

def board01_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    oldboard01 = Contacts.objects.get(id=pk)

    if oldboard01.user_id == user.id :
        return render(request, '04_knowledge01_edit.html', {'oldboard01': oldboard01, 'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge01_different.html', {'username': username, })

def board01_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

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
    c_count = Contacts.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge01_delete.html', {'username': username, 'page': page, })

def search01list(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Contacts.objects.filter(title__contains=searchStr).count()
    searchAll = Contacts.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchPage = paginator.page(page)
    except PageNotAnInteger:
        searchPage = paginator.page(1)
    except EmptyPage:
        searchPage = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '04_knowledge01_search01list.html', {'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'msg': msg, })
    return render(request, '04_knowledge01_search01list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchPage': searchPage, 'page_range': page_range, })

def board01_different(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge01_different.html', {'username': username, })

def board01_deleteconfirm(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    user = User.objects.filter(username=username).get()
    delete01 = Contacts.objects.get(id=pk)

    if delete01.user_id == user.id :
        return render(request, '04_knowledge01_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge01_different.html', {'username': username, 'pk': pk, })

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

    index = paginator.page_range.index(contacts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '04_knowledge02.html', {'contacts': contacts, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def board02_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Contacts02Form()
    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        write = User.objects.filter(username=username).get()
        contacts.user_id = write.pk
        contacts.save()

        new = Contacts02.objects.last()
        pk = new.id

        return redirect(board02_detail, pk=pk)

    else:
        form = Contacts02Form()

    return render(request, '04_knowledge02_write.html', {'form':form, 'username': username, })

def board02_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board02 = Contacts02.objects.get(id=pk)
    Contacts02.objects.filter(id=pk).update(hits = specific_board02.hits+1)

    total = Contacts02.objects.all().count()
    c_count = Contacts02.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge02_detail.html', {'specific_board02': specific_board02, 'page': page, 'username': username, 'pk': pk, })

@csrf_exempt

def board02_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    oldboard02 = Contacts02.objects.get(id=pk)

    if oldboard02.user_id == user.id :
        return render(request, '04_knowledge02_edit.html', {'oldboard02': oldboard02, 'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge02_different.html', {'username': username, 'pk': pk, })

def board02_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

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
    c_count = Contacts02.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge02_delete.html', {'page': page, 'username': username, })

def search02list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Contacts02.objects.filter(title__contains=searchStr).count()
    searchAll = Contacts02.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchPage = paginator.page(page)
    except PageNotAnInteger:
        searchPage = paginator.page(1)
    except EmptyPage:
        searchPage = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '04_knowledge02_search02list.html', {'username': username, 'searchStr':searchStr, 'searchCount': searchCount, 'msg': msg, })

    return render(request, '04_knowledge02_search02list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'page_range': page_range, })

def board02_different(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge02_different.html', {'username': username, })

def board02_deleteconfirm(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    delete02 = Contacts02.objects.get(id=pk)

    if delete02.user_id == user.id :
        return render(request, '04_knowledge02_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge02_different.html', {'username': username, 'pk': pk, })

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

    index = paginator.page_range.index(contacts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '04_knowledge03.html', {'contacts': contacts, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def board03_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Contacts03Form()
    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        write = User.objects.filter(username=username).get()
        contacts.user_id = write.pk
        contacts.save()

        new = Contacts03.objects.last()
        pk = new.id

        return redirect(board03_detail, pk=pk)
    return render(request, '04_knowledge03_write.html', {'form':form, 'username': username, })

def board03_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board03 = Contacts03.objects.get(id=pk)
    Contacts03.objects.filter(id=pk).update(hits = specific_board03.hits+1)

    total = Contacts03.objects.all().count()
    c_count = Contacts03.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge03_detail.html', {'specific_board03': specific_board03, 'page': page, 'username': username, 'pk': pk, })

@csrf_exempt

def board03_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    oldboard03 = Contacts03.objects.get(id=pk)

    if oldboard03.user_id == user.id :
        return render(request, '04_knowledge03_edit.html', {'oldboard03': oldboard03, 'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge03_different.html', {'username': username, 'pk': pk, })

def board03_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

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
    c_count = Contacts03.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge03_delete.html', {'page': page, 'username': username, })

def search03list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Contacts03.objects.filter(title__contains=searchStr).count()
    searchAll = Contacts03.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchPage = paginator.page(page)
    except PageNotAnInteger:
        searchPage = paginator.page(1)
    except EmptyPage:
        searchPage = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '04_knowledge03_search03list.html', {'username': username, 'searchStr':searchStr, 'searchCount': searchCount, 'msg': msg, })
    return render(request, '04_knowledge03_search03list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'page_range': page_range, })

def board03_different(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge03_different.html', {'username': username, })

def board03_deleteconfirm(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    delete03 = Contacts03.objects.get(id=pk)

    if delete03.user_id == user.id :
        return render(request, '04_knowledge03_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge03_different.html', {'username': username, 'pk': pk, })

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

    index = paginator.page_range.index(contacts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '04_knowledge04.html', {'contacts': contacts, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def board04_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Contacts04Form()
    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        write = User.objects.filter(username=username).get()
        contacts.user_id = write.pk
        contacts.save()

        new = Contacts04.objects.last()
        pk = new.id

        return redirect(board04_detail, pk=pk)
    return render(request, '04_knowledge04_write.html', {'form':form, 'username': username, })

def board04_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board04 = Contacts04.objects.get(id=pk)
    Contacts04.objects.filter(id=pk).update(hits = specific_board04.hits+1)

    total = Contacts04.objects.all().count()
    c_count = Contacts04.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge04_detail.html', {'specific_board04': specific_board04, 'page': page, 'username': username, 'pk': pk, })

@csrf_exempt

def board04_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    oldboard04 = Contacts04.objects.get(id=pk)

    if oldboard04.user_id == user.id :
        return render(request, '04_knowledge04_edit.html', {'oldboard04': oldboard04, 'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge04_different.html', {'username': username, 'pk': pk, })

def board04_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

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
    c_count = Contacts04.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge04_delete.html', {'page': page, 'username': username, })

def search04list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Contacts04.objects.filter(title__contains=searchStr).count()
    searchAll = Contacts04.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchPage = paginator.page(page)
    except PageNotAnInteger:
        searchPage = paginator.page(1)
    except EmptyPage:
        searchPage = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '04_knowledge04_search04list.html', {'username': username, 'searchStr':searchStr, 'searchCount': searchCount, 'msg': msg, })
    return render(request, '04_knowledge04_search04list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'page_range': page_range, })

def board04_different(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge04_different.html', {'username': username, })

def board04_deleteconfirm(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    delete04 = Contacts04.objects.get(id=pk)

    if delete04.user_id == user.id :
        return render(request, '04_knowledge04_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge04_different.html', {'username': username, 'pk': pk, })

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

    index = paginator.page_range.index(contacts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '04_knowledge05.html', {'contacts': contacts, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def board05_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Contacts05Form()
    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        write = User.objects.filter(username=username).get()
        contacts.user_id = write.pk
        contacts.save()

        new = Contacts05.objects.last()
        pk = new.id

        return redirect(board05_detail, pk=pk)
    return render(request, '04_knowledge05_write.html', {'form':form, 'username': username, })

def board05_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board05 = Contacts05.objects.get(id=pk)
    Contacts05.objects.filter(id=pk).update(hits = specific_board05.hits+1)

    total = Contacts05.objects.all().count()
    c_count = Contacts05.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge05_detail.html', {'specific_board05': specific_board05, 'page': page, 'username': username, 'pk': pk, })

@csrf_exempt

def board05_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    oldboard05 = Contacts05.objects.get(id=pk)

    if oldboard05.user_id == user.id :
        return render(request, '04_knowledge05_edit.html', {'oldboard05': oldboard05, 'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge05_different.html', {'username': username, 'pk': pk, })

def board05_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

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
    c_count = Contacts05.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge05_delete.html', {'page': page, 'username': username, })

def search05list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Contacts05.objects.filter(title__contains=searchStr).count()
    searchAll = Contacts05.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchPage = paginator.page(page)
    except PageNotAnInteger:
        searchPage = paginator.page(1)
    except EmptyPage:
        searchPage = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '04_knowledge05_search05list.html', {'username': username, 'searchStr':searchStr, 'searchCount': searchCount, 'msg': msg, })
    return render(request, '04_knowledge05_search05list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'page_range': page_range, })

def board05_different(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '04_knowledge05_different.html', {'username': username, })

def board05_deleteconfirm(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    delete05 = Contacts05.objects.get(id=pk)

    if delete05.user_id == user.id :
        return render(request, '04_knowledge05_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '04_knowledge05_different.html', {'username': username, 'pk': pk, })

def knowledge040601(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    contact_list = Contacts06q.objects.all().order_by('-created_at')
    paginator = Paginator(contact_list, 20)
    page = request.GET.get('page', 1)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(contacts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '04_knowledge06.html', {'contacts': contacts, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def board06_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Contacts06qForm()
    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.writer = request.POST['writer']
        contacts.password = request.POST['password']
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        contacts.save()
        new = Contacts06q.objects.last()
        pk = new.id
        return redirect(board06_detail, pk=pk)
    return render(request, '04_knowledge06_write.html', {'form':form, 'username': username, })

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
    c_count = Contacts06q.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1
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
    return render(request, '04_knowledge06_edit.html', {'username': username, 'oldboard01': oldboard01, 'pk': pk, })

def board06_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

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
    c_count = Contacts06q.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge06_delete.html', {'page': page, 'username': username, })

def search06list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Contacts06q.objects.filter(title__contains=searchStr).count()
    searchAll = Contacts06q.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchPage = paginator.page(page)
    except PageNotAnInteger:
        searchPage = paginator.page(1)
    except EmptyPage:
        searchPage = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '04_knowledge06_search06list.html', {'username': username, 'searchStr':searchStr, 'searchCount': searchCount, 'msg': msg, })
    return render(request, '04_knowledge06_search06list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'page_range': page_range, })

def board06_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Contacts06q.objects.all().count()
    c_count = Contacts06q.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '04_knowledge06_different.html', {'username': username, 'page': page, })

@csrf_exempt

def board06_deleteconfirm1(request, pk):
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
            return render(request, '04_knowledge06_deleteconfirm2.html', {'username': username, 'pk': pk, 'specific': specific, })
        else :
            return render(request, '04_knowledge06_different.html', {'username': username, 'pk': pk, })
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
    form = Contacts06aForm()
    if request.method == 'POST':
        r_form = form.save(commit=False)
        write = User.objects.filter(username=username).get()
        specific_board01 = Contacts06q.objects.filter(pk=pk).get()
        r_form.user_id = write.pk
        r_form.contacts06q_id = specific_board01.pk
        r_form.reply = request.POST['reply']
        r_form.save()

        return redirect(board06_detail, pk=pk)
    return render(request, '04_knowledge06_answer.html', {'form': form, 'username': username, })

@csrf_exempt

def board06_answeredit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Contacts06aForm()
    pk = pk
    specific = Contacts06a.objects.filter(contacts06q_id=pk).last()

    if request.method == 'POST':
        reply = request.POST['reply']
        question = Contacts06q.objects.filter(id=pk).get()
        Contacts06a.objects.filter(contacts06q_id=question.id).update(reply=reply)

        specific_board01 = Contacts06q.objects.filter(pk=pk).get()
        r_form = Contacts06a.objects.filter(contacts06q_id=question.id).last()

        return redirect(board06_detail, pk=pk)
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

    pk = pk
    delete = Contacts06a.objects.filter(contacts06q_id=pk).all()
    delete.delete()

    return render(request, '04_knowledge06_answerdelete.html', {'pk' : pk, 'username': username, })

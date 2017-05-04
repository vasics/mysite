from django.shortcuts import render, render_to_response, redirect
from .models import Customer01, Customer02, Customer03, Customer04
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from customer.forms import Customer01Form, Customer02Form, Customer03Form, Customer04Form
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime

def customer070101(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    customer_list = Customer01.objects.all().order_by('-created_at')
    paginator = Paginator(customer_list, 20)
    page = request.GET.get('page', 1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(customer.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '07_customer01.html', {'customer': customer, 'username': username, 'page_range': page_range, 'page': page, })

@csrf_exempt

def customer01_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Customer01Form()

    if request.method == 'POST':
        contacts = form.save(commit=False)
        contacts.title = request.POST['title']
        contacts.content = request.POST['content']
        write = User.objects.filter(username=username).get()
        contacts.user_id = write.pk
        contacts.save()

        new = Customer01.objects.last()
        pk = new.id

        return redirect(customer01_detail, pk=pk)
    return render(request, '07_customer01_write.html', {'form':form, 'username': username, })

def customer01_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    specific_board01 = Customer01.objects.get(id=pk)
    try:
        prev = specific_board01.get_previous_by_created_at()
    except :
        prev = None
    try:
        next = specific_board01.get_next_by_created_at()
    except :
        next = None

    total = Customer01.objects.all().count()
    c_count = Customer01.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    Customer01.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '07_customer01_detail.html', {'specific_board01': specific_board01, 'username': username, 'page': page, 'next': next, 'prev': prev, 'pk': pk, })

@csrf_exempt

def customer01_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    user = User.objects.filter(username=username).get()
    oldboard01 = Customer01.objects.get(id=pk)

    if oldboard01.user_id == user.id :
        return render(request, '07_customer01_edit.html', {'oldboard01': oldboard01, 'username': username, 'pk': pk, })
    else:
        return render(request, '07_customer01_different.html', {'username': username, })

def customer01_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    content = request.POST['content']
    title = request.POST['title']
    Customer01.objects.filter(id=pk).update(content=content, title=title)

    return render(request, '07_customer01_edit_db.html', {'pk': pk, 'username': username, })

def customer01_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete01 = Customer01.objects.get(id=pk)
    delete01.delete()
    total = Customer01.objects.all().count()
    c_count = Customer01.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '07_customer01_delete.html', {'page': page, 'username': username, })

def customer01_search01list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Customer01.objects.filter(title__contains=searchStr).count()
    searchAll = Customer01.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchAll = paginator.page(page)
    except PageNotAnInteger:
        searchAll = paginator.page(1)
    except EmptyPage:
        searchAll = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '07_customer01_search01list.html', {'searchStr':searchStr, 'username':username,
        'searchCount': searchCount, 'searchAll': searchAll, 'msg': msg, })

    return render(request, '07_customer01_search01list.html', {'searchStr':searchStr, 'username':username,
    'searchCount': searchCount, 'searchAll': searchAll, 'searchPage': searchPage, 'page_range': page_range, })

def customer01_different(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '07_customer01_different.html', {'username': username, })

def customer01_deleteconfirm(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    user = User.objects.filter(username=username).get()
    delete01 = Customer01.objects.get(id=pk)

    if delete01.user_id == user.id :
        return render(request, '07_customer01_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '07_customer01_different.html', {'username': username, 'pk': pk, })

def customer070201(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    customer_list = Customer02.objects.all().order_by('-created_at')
    paginator = Paginator(customer_list, 20)
    page = request.GET.get('page', 1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(customer.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '07_customer02.html', {'customer': customer, 'username': username, 'page': page, 'page_range': page_range, })

@csrf_exempt

def customer02_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Customer02Form()
    if request.method == 'POST':
        customer = form.save(commit=False)
        write = User.objects.filter(username=username).get()
        customer.title = request.POST['title']
        customer.content = request.POST['content']
        customer.user_id = write.pk
        customer.save()

        new = Customer02.objects.last()
        pk = new.id

        return redirect(customer02_detail, pk=pk)
    return render(request, '07_customer02_write.html', {'form':form, 'username': username, })

def customer02_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board01 = Customer02.objects.get(id=pk)
    author = User.objects.filter(id=specific_board01.user_id).get()

    try:
        prev = specific_board01.get_previous_by_created_at()
    except :
        prev = None
    try:
        next = specific_board01.get_next_by_created_at()
    except :
        next = None

    total = Customer02.objects.all().count()
    c_count = Customer02.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    Customer02.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '07_customer02_detail.html', {'specific_board01': specific_board01,
    'username': username, 'page': page, 'prev': prev, 'next': next, 'author': author, 'pk': pk, })

@csrf_exempt

def customer02_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None
    pk = pk
    user = User.objects.filter(username=username).get()
    oldboard01 = Customer02.objects.get(id=pk)

    if oldboard01.user_id == user.id :
        return render(request, '07_customer02_edit.html', {'oldboard01': oldboard01, 'username': username, 'pk': pk, })
    else:
        return render(request, '07_customer02_different.html', {'username': username, })

def customer02_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    content = request.POST['content']
    title = request.POST['title']
    Customer02.objects.filter(id=pk).update(content=content, title=title)

    return render(request, '07_customer02_edit_db.html', {'pk': pk, 'username': username, })

def customer02_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete02 = Customer02.objects.get(id=pk)
    delete02.delete()
    total = Customer02.objects.all().count()
    c_count = Customer02.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '07_customer02_delete.html', {'page': page, 'username': username, })

def customer02_search02list(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Customer02.objects.filter(title__contains=searchStr).count()
    searchAll = Customer02.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchAll = paginator.page(page)
    except PageNotAnInteger:
        searchAll = paginator.page(1)
    except EmptyPage:
        searchAll = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '07_customer02_search02list.html', {'searchStr':searchStr, 'username':username,
        'searchCount': searchCount, 'searchAll': searchAll, 'msg': msg, })

    return render(request, '07_customer02_search02list.html', {'searchStr':searchStr, 'username':username,
    'searchCount': searchCount, 'searchAll': searchAll, 'searchPage': searchPage, 'page_range': page_range, })

def customer02_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '07_customer02_different.html', {'username': username, })

def customer02_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    user = User.objects.filter(username=username).get()
    delete02 = Customer02.objects.get(id=pk)

    if delete02.user_id == user.id :
        return render(request, '07_customer02_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '07_customer02_different.html', {'username': username, 'pk': pk, })

def customer070301(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    customer_list = Customer03.objects.all().order_by('-created_at')
    paginator = Paginator(customer_list, 20)
    page = request.GET.get('page', 1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    t = datetime.datetime.now()
    to = str(t)
    tod = to[0:4] + to[5:7] + to[8:10]
    today = int(tod)

    index = paginator.page_range.index(customer.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '07_customer03.html', {'customer': customer, 'username': username, 'today': today, 'page': page, 'page_range': page_range, })

@csrf_exempt

def customer03_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Customer03Form()
    if request.method == 'POST':
        customer = form.save(commit=False)
        write = User.objects.filter(username=username).get()
        customer.user_id = write.pk
        customer.content = request.POST['content']
        customer.title = request.POST['title']
        a = request.POST['end_date']
        b = str(a)
        c = b[0:4] + "0" + b[5] + b[8:10]
        cint = int(c)
        customer.end_date = cint
        d = request.POST['start_date']
        e = str(d)
        f = e[0:4] + "0" + e[5] + e[8:10]
        fint = int(f)
        customer.start_date = fint
        customer.save()

        new = Customer03.objects.last()
        pk = new.id
        return redirect(customer03_detail, pk=pk)
    return render(request, '07_customer03_write.html', {'username': username, 'form': form, })

def customer03_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board01 = Customer03.objects.get(id=pk)
    author = User.objects.filter(id=specific_board01.user_id).get()

    try:
        prev = specific_board01.get_previous_by_created_at()
    except :
        prev = None
    try:
        next = specific_board01.get_next_by_created_at()
    except :
        next = None

    total = Customer03.objects.all().count()
    c_count = Customer03.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    Customer03.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '07_customer03_detail.html', {'specific_board01': specific_board01,
    'username': username, 'page': page, 'prev': prev, 'next': next, 'author': author, })

@csrf_exempt

def customer03_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    user = User.objects.filter(username=username).get()
    oldboard01 = Customer03.objects.get(id=pk)

    if oldboard01.user_id == user.id :
        return render(request, '07_customer03_edit.html', {'oldboard01': oldboard01, 'username': username, 'pk': pk, })
    else:
        return render(request, '07_customer03_different.html', {'username': username, })

def customer03_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    content = request.POST['content']
    title = request.POST['title']
    a = request.POST['end_date']
    b = str(a)
    c = b[0:4] + "0" + b[5] + b[8:10]
    cint = int(c)
    d = request.POST['start_date']
    e = str(d)
    f = e[0:4] + "0" + e[5] + e[8:10]
    fint = int(f)

    Customer03.objects.filter(id=pk).update(content=content, title=title, end_date=cint, start_date=fint)

    return render(request, '07_customer03_edit_db.html', {'pk': pk, 'username': username, })

def customer03_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete02 = Customer03.objects.get(id=pk)
    delete02.delete()
    total = Customer03.objects.all().count()
    c_count = Customer03.objects.order_by('created_at')[:int(pk)].count()
    page = (total - c_count) // 20 + 1

    return render(request, '07_customer03_delete.html', {'page': page, 'username': username, })

def customer03_search03list(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    searchStr = request.GET.get('search')
    searchCount = Customer03.objects.filter(title__contains=searchStr).count()
    searchAll = Customer03.objects.filter(title__contains=searchStr).all().order_by('-created_at')

    paginator = Paginator(searchAll, 20)
    page = request.GET.get('page', 1)
    try:
        searchAll = paginator.page(page)
    except PageNotAnInteger:
        searchAll = paginator.page(1)
    except EmptyPage:
        searchAll = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(searchPage.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render(request, '07_customer03_search03list.html', {'searchStr':searchStr, 'username':username,
        'searchCount': searchCount, 'searchAll': searchAll, 'msg': msg, })
    return render(request, '07_customer03_search03list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, 'searchCount': searchCount, 'searchPage': searchPage, 'page_range': page_range, })

def customer03_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '07_customer03_different.html', {'username': username, })

def customer03_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk
    user = User.objects.filter(username=username).get()
    delete03 = Customer03.objects.get(id=pk)

    if delete03.user_id == user.id :
        return render(request, '07_customer03_deleteconfirm.html', {'username': username, 'pk': pk, })
    else:
        return render(request, '07_customer03_different.html', {'username': username, 'pk': pk, })

def customer070401(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    customer_list = Customer04.objects.all().order_by('-created_at')
    paginator = Paginator(customer_list, 20)
    page = request.GET.get('page', 1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    index = paginator.page_range.index(customer.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, '07_customer04.html', {'customer': customer, 'username': username, 'page_range': page_range, 'page': page, })

@csrf_exempt

def customer04_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form = Customer04Form()
    if request.method == 'POST':
        customer = form.save(commit=False)
        customer.title = request.POST['title']
        customer.content = request.POST['content']
        customer.writer = request.POST['writer']
        customer.password = request.POST['password']
        customer.save()

        customer_list = Customer04.objects.all().order_by('-created_at')
        paginator = Paginator(customer_list, 20)
        page = request.GET.get('page', 1)
        try:
            customer = paginator.page(page)
        except PageNotAnInteger:
            customer = paginator.page(1)
        except EmptyPage:
            customer = paginator.page(paginator.num_pages)

        index = paginator.page_range.index(customer.number)
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = paginator.page_range[start_index:end_index]

        return render(request, '07_customer04.html', {'page':page, 'page_range':page_range, 'customer':customer, 'username': username, })
    return render(request, '07_customer04_write.html', {'form':form, 'username': username, })

@csrf_exempt

def customer04_answer(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if request.method == 'POST':
        user = User.objects.filter(username=username).get()
        answer = request.POST['answer']
        Customer04.objects.filter(id=pk).update(answer=answer, user=user.pk)

        customer_list = Customer04.objects.all().order_by('-created_at')
        paginator = Paginator(customer_list, 20)
        page = request.GET.get('page', 1)
        try:
            customer = paginator.page(page)
        except PageNotAnInteger:
            customer = paginator.page(1)
        except EmptyPage:
            customer = paginator.page(paginator.num_pages)

        index = paginator.page_range.index(customer.number)
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = paginator.page_range[start_index:end_index]

        return render(request, '07_customer04.html', {'page':page, 'page_range':page_range, 'customer':customer, 'username': username, })
    return render(request, '07_customer04_answer.html', {'username': username, })

def customer04_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    return render(request, '07_customer04_delete.html', {'username': username, 'pk': pk, })

def customer04_delete_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete = Customer04.objects.get(id=pk)
    delete.delete()

    return render(request, '07_customer04_delete_db.html', {'username': username, })

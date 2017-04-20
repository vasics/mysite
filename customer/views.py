from django.shortcuts import render, render_to_response, redirect
from .models import Customer01, Customer02, Customer03, Customer04
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from customer.forms import Customer01Form, Customer02Form, Customer03Form, Customer04Form, Customer04rForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime

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

    return render(request, '07_customer01.html', {'customer': customer, 'username': username })

@csrf_exempt

def customer01_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Customer01Form
    form = form_class(request.POST or None)

    total = Customer01.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '07_customer01_mustlogin.html')
        else:
            if form.is_valid():
                customer = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                customer.user_id = write.pk
                customer.save()

                new = Customer01.objects.last()
                pk = new.id

                total = Customer01.objects.all().count()
                page = total // 20
                page = page + 1

                return render(request, '07_customer01_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = Customer01Form()

    return render(request, '07_customer01_write.html', {'form':form, 'username': username, 'page': page, })

def customer01_detail(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    specific_board01 = Customer01.objects.get(id=pk)
    author = User.objects.filter(id=specific_board01.user_id).get()
    try:
        prev = specific_board01.get_previous_by_created_at()
    except :
        prev = None

    try:
        next = specific_board01.get_next_by_created_at()
    except :
        next = None

    total = Customer01.objects.all().count()
    page = total // 20
    page = page + 1

    Customer01.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '07_customer01_detail.html', {'specific_board01': specific_board01,
    'username': username, 'page': page, 'prev': prev, 'next': next, 'author': author, })

@csrf_exempt

def customer01_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard01 = Customer01.objects.get(id=pk)

        total = Customer01.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard01.user_id == user.id :
            return render(request, '07_customer01_edit.html', {'oldboard01': oldboard01, 'username': username, 'page': page, })
        else:
            return render(request, '07_customer01_different.html', {'username': username, })
    return render(request, '07_cutomer01_mustlogin.html', {'username':username, 'page': page, })

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
    page = total // 20
    page = page + 1

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

    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render_to_response('07_customer01_search01list.html', {'searchStr':searchStr, 'username':username,
        'searchCount': searchCount, 'searchAll': searchAll, 'msg': msg, })

    return render_to_response('07_customer01_search01list.html', {'searchStr':searchStr, 'username':username,
    'searchCount': searchCount, 'searchAll': searchAll, })

def customer01_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '07_customer01_complete.html', {'username': username, })

def customer01_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Customer01.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '07_customer01_different.html', {'username': username, 'page': page, })

def customer01_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete01 = Customer01.objects.get(id=pk)

        if delete01.user_id == user.id :
            total = Customer01.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '07_customer01_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Customer01.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '07_customer01_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Customer01.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '07_customer01_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

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

    return render(request, '07_customer02.html', {'customer': customer, 'username': username })

@csrf_exempt

def customer02_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Customer02Form
    form = form_class(request.POST or None)

    total = Customer02.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if not username:
            return render(request, '07_customer02_mustlogin.html')
        else:
            if form.is_valid():
                customer = form.save(commit=False)
                write = User.objects.filter(username=username).get()
                customer.user_id = write.pk
                customer.save()

                new = Customer02.objects.last()
                pk = new.id

                total = Customer02.objects.all().count()
                page = total // 20
                page = page + 1

                return render(request, '07_customer02_complete.html', {'pk': pk, 'username': username, 'page': page, })

            else:
                form = Customer02Form()

    return render(request, '07_customer02_write.html', {'form':form, 'username': username, 'page': page, })

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
    page = total // 20
    page = page + 1

    Customer02.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '07_customer02_detail.html', {'specific_board01': specific_board01,
    'username': username, 'page': page, 'prev': prev, 'next': next, 'author': author, })

@csrf_exempt

def customer02_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard01 = Customer02.objects.get(id=pk)

        total = Customer02.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard01.user_id == user.id :
            return render(request, '07_customer02_edit.html', {'oldboard01': oldboard01, 'username': username, 'page': page, })
        else:
            return render(request, '07_customer02_different.html', {'username': username, })
    return render(request, '07_customer02_mustlogin.html', {'username':username, 'page': page, })

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
    page = total // 20
    page = page + 1

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

    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render_to_response('07_customer02_search02list.html', {'searchStr':searchStr, 'username':username,
        'searchCount': searchCount, 'searchAll': searchAll, 'msg': msg, })

    return render_to_response('07_customer02_search02list.html', {'searchStr':searchStr, 'username':username,
    'searchCount': searchCount, 'searchAll': searchAll, })

def customer02_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '07_customer02_complete.html', {'username': username, })

def customer02_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Customer02.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '07_customer02_different.html', {'username': username, 'page': page, })

def customer02_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete02 = Customer02.objects.get(id=pk)

        if delete02.user_id == user.id :
            total = Customer02.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '07_customer02_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Customer02.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '07_customer02_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Customer02.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '07_customer02_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

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



    return render(request, '07_customer03.html', {'customer': customer, 'username': username })

@csrf_exempt

def customer03_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Customer03.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        write = User.objects.filter(username=username).get()
        customer.user_id = write.pk
        customer.save()

        new = Customer03.objects.last()
        pk = new.id
        return render(request, '07_customer03_complete.html', {'pk': pk, 'username': username, })
    return render(request, '07_customer03_write.html', {'username': username, 'page': page, })

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
    page = total // 20
    page = page + 1

    Customer03.objects.filter(id=pk).update(hits = specific_board01.hits+1)

    return render(request, '07_customer03_detail.html', {'specific_board01': specific_board01,
    'username': username, 'page': page, 'prev': prev, 'next': next, 'author': author, })

@csrf_exempt

def customer03_edit(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    if username:

        user = User.objects.filter(username=username).get()
        oldboard01 = Customer03.objects.get(id=pk)

        total = Customer03.objects.all().count()
        page = total // 20
        page = page + 1

        if oldboard01.user_id == user.id :
            return render(request, '07_customer03_edit.html', {'oldboard01': oldboard01, 'username': username, 'page': page, })
        else:
            return render(request, '07_customer03_different.html', {'username': username, })
    return render(request, '07_customer03_mustlogin.html', {'username':username, 'page': page, })

def customer03_edit_db(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

        content = request.POST['content']
        title = request.POST['title']

        Customer03.objects.filter(id=pk).update(content=content, title=title)

        return render(request, '07_customer03_edit_db.html', {'pk': pk, 'username': username, })

def customer03_delete(request, pk):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    delete02 = Customer03.objects.get(id=pk)
    delete02.delete()
    total = Customer03.objects.all().count()
    page = total // 20
    page = page + 1

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

    # board_list = Contacts.objects.raw('select * from Contacts where content like %s', searchStr)

    if searchCount == 0:
        msg = "검색 결과가 없습니다."
        return render_to_response('07_customer03_search03list.html', {'searchStr':searchStr, 'username':username,
        'searchCount': searchCount, 'searchAll': searchAll, 'msg': msg, })
    return render_to_response('07_customer03_search03list.html', {'searchAll': searchAll, 'searchStr':searchStr, 'username':username, })

def customer03_complete(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    return render(request, '07_customer03_complete.html', {'username': username, })

def customer03_different(request):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    total = Customer03.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '07_customer03_different.html', {'username': username, 'page': page, })

def customer03_deleteconfirm(request, pk):
    try:
        username = request.session["username"]
    except KeyError:
        username = None

    pk = pk

    if username:
        user = User.objects.filter(username=username).get()
        delete02 = Customer03.objects.get(id=pk)

        if delete02.user_id == user.id :
            total = Customer03.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '07_customer03_deleteconfirm.html', {'page': page, 'username': username, 'pk': pk, })
        else:
            total = Customer03.objects.all().count()
            page = total // 20
            page = page + 1

            return render(request, '07_customer03_different.html', {'username': username, 'page': page, 'pk': pk, })

    total = Customer03.objects.all().count()
    page = total // 20
    page = page + 1

    return render(request, '07_customer03_mustlogin.html', {'username': username, 'pk':pk, 'page': page, })

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

    return render(request, '07_customer04.html', {'customer': customer, 'username': username })

def customer04_write(request):

    try:
        username = request.session["username"]
    except KeyError:
        username = None

    form_class = Customer04Form
    form = form_class(request.POST or None)

    total = Customer04.objects.all().count()
    page = total // 20
    page = page + 1

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            total = Customer04.objects.all().count()
            page = total // 20
            page = page + 1
            customer_list = Customer04.objects.all().order_by('-created_at')
            paginator = Paginator(customer_list, 20)
            page = request.GET.get('page', 1)
            try:
                customer = paginator.page(page)
            except PageNotAnInteger:
                customer = paginator.page(1)
            except EmptyPage:
                customer = paginator.page(paginator.num_pages)
            return redirect('customer070401')
        else:
            form = Customer04Form()
    return render(request, '07_customer04_write.html', {'form':form, 'username': username, 'page': page, })

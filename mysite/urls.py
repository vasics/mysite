"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from start.views import index
from django.conf import settings
from login.views import choice, login_form, terms, register, success, check, logout, logout_process
from introduction.views import company0201, company0202, company0203, company0204
from finance.views import finance0301, finance0302, finance030301, finance030302, finance030303, finance030304
from finance.views import finance030305, finance030306, finance030401, finance030501, finance030502
from knowledge.views import knowledge040101, board01_detail, board01_edit, board01_delete, board01_write, board01_edit_db
from knowledge.views import knowledge040201, knowledge040301, knowledge040401, knowledge040501, knowledge040601
from knowledge.views import board02_detail, board02_edit, board02_delete, board02_write, board02_edit_db
from knowledge.views import search01list, board01_complete, board01_different, board01_deleteconfirm
from knowledge.views import search02list, board02_complete, board02_different, board02_deleteconfirm
from knowledge.views import board03_detail, board03_edit, board03_delete, board03_write, board03_edit_db
from knowledge.views import search03list, board03_complete, board03_different, board03_deleteconfirm
from knowledge.views import board04_detail, board04_edit, board04_delete, board04_write, board04_edit_db
from knowledge.views import search04list, board04_complete, board04_different, board04_deleteconfirm
from knowledge.views import board05_detail, board05_edit, board05_delete, board05_write, board05_edit_db
from knowledge.views import search05list, board05_complete, board05_different, board05_deleteconfirm
from knowledge.views import board06_detail, board06_edit, board06_delete, board06_write, board06_edit_db, board06_deleteconfirm2
from knowledge.views import search06list, board06_complete, board06_different, board06_deleteconfirm1, board06_editconfirm
from knowledge.views import board06_answer, board06_answeredit, board06_answerdelete, board06_answerdeletecon

from counsel.views import counsel050101, counsel050201, counsel050202
from counsel.views import c01_write, c01_detail, c01_editpw, c01_deletepw, c01_edit, c01_edit_db, c01_auth
from counsel.views import c01_delete, c01_delete_db

from customer.views import customer070101, customer070201, customer070301, customer070401
from customer.views import customer01_detail, customer01_edit, customer01_delete, customer01_write, customer01_edit_db
from customer.views import customer01_search01list, customer01_complete, customer01_different, customer01_deleteconfirm
from customer.views import customer02_detail, customer02_edit, customer02_delete, customer02_write, customer02_edit_db
from customer.views import customer02_search02list, customer02_complete, customer02_different, customer02_deleteconfirm
from customer.views import customer03_detail, customer03_edit, customer03_delete, customer03_write, customer03_edit_db
from customer.views import customer03_search03list, customer03_complete, customer03_different, customer03_deleteconfirm


from mall.views import mall0601
from english.views import english
from mypage.views import mypage



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index'),

    url(r'^login/choice/$', choice, name='choice'),
    url(r'^login/$', login_form, name='login_form'),
    url(r'^login/terms/$', terms, name='terms'),
    url(r'^login/register/$', register, name='register'),
    url(r'^login/success/$', success, name='success'),
    url(r'^login/check/$', check, name='check'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout/process/$', logout_process, name='logout_process'),

    url(r'^introduction/0201/$', company0201, name='company0201'),
    url(r'^introduction/0202/$', company0202, name='company0202'),
    url(r'^introduction/0203/$', company0203, name='company0203'),
    url(r'^introduction/0204/$', company0204, name='company0204'),

    url(r'^finance/0301/$', finance0301, name='finance0301'),
    url(r'^finance/0302/$', finance0302, name='finance0302'),
    url(r'^finance/030301/$', finance030301, name='finance030301'),
    url(r'^finance/030302/$', finance030302, name='finance030302'),
    url(r'^finance/030303/$', finance030303, name='finance030303'),
    url(r'^finance/030304/$', finance030304, name='finance030304'),
    url(r'^finance/030305/$', finance030305, name='finance030305'),
    url(r'^finance/030306/$', finance030306, name='finance030306'),
    url(r'^finance/030401/$', finance030401, name='finance030401'),
    url(r'^finance/030501/$', finance030501, name='finance030501'),
    url(r'^finance/030502/$', finance030502, name='finance030502'),

    url(r'^knowledge/01/$', knowledge040101, name='knowledge040101'),
    url(r'^knowledge/01/(?P<pk>\d+)/$', board01_detail, name='board01_detail'),
    url(r'^knowledge/01/board01_write/$', board01_write, name='board01_write'),
    url(r'^knowledge/01/(?P<pk>\d+)/board01_edit/$', board01_edit, name='board01_edit'),
    url(r'^knowledge/01/(?P<pk>\d+)/board01_delete/$', board01_delete, name='board01_delete'),
    url(r'^knowledge/01/(?P<pk>\d+)/board01_edit_db/$', board01_edit_db, name='board01_edit_db'),
    url(r'^knowledge/01/search01list', search01list, name='search01list'),
    url(r'^knowledge/01/complete/$', board01_complete, name='board01_complete'),
    url(r'^knowledge/01/different/$', board01_different, name='board01_different'),
    url(r'^knowledge/01/(?P<pk>\d+)/board01_deleteconfirm/$', board01_deleteconfirm, name='board01_deleteconfirm'),


    url(r'^knowledge/02/$', knowledge040201, name='knowledge040201'),
    url(r'^knowledge/02/(?P<pk>\d+)/$', board02_detail, name='board02_detail'),
    url(r'^knowledge/02/board02_write/$', board02_write, name='board02_write'),
    url(r'^knowledge/02/(?P<pk>\d+)/board02_edit/$', board02_edit, name='board02_edit'),
    url(r'^knowledge/02/(?P<pk>\d+)/board02_delete/$', board02_delete, name='board02_delete'),
    url(r'^knowledge/02/(?P<pk>\d+)/board02_edit_db/$', board02_edit_db, name='board02_edit_db'),
    url(r'^knowledge/02/search02list', search02list, name='search02list'),
    url(r'^knowledge/02/complete/$', board02_complete, name='board02_complete'),
    url(r'^knowledge/02/different/$', board02_different, name='board02_different'),
    url(r'^knowledge/02/(?P<pk>\d+)/board02_deleteconfirm/$', board02_deleteconfirm, name='board02_deleteconfirm'),

    url(r'^knowledge/03/$', knowledge040301, name='knowledge040301'),
    url(r'^knowledge/03/(?P<pk>\d+)/$', board03_detail, name='board03_detail'),
    url(r'^knowledge/03/board03_write/$', board03_write, name='board03_write'),
    url(r'^knowledge/03/(?P<pk>\d+)/board03_edit/$', board03_edit, name='board03_edit'),
    url(r'^knowledge/03/(?P<pk>\d+)/board03_delete/$', board03_delete, name='board03_delete'),
    url(r'^knowledge/03/(?P<pk>\d+)/board03_edit_db/$', board03_edit_db, name='board03_edit_db'),
    url(r'^knowledge/03/search03list', search03list, name='search03list'),
    url(r'^knowledge/03/complete/$', board03_complete, name='board03_complete'),
    url(r'^knowledge/03/different/$', board03_different, name='board03_different'),
    url(r'^knowledge/03/(?P<pk>\d+)/board03_deleteconfirm/$', board03_deleteconfirm, name='board03_deleteconfirm'),

    url(r'^knowledge/04/$', knowledge040401, name='knowledge040401'),
    url(r'^knowledge/04/(?P<pk>\d+)/$', board04_detail, name='board04_detail'),
    url(r'^knowledge/04/board04_write/$', board04_write, name='board04_write'),
    url(r'^knowledge/04/(?P<pk>\d+)/board04_edit/$', board04_edit, name='board04_edit'),
    url(r'^knowledge/04/(?P<pk>\d+)/board04_delete/$', board04_delete, name='board04_delete'),
    url(r'^knowledge/04/(?P<pk>\d+)/board04_edit_db/$', board04_edit_db, name='board04_edit_db'),
    url(r'^knowledge/04/search04list', search04list, name='search04list'),
    url(r'^knowledge/04/complete/$', board04_complete, name='board04_complete'),
    url(r'^knowledge/04/different/$', board04_different, name='board04_different'),
    url(r'^knowledge/04/(?P<pk>\d+)/board04_deleteconfirm/$', board04_deleteconfirm, name='board04_deleteconfirm'),

    url(r'^knowledge/05/$', knowledge040501, name='knowledge040501'),
    url(r'^knowledge/05/(?P<pk>\d+)/$', board05_detail, name='board05_detail'),
    url(r'^knowledge/05/board05_write/$', board05_write, name='board05_write'),
    url(r'^knowledge/05/(?P<pk>\d+)/board05_edit/$', board05_edit, name='board05_edit'),
    url(r'^knowledge/05/(?P<pk>\d+)/board05_delete/$', board05_delete, name='board05_delete'),
    url(r'^knowledge/05/(?P<pk>\d+)/board05_edit_db/$', board05_edit_db, name='board05_edit_db'),
    url(r'^knowledge/05/search05list', search05list, name='search05list'),
    url(r'^knowledge/05/complete/$', board05_complete, name='board05_complete'),
    url(r'^knowledge/05/different/$', board05_different, name='board05_different'),
    url(r'^knowledge/05/(?P<pk>\d+)/board05_deleteconfirm/$', board05_deleteconfirm, name='board05_deleteconfirm'),

    url(r'^knowledge/06/$', knowledge040601, name='knowledge040601'),
    url(r'^knowledge/06/(?P<pk>\d+)/$', board06_detail, name='board06_detail'),
    url(r'^knowledge/06/board06_write/$', board06_write, name='board06_write'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_edit/$', board06_edit, name='board06_edit'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_delete/$', board06_delete, name='board06_delete'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_edit_db/$', board06_edit_db, name='board06_edit_db'),
    url(r'^knowledge/06/search06list', search06list, name='search06list'),
    url(r'^knowledge/06/complete/$', board06_complete, name='board06_complete'),
    url(r'^knowledge/06/different/$', board06_different, name='board06_different'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_deleteconfirm1/$', board06_deleteconfirm1, name='board06_deleteconfirm1'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_editconfirm/$', board06_editconfirm, name='board06_editconfirm'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_deleteconfirm2/$', board06_deleteconfirm2, name='board06_deleteconfirm2'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_answer/$', board06_answer, name='board06_answer'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_answeredit/$', board06_answeredit, name='board06_answeredit'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_answerdeletecon/$', board06_answerdeletecon, name='board06_answerdeletecon'),
    url(r'^knowledge/06/(?P<pk>\d+)/board06_answerdelete/$', board06_answerdelete, name='board06_answerdelete'),

    url(r'^counsel/01/$', counsel050101, name='counsel050101'),
    url(r'^counsel/01/c01_write/$', c01_write, name='c01_write'),
    url(r'^counsel/01/(?P<pk>\d+)/$', c01_detail, name='c01_detail'),
    url(r'^counsel/01/(?P<pk>\d+)/editpw/$', c01_editpw, name='c01_editpw'),
    url(r'^counsel/01/(?P<pk>\d+)/deletepw/$', c01_deletepw, name='c01_deletepw'),
    url(r'^counsel/01/(?P<pk>\d+)/edit/$', c01_edit, name='c01_edit'),
    url(r'^counsel/01/(?P<pk>\d+)/edit_db/$', c01_edit_db, name='c01_edit_db'),
    url(r'^counsel/01/(?P<pk>\d+)/auth/$', c01_auth, name='c01_auth'),
    url(r'^counsel/01/(?P<pk>\d+)/delete/$', c01_delete, name='c01_delete'),
    url(r'^counsel/01/(?P<pk>\d+)/delete_db/$', c01_delete_db, name='c01_delete_db'),


    url(r'^counsel/0201/', counsel050201, name='counsel050201'),
    url(r'^counsel/0202/(?P<pk>\d+)/', counsel050202, name='counsel050202'),

    url(r'^mall/01/$', mall0601, name='mall0601'),

    url(r'^customer/01/$', customer070101, name='customer070101'),
    url(r'^customer/01/(?P<pk>\d+)/$', customer01_detail, name='customer01_detail'),
    url(r'^customer/01/customer01_write/$', customer01_write, name='customer01_write'),
    url(r'^customer/01/(?P<pk>\d+)/customer01_edit/$', customer01_edit, name='customer01_edit'),
    url(r'^customer/01/(?P<pk>\d+)/customer01_delete/$', customer01_delete, name='customer01_delete'),
    url(r'^customer/01/(?P<pk>\d+)/customer01_edit_db/$', customer01_edit_db, name='customer01_edit_db'),
    url(r'^customer/01/search01list', customer01_search01list, name='customer01_search01list'),
    url(r'^customer/01/complete/$', customer01_complete, name='customer01_complete'),
    url(r'^customer/01/different/$', customer01_different, name='customer01_different'),
    url(r'^customer/01/(?P<pk>\d+)/customer01_deleteconfirm/$', customer01_deleteconfirm, name='customer01_deleteconfirm'),

    url(r'^customer/02/$', customer070201, name='customer070201'),
    url(r'^customer/02/(?P<pk>\d+)/$', customer02_detail, name='customer02_detail'),
    url(r'^customer/02/customer02_write/$', customer02_write, name='customer02_write'),
    url(r'^customer/02/(?P<pk>\d+)/customer02_edit/$', customer02_edit, name='customer02_edit'),
    url(r'^customer/02/(?P<pk>\d+)/customer02_delete/$', customer02_delete, name='customer02_delete'),
    url(r'^customer/02/(?P<pk>\d+)/customer02_edit_db/$', customer02_edit_db, name='customer02_edit_db'),
    url(r'^customer/02/search02list', customer02_search02list, name='customer02_search02list'),
    url(r'^customer/02/complete/$', customer02_complete, name='customer02_complete'),
    url(r'^customer/02/different/$', customer02_different, name='customer02_different'),
    url(r'^customer/02/(?P<pk>\d+)/customer02_deleteconfirm/$', customer02_deleteconfirm, name='customer02_deleteconfirm'),

    url(r'^customer/03/$', customer070301, name='customer070301'),
    url(r'^customer/03/(?P<pk>\d+)/$', customer03_detail, name='customer03_detail'),
    url(r'^customer/03/customer03_write/$', customer03_write, name='customer03_write'),
    url(r'^customer/03/(?P<pk>\d+)/customer03_edit/$', customer03_edit, name='customer03_edit'),
    url(r'^customer/03/(?P<pk>\d+)/customer03_delete/$', customer03_delete, name='customer03_delete'),
    url(r'^customer/03/(?P<pk>\d+)/customer03_edit_db/$', customer03_edit_db, name='customer03_edit_db'),
    url(r'^customer/03/search03list', customer03_search03list, name='customer03_search03list'),
    url(r'^customer/03/complete/$', customer03_complete, name='customer03_complete'),
    url(r'^customer/03/different/$', customer03_different, name='customer03_different'),
    url(r'^customer/03/(?P<pk>\d+)/customer03_deleteconfirm/$', customer03_deleteconfirm,
        name='customer03_deleteconfirm'),

    url(r'^customer/0401/$', customer070401, name='customer070401'),

    url(r'^english/$', english, name='english'),
    url(r'^mypage/$', mypage, name='mypage'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
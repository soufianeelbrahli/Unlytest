from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from .views import ( MessageListView,
                     MessageDetailView,
                     MessageCreateView,
                     MessageUpdateView,
                     MessageDeleteView )

from django.contrib.auth.views import ( login, logout,
 										password_reset, password_reset_done,
										password_reset_confirm, password_reset_complete )
urlpatterns = [
    url(r'^login/$',login,{'template_name':'Unlyacc/login.html'}),
    url(r'^profile/$',views.view_profile, name='view_profile'),
	url(r'^home/$',views.home),
	url(r'^logout/$',logout,{'template_name':'Unlyacc/logout.html'}),
	url(r'^register/$',views.register,name='register'),
	url(r'^Edit/$',views.edit_profile,name='edit_profile'),
	url(r'^change-password/$',views.change_password,name='change_password'),
	url(r'^reset-password/$',password_reset,name='reset_password'),
	url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name='password_reset_confirm'),
	url(r'^reset-password/complete/$',password_reset_complete,name='password_reset_complete'),
    url(r'^messages/$',views.view_messages,name='view_messages'),
    url(r'^messages/new/$',login_required(MessageCreateView.as_view()),name='message-create'),
    url(r'^messages/(?P<pk>\d+)/$',MessageDetailView.as_view(),name='message-detail'),
    url(r'^messages/(?P<pk>\d+)/update/$',login_required(MessageUpdateView.as_view()),name='message-update'),
    url(r'^messages/(?P<pk>\d+)/delete/$',login_required(MessageDeleteView.as_view()),name='message-delete')
]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse, redirect
from Unlyacc.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from Unlyacc.models import Message
from django.views.generic import (
								ListView,
							 	DetailView,
								CreateView,
								UpdateView,
								DeleteView
							)
# Create your views here.

def home(request):
	adherents=['Soufiane','Anas','Ayoub','Oussama','Amine']
	args={'id_adherent':1,'Login':'Soufiane','Adherents':adherents}
	return render(request,'Unlyacc/home.html',args)

def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('/Unlyacc/profile')
		else :
			return redirect('/Unlyacc/register')
	else :
		form=RegistrationForm()
		args={'form': form}
		return render(request,'Unlyacc/reg_form.html',args)

def view_profile(request):
	if request.user.is_authenticated():
		args = {'user': request.user}
		return render(request,'Unlyacc/profile.html',args)
	else :
		return redirect('/Unlyacc/login')

def edit_profile(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form=EditProfileForm(request.POST, instance=request.user)

			if form.is_valid():
				form.save()
				return redirect('/Unlyacc/profile')
		else:
			form=EditProfileForm(instance=request.user)
			args={'form': form}
			return render(request, 'Unlyacc/edit_profile.html',args)
	else :
		return redirect('/Unlyacc/login')

def change_password(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form=PasswordChangeForm(data=request.POST, user=request.user)

			if form.is_valid():
				form.save()
				print 'ok'
				update_session_auth_hash(request,form.user)
				return redirect('/Unlyacc/profile')
			else :
				return redirect('/Unlyacc/change-password')
		else:
			form=PasswordChangeForm(user=request.user)
			args={'form': form}
			return render(request, 'Unlyacc/change_password.html',args)
	else:
		return redirect('/Unlyacc/login')

def view_messages(request):
	if request.user.is_authenticated():
		if request.user.is_staff==True:
			args={
				'messages':Message.objects.all()
			}
			return render(request,'Unlyacc/messages.html',args)
		else :
			args={
				'messages':Message.objects.filter(author__id=request.user.id)
			}
			return render(request,'Unlyacc/messages.html',args)
	else :
		return redirect('/Unlyacc/login')
class MessageListView(ListView):
	model = Message
	template_name='Unlyacc/messages.html'
	context_object_name='messages'
	ordering=['-date_posted']

class MessageDetailView(DetailView):
	model = Message

class MessageCreateView(CreateView):
		model = Message
		fields=['title','content']

		def form_valid(self,form):
			form.instance.author = self.request.user
			return super(MessageCreateView,self).form_valid(form)

class MessageUpdateView(UpdateView):
		model = Message
		fields=['title','content']

		def form_valid(self,form):
			form.instance.author = self.request.user
			return super(MessageUpdateView,self).form_valid(form)

class MessageDeleteView(DeleteView):
	model = Message
	success_url='/Unlyacc/messages'

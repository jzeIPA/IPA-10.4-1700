from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from benutzeraccounts.models import Profile
from benutzeraccounts.forms import UserForm, ProfileForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.db import transaction, models

def profile(request, pk=None):
    if pk:   #pk = id  pk ist unabhaengiger vom eigentlichen Primaerschluesselfeld, d. h. man muss sich nicht darum kuemmern, ob das Primaerschluesselfeld "id" oder "object_id" oder was auch immer heisst.
        user = User.object.get(pk=pk)
    else:
        user = request.user
    cont = {'user': user}
    return render(request, ('benutzeraccounts/profile.html'), cont)

@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)                   #Instanz zu UserModel ueber forms
        profile_form = ProfileForm(request.POST, instance=request.user.profile)     #Instanz zu ProfileModel ueber forms
        if user_form.is_valid() and profile_form.is_valid():                        #is_valid()-Methode checkt ob Felder gueltig sind
            user_form.save()                                                        #save()-Methode speichert die eingegebenen Daten
            profile_form.save()
            return redirect(reverse('user:profile'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    cont = {'user_form': user_form, 'profile_form':profile_form}
    return render(request, 'benutzeraccounts/edit_profile.html', cont)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user:password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    cont = {'form': form}
    return render(request, 'benutzeraccounts/change_password.html', cont)

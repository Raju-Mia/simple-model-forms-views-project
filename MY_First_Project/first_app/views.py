

from django.shortcuts import render
from first_app.models import *
from django import forms

from first_app import forms

# Create your views here.

def index(request):
    musicium_list = Musicium.objects.order_by("first_name")
    context = { 'musicium': musicium_list, 'name':'this is a index funtion page'}
    return render(request, 'first_app/index.html',context)



def album(request):
    album_list = Album.objects.order_by("name")
    context = { 'album': album_list,}
    return render(request, 'first_app/album.html',context)


def form(request):
    new_form = forms.user_form()
    diction = {'test_form': new_form}

    if request.method == 'POST':
        print("hi")
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']

            diction.update({'user_name':user_name})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            diction.update({'form_submited':"yes"})
            

    return render(request, 'first_app/form.html',context=diction)


def add_form(request):
    new_form = forms.MusicianForm()

    if request.method == "POST":
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit = True)

            # return index(request)

    context = {'new_form': new_form,'value': 'This is new value add'}
    return render(request, 'first_app/add_form.html',context)
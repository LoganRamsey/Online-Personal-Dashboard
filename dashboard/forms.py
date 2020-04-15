from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from dashboard.models import Profile, Todo, Note
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')


class TodoFormText(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task',)


class TodoFormDate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('due',)


class TodoFormTextDate(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task', 'due')

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')

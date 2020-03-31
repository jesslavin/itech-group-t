from django import forms
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from vinyldestination.models import Artist, UserProfile, Review

class ArtistForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the artist's name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide
    class Meta:
        # Provide an association
        model = Artist
        fields = ('name',)


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=50, help_text="Please give your review a title.")
    review = forms.TextInput()
    
    
    # def __init__(self, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     self.fields['author'].initial = self.data

    class Meta:
        model = Review
        fields = ('title', 'review')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

from django import forms
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from vinyldestination.models import Page, Artist, UserProfile, Review

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


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values; we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
# or specify the fields to include (don't include the category field).
# fields = ('title', 'url', 'views')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# class Artist(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     slug = models.SlugField(blank=True)

#     class Meta:
#         permissions = (
#             ('perm_add_artist', 'Can add artist'),
#         )

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Artist, self).save(*args, **kwargs)

#     def __str__(self): # For Python 2, use __unicode__ too
#         return self.name

#     def get_absolute_url(self):
#         return reverse('artist-detail', kwargs={'slug': self.slug})

# class Album(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     artist = models.ForeignKey(Artist)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     slug = models.SlugField(blank=True)

#     class Meta:
#         permissions = (
#             ('perm_add_album', 'Can add album'),
#         )

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Album, self).save(*args, **kwargs)

#     def __str__(self): # For Python 2, use __unicode__ too
#         return self.name

#     def get_absolute_url(self):
#         return reverse('album-detail', kwargs={'slug': self.slug})

class Artist(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name

class Record(models.Model):
    NAME_MAX_LENGTH = 128

    r_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    year = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Record, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Records'

    def __str__(self):
        return self.name

class Shop (models.Model):
    NAME_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 1000

    s_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name

class Review (models.Model):

    TITLE_MAX_LENGTH = 50
    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
#or try to sub get_user_model() with User, if this doesn't work
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return self.title

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

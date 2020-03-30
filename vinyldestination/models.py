from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model
from star_ratings.models import Rating
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
    DESCRIPTION_MAX_LENGTH = 1000
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    slug = models.SlugField(unique=True)
    insta = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/artists', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name


class Record(models.Model):
    NAME_MAX_LENGTH = 128
    GENRE_MAX_LENGTH = 16
    DESCRIPTION_MAX_LENGTH = 1000

    r_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    year = models.IntegerField(default=0, validators=[MaxValueValidator(2020)])
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    a_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=GENRE_MAX_LENGTH)
    image = models.ImageField(upload_to='images/records/', blank=True)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, blank=True)
    ratings = GenericRelation(Rating, related_query_name='records')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.a_id) + "-" + slugify(self.name)
        super(Record, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Records'

    def __str__(self):
        return self.name

class Shop(models.Model):
    NAME_MAX_LENGTH = 128
    DESCRIPTION_MAX_LENGTH = 1000

    s_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/shops/', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name


class Stock(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    stock_item = models.ForeignKey(Record, on_delete=models.CASCADE, blank=True)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.shop) + "-" + slugify(self.stock_item)
        super(Stock, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return self.slug


class Review(models.Model):
    TITLE_MAX_LENGTH = 50

    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    review = models.TextField()

    def set_author(self, author):
        self.author = author 

    def __str__(self):
        return self.title


class List(models.Model):
    LIST_NAME_MAX_LENGTH = 128

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    list_name = models.CharField(max_length=LIST_NAME_MAX_LENGTH)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author) + "-" + slugify(self.list_name) + "-" + slugify(self.record)
        super(List, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Lists'

    def __str__(self):
        return self.list_name


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

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
        verbose_name_plural = 'artists'

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=128, unique=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,)
    year = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    class Meta:
        # permissions = (
        #     ('perm_add_album', 'Can add album'),
        # )
        verbose_name_plural = 'albums'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

    # def get_absolute_url(self):
    #     return reverse('album-detail', kwargs={'slug': self.slug})


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

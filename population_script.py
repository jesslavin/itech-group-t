import os

from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech-group-t.settings')

import django

django.setup()
from vinyldestination.models import Record, Shop


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    records = [
        {'r_id': '0',
         'name': 'record 1',
         'year': '2014',
         'views': '0',
         'likes': '0'},
        {'r_id': '1',
         'name': 'record 2',
         'year': '2014',
         'views': '0',
         'likes': '0'},
        {'r_id': '2',
         'name': 'record 3',
         'year': '2018',
         'views': '0',
         'likes': '0'},
        {'r_id': '3',
         'name': 'record 4',
         'year': '2018',
         'views': '0',
         'likes': '0'},
        {'r_id': '4',
         'name': 'record 5',
         'year': '2014',
         'views': '0',
         'likes': '0'},
        {'r_id': '5',
         'name': 'record 6',
         'year': '2019',
         'views': '0',
         'likes': '0'},
        {'r_id': '6',
         'name': 'record 7',
         'year': '2020',
         'views': '0',
         'likes': '0'},
        {'r_id': '7',
         'name': 'record 8',
         'year': '1974',
         'views': '0',
         'likes': '0'},
        {'r_id': '8',
         'name': 'record 9',
         'year': '2020',
         'views': '0',
         'likes': '0'},
        {'r_id': '9',
         'name': 'record 10',
         'year': '2011',
         'views': '0',
         'likes': '0'}]

    shops = [
        {'s_id': '0',
         'name': 'CableCar Music',
         'description': 'CableCar Music opened its doors in 2010 in to a Glasgow music scene that'
                        ' was loosing many of its great record shops. Passionate to halt the decline,'
                        ' CableCar focused on showcasing the best of the Scottish independent scene,'
                        ' past and present, and cultivating a sense of community between artist and listener.',
         'views': '0',
         'likes': '0'},
        {'s_id': '1',
         'name': 'Roundabout Records',
         'description': 'Home to Glasgow’s finest range of new release Metal, Hardcore and Punk LPs,'
                        ' Roundabout Records is a decades-old city institution. If we don’t have it,'
                        ' you wouldn’t want to be listening to it.',
         'views': '0',
         'likes': '0'},
        {'s_id': '2',
         'name': 'Whiteinch 12inch',
         'description': 'Specialising in dance music, with 12”s sourced from'
                        ' across the globe. Check out our instore white-labels and'
                        ' exclusive pressings of the best work from local producers.',
         'views': '0',
         'likes': '0'},
        {'s_id': '3',
         'name': 'Lost + Found',
         'description': 'At Lost + Found we like to put you back in touch with the records of yesteryear that you '
                        'thought you would never hear again. Covering all genres - but specialising in the music of '
                        'the 60s to the 80s - our collection covers everything from Acid Folk to Zouk, and all points '
                        'in between.',
         'views': '0',
         'likes': '0'}]

    users = [
        {'username': 'Aitcho_TestUser',
         'email': 'aitcho_tu@gmail.com',
         'password': 'a3d4aa2'
         },
        {'username': 'Kenny_TestUser',
         'email': 'kenny_tu@gmail.com',
         'password': '41fhj2vk55'
         },
        {'username': 'Fabia_TestUser',
         'email': 'Fabia_tu@gmail.com',
         'password': 'kwoa209'
         }
    ]

    #    python_pages = [
    #        {'title': 'Official Python Tutorial',
    #         'url': 'http://docs.python.org/3/tutorial/',
    #         'views': 12},
    #        {'title': 'How to Think like a Computer Scientist',
    #         'url': 'http://www.greenteapress.com/thinkpython/',
    #         'views': 12},
    #        {'title': 'Learn Python in 10 Minutes',
    #         'url': 'http://www.korokithakis.net/tutorials/python/',
    #         'views': 12}]

    #    django_pages = [
    #        {'title': 'Official Django Tutorial',
    #         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
    #         'views': 3},
    #        {'title': 'Django Rocks',
    #         'url': 'http://www.djangorocks.com/',
    #         'views': 3},
    #        {'title': 'How to Tango with Django',
    #         'url': 'http://www.tangowithdjango.com/',
    #         'views': 3}]

    #    other_pages = [
    #        {'title': 'Bottle',
    #         'url': 'http://bottlepy.org/docs/dev/',
    #         'views': 3},
    #        {'title': 'Flask',
    #         'url': 'http://flask.pocoo.org',
    #         'views': 3}]

    #    cats = {'Python': {'pages': python_pages,
    #                       'views': 128,
    #                       'likes': 64},
    #            'Django': {'pages': django_pages,
    #                       'views': 64,
    #                       'likes': 32},
    #            'Other Frameworks': {'pages': other_pages,
    #                                 'views': 32,
    #                                 'likes': 16}}

    for r in records:
        add_record(r['r_id'], r['name'], r['year'], r['views'], r['likes'])

    for s in shops:
        add_shop(s['s_id'], s['name'], s['description'], s['views'], r['likes'])

    for u in users:
        add_user(u['username'], u['email'], u['password'])


    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.


#    for cat, cat_data in cats.items():
#        c = add_cat(cat, cat_data['views'], cat_data['likes'])
#        for p in cat_data['pages']:
#            add_page(c, p['title'], p['url'], p['views'])
#
#   # Print out the categories we have added.
#   for c in Category.objects.all():
#       for p in Page.objects.filter(category=c):
#           print(f'- {c}: {p}')

def add_record(r_id, name, year, views, likes):
    r = Record.objects.get_or_create(r_id=r_id, name=name, year=year, views=views, likes=likes)[0]
    return r


def add_shop(s_id, name, description, views, likes):
    s = Shop.objects.get_or_create(s_id=s_id, name=name, description=description, views=views, likes=likes)[0]
    return s

def add_user(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    return u


# def add_page(cat, title, url, views=0):
#    p = Page.objects.get_or_create(category=cat, title=title)[0]
#    p.url = url
#    p.views = views
#    p.save()
#    return p


# def add_cat(name, views=0, likes=0):
#    c = Category.objects.get_or_create(name=name)[0]
#    c.name = name
#    c.views = views
#    c.likes = likes
#    c.save()
#    return c


# Startexecutionhere!
if __name__ == '__main__':
    print('Starting population script...')
    populate()

import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'itech-group-t.settings')

import django
django.setup() 
from vinyldestination.models import Artist, Album

def populate():
	# First, we will create lists of dictionaries containing the pages
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories. 
	# This might seem a little bit confusing, but it allows us to iterate 
	# through each data structure, and add the data to our models.

	nirvana = [
		{'name':'Nevermind',
		 'url':'http://docs.python.org/3/tutorial/',
		 'views':12} ]

	faith_no_more = [
		{'name':'Angel Dust',
		 'url':'https://www.discogs.com/Faith-No-More-Angel-Dust/master/15659', 
		 'views':3},
		{'title':'King For A Day Fool For A Lifetime',
		 'url':'https://www.discogs.com/Faith-No-More-Final-Mixes/master/15723',
		 'views':3} ]

	aphex_twin = [
		{'name':'Analord',
		 'url':'http://bottlepy.org/docs/dev/',
		 'views':3},
		{'name':'Flask',
		 'url':'http://flask.pocoo.org',
		 'views':3} ]

	artists = {'Nivana': {'Albums': nirvana, 
			'views': 128, 
			'likes': 64},
			'Faith No More': {'Albums': faith_no_more,
			'views': 64, 
			'likes': 32},
			'Aphex Twin': {'Albums': aphex_twin,
			'views': 32,
			'likes': 16 } }

	# If you want to add more categories or pages,
	# add them to the dictionaries above.

	# The code below goes through the cats dictionary, then adds each category, 
	# and then adds all the associated pages for that category.
	for cat, cat_data in artists.items():
		c = add_artist(cat,cat_data['views'],cat_data['likes'])
		for p in cat_data['Albums']:
			add_album(c, p['url'], p['views'])

	# Print out the categories we have added.
	for c in Artist.objects.all():
		for p in Album.objects.filter(artist=c):
			print(f'- {c}: {p}')

def add_album(cat,name,url,views=0):
	p = Album.objects.get_or_create(artist=cat, name=name)[0] 
	p.views=views
	p.save()
	return p

def add_artist(name,views=0,likes=0):
	c = Artist.objects.get_or_create(name=name)[0] 
	c.name=name
	c.views=views
	c.likes=likes
	c.save()
	return c

#Startexecutionhere!
if __name__=='__main__':
	print('Starting population script...')
	populate()


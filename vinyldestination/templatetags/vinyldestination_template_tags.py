from django import template
from vinyldestination.models import Artist

register=template.Library()
@register.inclusion_tag('vinyldestination/artists.html')

def get_artist_list(current_artist=None): 
	return {'artists': Artist.objects.all(), 
			'current_artist': current_artist}

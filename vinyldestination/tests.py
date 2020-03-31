from django.test import TestCase
from vinyldestination.models import Artist, Shop, Record, Review
from vinyldestination.forms import ReviewForm
from django.forms import fields as django_fields


# Create your tests here.
class ModelsTests(TestCase):
    """
    Ensures the number of views received for a Category are positive or zero.
    """

    def test_ensure_can_add_artist_without_image(self):
        artist = Artist(name='test', description='test description')
        artist.save()
        print('test1 performed')
        # self.assertEqual((category.views >= 0), True)

    def test_artist_slugify_works(self):
        artist2 = Artist(name='captain test and the tests')
        artist2.save()
        print('test2 performed')
        self.assertEqual(artist2.slug, 'captain-test-and-the-tests')

    # doesn't run test3
    def do_shops_default_to_zero_views_and_likes(self):
        shop = Shop(s_id='1', name='test_shop', description='test description')
        shop.save()
        print('test3 performed')
        self.assertTrue((shop.views == 0))

    def test_shop_slugify_fixes_cases(self):
        shop2 = Artist(name='mYshOp')
        shop2.save()
        print('test4 performed')
        self.assertEqual(shop2.slug, 'myshop')

    # doesn't run test5
    def artist_object_name_is_name(self):
        artist3 = Artist(name='I give my name to the Object', description='test description')
        artist3.save()
        expected_object_name = 'artist3.name'
        print('test5 performed')
        self.assertEqual(expected_object_name, str(artist3))


class FormsTests(TestCase):
    def test_review_form(self):
        review_form = ReviewForm()
        fields = review_form.fields

        desired_fields = {
            'title': django_fields.CharField,
            'review': django_fields.CharField,
            'rating': django_fields.IntegerField
        }

        for desired_field_name in desired_fields:
            desired_field = desired_fields[desired_field_name]
            self.assertTrue(desired_field_name in fields.keys())
            self.assertEqual(desired_field, type(fields[desired_field_name]))


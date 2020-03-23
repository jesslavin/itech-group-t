import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech-group-t.settings')
import django

django.setup()
from vinyldestination.models import Artist, Record, Shop, Review, Page, UserProfile
from django.contrib.auth.models import User


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    records = [
        {'r_id': '0',
         'name': 'Belle and Sebastian - Tigermilk',
         'year': '1996',
         'image': '/images/records/Belle and Sebastian - Tigermilk.jpg',
         'description': "Belle & Sebastian released their first record, Tigermilk, way back in 1996, when indie pop "
                        "was fresh and new and barely a teenager. It's the start of a long songwriting career for "
                        "Stuart Murdoch, who was the only songwriter for the band at this point, and shows off soft, "
                        "delicately made songs that hadn't quite become fanciful and twee yet. Also, the album artwork "
                        "is really something, huh?",
         'genres': 'Alternative, Indie, Pop',
         'views': '0',
         'likes': '0'},
        {'r_id': '1',
         'name': 'The Beths - Future Me Hates Me',
         'year': '2018',
         'image': '/images/records/The Beths - Future Me Hates Me.jpg',
         'description': "Carpark Records (Cloud Nothings, Toro Y Moi) present some fuzzy niceness from Kiwi quartet The"
                        " Beths. Future Me Hates Me is a peppy synthesis of OG twee-grungers like The Lemonheads with "
                        "the shy coyness found in the more recent fare of Yuck and Mitski. Nice harmonies, "
                        "nice melodies, and the fact that the four members all have jazz chops ensures a higher "
                        "level of musicianship that one usually finds on these sort of LPs.",
         'genres': 'Alternative, Indie, Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '2',
         'name': 'Childish Gambino - Because the internet',
         'year': '2013',
         'image': '/images/records/Childish Gambino - Because the internet.jpg',
         'description': "Because the Internet is Childish Gambino's follow up to his debut album Camp which was "
                        "released in 2011 to enormous critical acclaim and established the actor / comedian / writer "
                        "as one of the most challenging, exciting and lyrically interesting talents to emerge in hip "
                        "hop for years. Because the Internet features guest appearances from Chance The Rapper, "
                        "Jhene Aiko and Azealia Banks, with production handled by Gambino himself, Christian Rich, "
                        "Thundercat and Ludwig Goransson among others.",
         'genres': 'Hip-Hop, Rap, Alternative',
         'views': '0',
         'likes': '0'},
        {'r_id': '3',
         'name': 'record 4',
         'year': '2018',
         'image': '/images/records/Courtney Barnett - Tell Me How You Really Feel.jpg',
         'description': "This here offering is Courtney's second album following up {long title}, but also that thing "
                        "she did with Kurt Vile. Here her witty observations are matched with a more serious tone "
                        "capturing more obviously the beauty and warmth in her delivery. She's becoming increasingly "
                        "popular so this will be a big 'un.",
         'genres': 'Alternative, Indie, Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '4',
         'name': 'Diet Cig - Over Easy',
         'year': '2015',
         'image': '/images/records/Diet Cig - Over Easy.jpg',
         'description': "People really enjoy having overblown opinions about the very chill band Diet Cig but they "
                        "will essentially work for you if you like having feelings over decent chord progressions and "
                        "enjoy the bridge built between indie rock and pop punk. Over Easy is five songs, an EP if you "
                        "will, and it was initially released in 2015.",
         'genres': 'Alternative, Indie, Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '5',
         'name': 'Fleetwood Mac - Rumours',
         'year': '1977',
         'image': '/images/records/Fleetwood Mac - Rumours.jpg',
         'description': "Who hasn't heard this before? Well if you haven't then you are in for a treat. It's one of "
                        "the biggest selling albums of all time and the reason why is because it is soft rock hit "
                        "after soft rock hit. Most of these songs were FM radio smashes but the album has a dark "
                        "lyrical undertone as the band's internal dynamic was..um..complicated to say the least.",
         'genres': 'Pop, Rock, Pop Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '6',
         'name': 'Girlpool - Before The World Was Big',
         'year': '2015',
         'image': '/images/records/Girlpool - Before The World Was Big.jpg',
         'description': 'Relief and elation fight each other as Girlpool release their new record Before the World '
                        'Was Big! Thank goodness for that; following on from their EP of spry, confrontational jangle '
                        'pop, they offer more songs about personal growth and identity, intertwined with unbelievable '
                        'melodies that are modestly stated but deeply felt. Phew.',
         'genres': 'Alternative, Indie, Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '7',
         'name': 'Janelle Monae - Dirty Computer',
         'year': '2018',
         'image': '/images/records/Janelle Monae - Dirty Computer.jpg',
         'description': 'Inventive, trend-bending hip-pop soulsmith Janelle Monáe returns with a host of collaborators '
                        'for Dirty Computer. Her first album in five years finds her celebrating the spectra of '
                        'sexuality with rubbery pop - some of which co-written by the late Prince himself. The album '
                        'also hosts the dulcet tones of Brian Wilson, Zoë Kravitz, Grimes and Pharrell Williams.',
         'genres': 'R&B, Soul, Hip-Hop',
         'views': '0',
         'likes': '0'},
        {'r_id': '8',
         'name': 'Kendrick Lamar - DAMN',
         'year': '2017',
         'image': '/images/records/Kendrick Lamar - DAMN.jpg',
         'description': 'The biggest of big deals in 2017: a new full-length album from Kendrick Lamar himself. Damn '
                        'features fairly large guests like Rihanna and, um, U2, but Kendrick doesn’t need any big-name '
                        'support to tell a narrative and craft wonderful beats. This soon-to-be-album-of-the-year '
                        'record is released by Polydor.',
         'genres': 'Hip-Hop, Rap, Alternative',
         'views': '0',
         'likes': '0'},
        {'r_id': '9',
         'name': 'Lizzo - Cuz I Love You',
         'year': '2019',
         'image': '/images/records/Lizzo - Cuz I Love You.jpg',
         'description': 'The debut album from Lizzo, featuring the hit singles "Juice," "Truth Hurts," and a brand new '
                        'version of “Good As Hell” featuring Arianna Grande. When you love yourself, anything becomes '
                        'possible. Channeling boundless self-confidence through a downright earth-quaking voice, '
                        'colorful persona, and undeniable star power, Lizzo struts into the spotlight and steps up '
                        'with a whole lot of sass, spirit, and soul. Embracing her vocal range like never before and '
                        'celebrating herself to the fullest, she speaks her mind, censors nothing, and delivers an '
                        'enviable level of honesty, pure passion, and fresh fire.',
         'genres': 'Pop, Funk, R&B',
         'views': '0',
         'likes': '0'},
        {'r_id': '10',
         'name': 'Lucy Dacus - Historian',
         'year': '2019',
         'image': '/images/records/Lucy Dacus - Historian.jpg',
         'description': 'Indie-rock sensation Lucy Dacus returns with her second album, Historian. She feels as though,'
                        ' she left every bit of herself on the tape, saying everything she wanted to say. A fuller '
                        'sound than debut record, No Burden, has been brought about with mixing input from producer '
                        'John Congleton (He’s worked with just about everyone) and instrumental help from guitarist '
                        'Jacob Blizzard. LP and CD on Matador.',
         'genres': 'Indie, Rock, Singer-Songwriter',
         'views': '0',
         'likes': '10'},
        {'r_id': '11',
         'name': 'Pictish Trail - Thumb World',
         'year': '2020',
         'image': '/images/records/Pictish Trail - Thumb World.jpg',
         'description': 'Scottish producer Johnny Lynch prepares the release of his eighth album as Pictish Trail, '
                        'following four years on from his Scottish Album of the Year-winning Future Echoes. Probably '
                        'his weirdest and most collaborative work yet, Thumb World was forged alongside visual artist '
                        'Swatpaz, a process that had them both imagining that the music was taking place in a retro '
                        '‘80s arcade game world. ',
         'genres': 'Alternative, Indie, Psych-Folk',
         'views': '0',
         'likes': '0'},
        {'r_id': '12',
         'name': 'Porridge Radio - Every Bad',
         'year': '2020',
         'image': '/images/records/Porridge Radio - Every Bad.jpg',
         'description': 'Heavily tipped newcomers Porridge Radio announce their debut studio album Every Bad, following'
                        ' exposure from BBC 6 Music and Radio X among others. Formed around an initial solo project by '
                        'now-lead singer Dana Margolin and her bedroom-composed tracks, their thoughtful, DIY indie '
                        'approach has made them one of the most exciting new bands in Britain.',
         'genres': 'Alternative, Indie, Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '13',
         'name': 'Proclaimers - Sunshine On Leith',
         'year': '1988',
         'image': '/images/records/Proclaimers - Sunshine on Leith.jpg',
         'description': "Sunshine on Leith is the second studio album by Scottish folk rock duo The Proclaimers, "
                        "released in August 1988 though Chrysalis Records. The record spawned four singles, I'm Gonna "
                        "Be (500 Miles), which topped charts in Australia, New Zealand and Iceland, Sunshine on Leith, "
                        "a ballad which has become an anthem for Scottish football club Hibernian F.C., the No. 3 "
                        "Australian hit I'm on My Way, and the Australian-exclusive Then I Met You. The non-single Cap "
                        "in Hand also came to prominence in 2014 with the Scottish Independence referendum.",
         'genres': 'Rock, Folk, Pop',
         'views': '0',
         'likes': '0'},
        {'r_id': '14',
         'name': 'Robyn - Body Talk',
         'year': '2010',
         'image': '/images/records/Robyn - Body Talk.jpg',
         'description': "Melding dancehall with bubblegum pop, heartbroken love songs with hilariously catty weirdness,"
                        " and euphorically catchy melodies with propulsive rhythms, Body Talk-- which combines the"
                        " five-song Body Talk Pt. 3 with, outside of Pt. 1's uncommonly wise Cry When You Get Older, "
                        "the highlights from the first two mini-albums-- is a deeply affecting pop record.",
         'genres': 'Dance, Electropop, Pop',
         'views': '0',
         'likes': '0'},
        {'r_id': '15',
         'name': 'Snail Mail - Lush',
         'year': '2018',
         'image': '/images/records/Snail Mail - Lush.jpg',
         'description': 'Snail Mail’s full-length debut album, Lush, is a debut for the record books — a refreshing '
                        'marvel of songwriting and technical composition, that’s both cohesive and explosive — Her '
                        'voice rises and falls with electricity throughout, spinning with bold excitement and new '
                        'beginnings at every turn. Lush feels at times like an emotional rollercoaster, only fitting '
                        'for Jordan’s explosive, dynamic personality.',
         'genres': 'Indie, Rock, Singer-Songwriter',
         'views': '0',
         'likes': '0'},
        {'r_id': '16',
         'name': 'Soccer Mommy - color theory',
         'year': '2020',
         'image': '/images/records/Soccer Mommy - Color theory.jpg',
         'description': 'color theory by Soccer Mommy (AKA Sophie Allison) is the follow up to 2018’s rather '
                        'marvellous Clean. Here she lays herself bare to listeners through unflinchingly honest lyrics'
                        ' that detail her struggles with mental health and her family. It seems that writing about '
                        'these issues has been a cathartic process for the resilient 22 year-old.',
         'genres': 'Alternative, Indie, Rock',
         'views': '0',
         'likes': '0'},
        {'r_id': '17',
         'name': 'Taylor Swift - 1989',
         'year': '2014',
         'image': '/images/records/Taylor Swift - 1989.jpg',
         'description': "Taylor Swift, seven-time GRAMMY award winner, and the youngest recipient in history of the "
                        "music industry’s highest honor, the GRAMMY Award for Album of the Year. 1989 is a touchstone "
                        "- Taylor's songwriting and sonic evolution surprises us more than ever before. Heavily "
                        "keyboard and beat-driven, the pop sensibilities that have always been the hallmark of Taylor’s"
                        " music now move front and centre on 1989.",
         'genres': 'Pop, Electropop, Dance',
         'views': '0',
         'likes': '0'},
        {'r_id': '18',
         'name': 'Waxahatchee - Ivy Trip',
         'year': '2015',
         'image': '/images/records/Waxahatchee - Ivy Trip.jpg',
         'description': "Katie Crutchfield's southern roots are undeniable. The name of her solo musical project "
                        "Waxahatchee comes from a creek not far from her childhood home in Alabama and seems to "
                        "represent both where she came from and where she's going. Ivy Tripp, drifts confidently from "
                        "its predecessors and brings forth a more informed and powerful recognition of where "
                        "Crutchfield has currently found herself. The lament and grieving for her youth seem to have "
                        "been replaced with control and sheer self-honesty.",
         'genres': 'Alternative, Indie, Folk',
         'views': '0',
         'likes': '0'},
        {'r_id': '19',
         'name': 'Wolf Alice - My Love Is Cool',
         'year': '2015',
         'image': '/images/records/Wolf Alice - My Love Is Cool.jpg',
         'description': 'The debut album from London’s Wolf Alice, My Love Is Cool take further leaps into rock '
                        'territory following their folksy beginnings. Very in tune with the modern strain of motorik '
                        'krautrock whilst retaining an ear for melody, it’s like a diluted Sonic Youth for the kids. '
                        'Out on CD and vinyl double LP from Dirty Hit.',
         'genres': 'Alternative, Indie, Rock',
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
         },
        {'username': 'Brogo_TestUser',
         'email': 'Brogo_tu@gmail.com',
         'password': '832j8a2'
         },
        {'username': 'Charlie_TestUser',
         'email': 'Charlie_tu@gmail.com',
         'password': 'ze6dd23'
         },
        {'username': 'Maisles_TestUser',
         'email': 'Maisles_tu@gmail.com',
         'password': 'le820oe5t'}]

    reviews = {
        'Aitcho_TestUser':
            {'0': {'title': 'Fab!',
                   'review': 'Cannae believe I managed to track down a copy of this! Caught them at '
                             'the Barras in 1999. All downhill since then. For me, not them!',
                   'rating': 5},
             '2': {'title': 'DIMinishing returns',
                   'review': 'Living up to his name, this aint for fans of Camp.',
                   'rating': 2},
             '4': {'title': 'Better with every listen',
                   'review': 'Though there are only two of them, there is just '
                             'more and more to hear everytime I put this on. '
                             'Sound like a choir. On acid. ',
                   'rating': 4},
             '8': {'title': 'Who can stop him?',
                   'review': 'Resisted for as long as I could. I was wrong. '
                             'This is right. ',
                   'rating': 4},
             '12': {'title': 'Showing guitars still have somewhere to go!',
                    'review': 'Picked this up after seeing them at End of the Pier in 2019. My friend had thrown up '
                              'over my shoes, but I could not move away to clean them up. Entranced!',
                    'rating': 4}},
        'Kenny_TestUser':
            {'0': {'title': 'Uncle Tam wisnae wrang',
                   'review': 'Even better on vinyl.',
                   'rating': 4},
             '2': {'title': 'Not a weak tune in the bunch',
                   'review': 'Found out about in on the internet, ironically. Even bought a copy for my sister. She '
                             'hated it though, so now I have two. No complaints.',
                   'rating': 2},
             '3': {'title': 'Weird Pressing?',
                   'review': 'My copy shifts about in pitch all over the place. Still manages to sound better than on '
                             'Spotify. Maybe give it a listen before you put your money down.',
                   'rating': 3},
             '5': {'title': 'No arguments here',
                   'review': 'Classic.', 'rating': 5},
             '7': {'title': 'Better than the purple one',
                   'review': 'Pretty sure Monae is from the future. I hope so anyway, gives me something to look '
                             'forward to!',
                   'rating': 4}},
        'Fabia_TestUser':
            {'2': {'title': 'CGFTW',
                   'review': "Those who only know Donald Glover from Community are really missing out. I've got "
                             "everything the guy has ever put out, but this is probably my favourite of the lot. "
                             "Funny and funky.",
                   'rating': 4},
             '14': {'title': "Girl's got our backs",
                    'review': 'Robyn really takes her time with her records, and it shows best here. Not a single '
                              'beat or string a moment or note out of place. I stuck it on when I first got together '
                              'with my ex, and then again when we broke up. Worked both ways.',
                    'rating': 4},
             '15': {'title': 'Really coming together',
                    'review': "Snail Mail just keeps getting better and better and Lush proves that she's got miles "
                              "to go yet. Great to fall asleep too, gentle, wistful, mysterious. Also just good!",
                    'rating': 4}},
        'Brogo_TestUser':
            {'11': {'title': 'More to this guy than just the label!',
                    'review': "I know so many people who listen to the stuff coming out on Lost Maps, who don't pay "
                              "any attention to Johnny's own stuff. His ear for the bands he has on their carries "
                              "over to his own stuff as well!",
                    'rating': 4},
             '16': {'title': 'So disappointed',
                    'review': "Someone told me I should get this, 'cos it sounds like Best Coast. Someone should tell "
                              "her that too.",
                    'rating': 2}},
        'Maisles_TestUser':
            {'3': {'title': 'Feel real Good.',
                   'review': "Saw someone else on here complaining about the pressing. Mine is fine! Don't know if "
                             "that is good news or bad. She should record with Vile again, can't believe how good "
                             "that would be! Check out Nameless, Faceless. If you don't like that you won't like "
                             "this, and I won't like you!",
                   'rating': 5},
             '9': {'title': 'Can hear this coming down the street from about 3 windows!',
                   'review': "Wish I could get this in Cardi B's hands - Lizzo shows you CAN shout and sing at the "
                             "time.",
                   'rating': 4},
             '17': {'title': 'Bought this for my sis, so I could cover for having a copy in the house!',
                    'review': "Normally wouldn't touch this with yours, but had to admit I loved Style after catching "
                              "myself belting it out in the shower for the whole of last week. I won’t tell you if I "
                              "like any of the others.",
                    'rating': 3},
             '18': {'title': 'Lush',
                    'review': "Caught her live at SXSW in 2017. Can’t believe how well this record nails her sound. "
                              "Or maybe how well she recreates it live haha.",
                    'rating': 4},
             '19': {'title': 'Should be getting more love.',
                    'review': 'Just wish I had a turntable setup for the bath!',
                    'rating': 4}}
    }

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
        add_record(r['r_id'], r['name'], r['year'], r['image'], r['views'], r['likes'])

    for s in shops:
        add_shop(s['s_id'], s['name'], s['description'], s['views'], r['likes'])

    for u in users:
        add_user(u['username'], u['email'], u['password'])
        if u['username'] in reviews.keys():
            for rev in reviews[u['username']].keys():
                record = Record.objects.get(r_id=rev)
                author = User.objects.get(username=u['username'])
                title = reviews[u['username']][rev]['title']
                review = reviews[u['username']][rev]['review']
                rating = reviews[u['username']][rev]['rating']
                add_review(record, author, title, review, rating)

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

def add_record(r_id, name, year, image, views, likes):
    r = Record.objects.get_or_create(r_id=r_id, name=name, year=year, image=image, views=views, likes=likes)[0]
    return r


def add_shop(s_id, name, description, views, likes):
    s = Shop.objects.get_or_create(s_id=s_id, name=name, description=description, views=views, likes=likes)[0]
    return s


def add_user(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    return u


def add_review(record, author, title, review, rating):
    rev = Review.objects.get_or_create(record=record, author=author, title=title, review=review, rating=rating)[0]
    return rev


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

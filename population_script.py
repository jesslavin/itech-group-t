import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'itech-group-t.settings')
import django

django.setup()
from vinyldestination.models import Artist, Record, Shop, Review, Page, UserProfile, Stock, List
from django.contrib.auth.models import User


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    artists = [
        {'name': 'Belle and Sebastian',
         'description': "A band that takes its name from a French children's television series about a boy and his "
                        "dog would almost have to be precious, and to be sure, Belle and Sebastian are precious. But "
                        "precious can be a damning word, and Belle and Sebastian don't have the negative qualities "
                        "that the word connotes: they are private but not insular, and pretty but not wimpy; they "
                        "make gorgeous, delicate melodies sound full-bodied.",
         'image': '/images/artists/Belle and Sebastian.jpg',
         'insta': ''},
        {'name': 'The Beths',
         'description': "New Zealand four-piece The Beths channel their friendship into high-energy guitar pop with a "
                        "smart lyrical bite. 2018 was their breakout year, beginning with signing to Carpark Records "
                        "and Dew Process, before releasing the internationally acclaimed debut album Future Me Hates "
                        "Me, which was heralded as one the stand-out music releases of that year.",
         'image': '/images/artists/The Beths.jpg',
         'insta': ''},
        {'name': 'Childish Gambino',
         'description': "Donald McKinley Glover is an American actor, comedian and musician. As a recording artist, "
                        "he usually performs with the stage name Childish Gambino. While a disk jockey, he performs "
                        "as mcDJ. After several self-released albums and mixtapes, Glover signed to Glassnote Records "
                        "in 2011 as Childish Gambino.",
         'image': '/images/artists/Childish Gambino.jpg',
         'insta': ''},
        {'name': 'Courtney Barnett',
         'description': "Courtney Barnett is an Australian singer/songwriter originally from Sydney, New South Wales. "
                        "Barnett puts a lot of effort into sounding effortless. Her songs are wild and wooly and "
                        "wordy, her lyrics plainspoken and delivered like she’s making them up on the spot.",
         'image': '/images/artists/Courtney Barnett.jpg',
         'insta': ''},
        {'name': 'Diet Cig',
         'description': "Alternative rock duo Diet Cig have a keen sense of fun, even while delivering relatable, "
                        "heartfelt songs about youth, love, and life. Fronted by Alex Luciano with Noah Bowman of "
                        "Earl Boykins (Forged Artifacts) on drums. The two have been playing music together ever "
                        "since Luciano interrupted the set of Bowman's other band for a lighter.",
         'image': '/images/artists/Diet Cig.jpg',
         'insta': ''},
        {'name': 'Fleetwood Mac',
         'description': "Fleetwood Mac are a British blues band formed in 1967. From the band's inception through the "
                        "end of 1974, no incarnation of Fleetwood Mac lasted longer than two years, but all featured "
                        "core members Mick Fleetwood and John McVie. Their two most successful periods were during "
                        "the late 60s British blues boom and from 1975 to 1987, when they went a pop-oriented "
                        "direction with musicians Christine McVie, Lindsey Buckingham, and Stevie Nicks.",
         'image': '/images/artists/Fleetwood Mac.jpg',
         'insta': ''},
        {'name': 'Girlpool',
         'description': "The music Avery Tucker and Harmony Tividad release as Girlpool occupies a transient space. "
                        "Their constant evolution makes it perfectly impossible to articulate exactly where their "
                        "project falls within the contemporary musical canon; this is one of the many reasons "
                        "Girlpool’s music is so captivating.",
         'image': '/images/artists/Girlpool.jpg',
         'insta': ''},
        {'name': 'Janelle Monae',
         'description': "Grammy-nominated singer, songwriter, arranger, producer, and actor Janelle Monáe left her "
                        "mark on 2010s R&B with an energized retro-futuristic sound wrapped in theatrical science "
                        "fiction concepts. After she spent years grinding away in the Atlanta underground, "
                        "Monáe capitalized on support from OutKast and developed into one of the most dynamic artists "
                        "of her time, fusing soul, funk, hip-hop, and new wave with a spirited approach.",
         'image': '/images/artists/Janelle Monae.jpg',
         'insta': ''},
        {'name': 'Kendrick Lamar',
         'description': "Kendrick Lamar (born Kendrick Lamar Duckworth) is a rapper from Compton, California. He is "
                        "also a member of the hip-hop supergroup Black Hippy collective along with members Jay Rock, "
                        "Ab-Soul and Schoolboy Q. His music is largely influenced by the works of 2Pac, Jay-Z, Nas, "
                        "DMX, The Notorious B.I.G., Mos Def, Eazy-E and Eminem.",
         'image': '/images/artists/Kendrick Lamar.jpg',
         'insta': ''},
        {'name': 'Lizzo',
         'description': "Melissa Jefferson, known professionally as Lizzo, is an American rapper and singer. She is a "
                        "founding member of indie hip hop groups The Chalice, Grrrl Prty, The Clerb, Ellypseas, "
                        "and Absynthe. Her debut album, Lizzobangers, was released in 2013. In 2015, she released her "
                        "sophomore album, Big Grrrl Small World.",
         'image': '/images/artists/Lizzo.jpg',
         'insta': ''},
        {'name': 'Lucy Dacus',
         'description': "Lucy Dacus is a singer-songwriter from Richmond, VA. Debut album No Burden was released on "
                        "Friday 26 February 2016 via EggHunt Records. Following her debut, she was signed by indie "
                        "giant Matador Records, who issued her second album Historian on March 2, 2018. After "
                        "releasing a series of singles throughout 2019, her EP 2019 was released on November 8th.",
         'image': '/images/artists/Lucy Dacus.jpg',
         'insta': ''},
        {'name': 'Pictish Trail',
         'description': "The work of Johnny Lynch, aka ‘The Pictish Trail’ is more stirringly subversive stuff from "
                        "the Fence Collective. Lynch writes warm, welcoming tales with tiny keyboard patterns, "
                        "acoustic neo-folk rumblings and all manner of undeniable oddball noises.",
         'image': '/images/artists/Pictish Trail.jpg',
         'insta': ''},
        {'name': 'Porridge Radio',
         'description': "Porridge Radio is a British DIY music band formed in Brighton in 2015. The band is fronted "
                        "by vocalist, songwriter and lead guitarist Dana Margolin, who grew up in the Jewish "
                        "community of North West London. The other members are keyboardist Georgie, bass guitarist "
                        "Maddie and drummer Sam.",
         'image': '/images/artists/Porridge Radio.jpg',
         'insta': ''},
        {'name': 'Proclaimers',
         'description': "The Proclaimers are a Scottish band composed of identical twin brothers, Charlie and Craig "
                        "Reid. They are probably best known for the songs \"Letter from America\", \"I'm On My Way\" "
                        "and \"I'm Gonna Be (500 Miles)\". The band tours extensively throughout Europe and other "
                        "continents. They have released eleven studio albums from 1987 until the present.",
         'image': '/images/artists/Proclaimers.jpg',
         'insta': ''},
        {'name': 'Robyn',
         'description': "Robyn is the stage name of the Swedish pop singer-songwriter Robin Miriam Carlsson. She is "
                        "best known for her critically acclaimed electropop music, her impressive live shows and the "
                        "hits \"With Every Heartbeat\" and \"Dancing On My Own\". In 2011, the single \"Dancing On My "
                        "Own\" was nominated at Grammy Awards for the category Best Dance Recording.",
         'image': '/images/artists/Robyn.jpg',
         'insta': ''},
        {'name': 'Snail Mail',
         'description': "Snail Mail is the American indie rock solo project of guitarist and singer-songwriter "
                        "Lindsey Jordan. In 2015, she started playing her songs live with her band and released the "
                        "EP Habit in 2016. Snail Mail's debut studio album, Lush, was released on June 8, 2018. Snail "
                        "Mail's music is heavily guitar-inspired.",
         'image': '/images/artists/Snail Mail.jpg',
         'insta': ''},
        {'name': 'Soccer Mommy',
         'description': "Sophie Allison, better known by her stage name Soccer Mommy, is an American "
                        "singer-songwriter and musician from Nashville, Tennessee. She has toured with Mitski, "
                        "Jay Som, Slowdive, Frankie Cosmos, Liz Phair, Phoebe Bridgers and others. She recently "
                        "joined Paramore and Foster the People on the first half of their 2018 summer tour.",
         'image': '/images/artists/Soccer Mommy.jpg',
         'insta': ''},
        {'name': 'Taylor Swift',
         'description': "A superstar who managed to completely cross over from country to the mainstream. Other "
                        "singers performed similar moves – notably, Dolly Parton and Willie Nelson but Swift shed her "
                        "country roots like they were a second skin; it was a necessary molting to reveal she was "
                        "perhaps the sharpest, savviest populist singer/songwriter of her generation.",
         'image': '/images/artists/Taylor Swift.jpg',
         'insta': ''},
        {'name': 'Waxahatchee',
         'description': "Waxahatchee is a solo project of songwriter Katie Crutchfield, formed after the breakup of "
                        "P.S. Eliot. She released her first music as Waxahatchee as a split cassette with Chris "
                        "Clavin on Plan-It-X Records. Her bedroom-recorded debut album, American Weekend, "
                        "was released on Don Giovanni Records in 2012.",
         'image': '/images/artists/Waxahatchee.jpg',
         'insta': ''},
        {'name': 'Wolf Alice',
         'description': "Wolf Alice is a rock band from North London, UK formed in 2010. The lineup consists of Ellie "
                        "Rowsell (vocals, guitar), Joff Oddie (guitar), Theo Ellis (bass), and Joel Amey (drums). The "
                        "band began in 2010, initially as a solo project of Ellie Rowsell, with the name taken from a "
                        "short story by Angela Carter.",
         'image': '/images/artists/Wolf Alice.jpg',
         'insta': ''}]

    records = {
        'Belle and Sebastian':
            {'0': {'r_id': '0',
                   'name': 'Tigermilk',
                   'year': '1996',
                   'image': '/images/records/Belle and Sebastian - Tigermilk.jpg',
                   'description': "Belle & Sebastian released their first record, 'Tigermilk', way back in 1996, "
                                  "when indie pop was fresh and new and barely a teenager. It's the start of a long "
                                  "songwriting career for Stuart Murdoch, who was the only songwriter for the band at "
                                  "this point, and shows off soft, delicately made songs that hadn't quite become "
                                  "fanciful and twee yet. Also, the album artwork is really something, huh?",
                   'genre': 'Alternative',
                   'views': '59',
                   'likes': '32'},
             '1': {'r_id': '20',
                   'name': 'Dear Catastrophe Waitress',
                   'year': '2003',
                   'image': '/images/records/Belle and Sebastian - Dear Catastrophe Waitress.jpg',
                   'description': "Belle and Sebastian called upon Trevor Horn to produce Dear Catastrophe Waitress, "
                                  "the band's sixth album. The resulting sound was one that exhibited the strong pop "
                                  "sensabilities that had always been at the band's heart. While some fans recoiled "
                                  "at the move away from the lo-fi sounds of the band's previous work, songs such as "
                                  "'Step into My Office Baby' and 'I'm a Cuckoo', brought a new audience, "
                                  "without betraying their indie-disco cred.",
                   'genre': 'Alternative',
                   'views': '43',
                   'likes': '12'}},
        'The Beths':
            {'0': {'r_id': '1',
                   'name': 'Future Me Hates Me',
                   'year': '2018',
                   'image': '/images/records/The Beths - Future Me Hates Me.jpg',
                   'description': "Carpark Records (Cloud Nothings, Toro Y Moi) present some fuzzy niceness from Kiwi "
                                  "quartet The Beths. Future Me Hates Me is a peppy synthesis of OG twee-grungers "
                                  "like The Lemonheads with the shy coyness found in the more recent fare of Yuck and "
                                  "Mitski. Nice harmonies, nice melodies, and the fact that the four members all have "
                                  "jazz chops ensures a higher level of musicianship that one usually finds on these "
                                  "sort of LPs.",
                   'genre': 'Alternative',
                   'views': '171',
                   'likes': '75'}},
        'Childish Gambino':
            {'0': {'r_id': '2',
                   'name': 'Because the internet',
                   'year': '2013',
                   'image': '/images/records/Childish Gambino - Because the internet.jpg',
                   'description': "Because the Internet is Childish Gambino's follow up to his debut album Camp which "
                                  "was released in 2011 to enormous critical acclaim and established the actor / "
                                  "comedian / writer as one of the most challenging, exciting and lyrically "
                                  "interesting talents to emerge in hip hop for years. 'Because the Internet' "
                                  "features guest appearances from Chance The Rapper, Jhene Aiko and Azealia Banks, "
                                  "with production handled by Gambino himself, Christian Rich, Thundercat and Ludwig "
                                  "Goransson among others.",
                   'genre': 'Hip-Hop',
                   'views': '76',
                   'likes': '35'},
             '1': {'r_id': '21',
                   'name': 'Awaken, My Love',
                   'year': '2016',
                   'image': '/images/records/Childish Gambino - Awaken My Love.jpg',
                   'description': "Donald Glover's 3rd album as Childish Gambino leant heavily into a psych-funk "
                                  "lineage, from the Afro-futurist inspired cover, to the instrumental workouts on "
                                  "many of the tracks. Gambino's dominant role throughout exhibited the record's "
                                  "discontinuity with the p-funk influences, so clear on the arrangements, "
                                  "bringing to mind instead the roles of Prince, or even - whisper - Frank Zappa, "
                                  "as band-leader.  ",
                   'genre': 'Hip-Hop',
                   'views': '189',
                   'likes': '89'}},
        'Courtney Barnett':
            {'0': {'r_id': '22',
                   'name': 'The Double EP: A Sea of Split Peas',
                   'year': '2013',
                   'image': '/images/records/Courtney Barnett - A Sea of Split Peas.jpg',
                   'description': "Bringing together Barnett's first two EPs 'A Sea of Split Peas' drew greater "
                                  "attention to the lyrical prowess the Australian singer/songwriter was already "
                                  "demonstrating, so early in her career. Though not intended to serve as full-length "
                                  "debut, the near hour-long runtime was suggestive of the productivity Barnett has "
                                  "continued to achieve in her recording and touring.",
                   'genre': 'Alternative',
                   'views': '69',
                   'likes': '34'},
             '1': {'r_id': '3',
                   'name': 'Tell Me How You Really Feel',
                   'year': '2018',
                   'image': '/images/records/Courtney Barnett - Tell Me How You Really Feel.jpg',
                   'description': "This here offering is Courtney's second album following up {long title}, but also "
                                  "that thing she did with Kurt Vile. Here her witty observations are matched with a "
                                  "more serious tone capturing more obviously the beauty and warmth in her delivery. "
                                  "She's becoming increasingly popular so this will be a big 'un.",
                   'genre': 'Alternative',
                   'views': '63',
                   'likes': '23'}},
        'Diet Cig':
            {'0': {'r_id': '4',
                   'name': ' Over Easy',
                   'year': '2015',
                   'image': '/images/records/Diet Cig - Over Easy.jpg',
                   'description': "People really enjoy having overblown opinions about the very chill band Diet Cig but"
                                  " they will essentially work for you if you like having feelings over decent chord "
                                  "progressions and enjoy the bridge built between indie rock and pop punk. Over Easy "
                                  "is five songs, an EP if you will, and it was initially released in 2015.",
                   'genre': 'Alternative',
                   'views': '37',
                   'likes': '12'}},
        'Fleetwood Mac':
            {'0': {'r_id': '5',
                   'name': 'Rumours',
                   'year': '1977',
                   'image': '/images/records/Fleetwood Mac - Rumours.jpg',
                   'description': "Who hasn't heard this before? Well if you haven't then you are in for a treat. "
                                  "It's one of the biggest selling albums of all time and the reason why is because "
                                  "it is soft rock hit after soft rock hit. Most of these songs were FM radio smashes "
                                  "but the album has a dark lyrical undertone as the band's internal dynamic "
                                  "was..um..complicated to say the least.",
                   'genre': 'Pop',
                   'views': '90',
                   'likes': '54'},
             '1': {'r_id': '23',
                   'name': 'Tusk',
                   'year': '1979',
                   'image': '/images/records/Fleetwood Mac - Tusk.jpg',
                   'description': "Without the gravitational distortion effected upon Fleetwood Mac's catalogue by "
                                  "the band's previous album 'Rumours', its easy to imagine this record enjoying "
                                  "similar levels of sales and acclaim to its more celebrated predecessor. However its "
                                  "hard to imagine that Tusk would take the form that it does without 'Rumours'"
                                  "looming over proceedings. A sense of exhaustion pervades across the album's 20 "
                                  "tracks. While that may help to explain the lack of comparable commercial success, "
                                  "the sounds of a band struggling to come to terms with success, and each other, have "
                                  "seldom sounded so true to its talent.",
                   'genre': 'Pop',
                   'views': '87',
                   'likes': '64'},
             '2': {'r_id': '24',
                   'name': 'Tango in the Night',
                   'year': '1987',
                   'image': '/images/records/Fleetwood Mac - Tango in the Night.jpg',
                   'description': "A decade on from 'Rumours', 'Tango in the Night' brought to an end the recorded "
                                  "output of this most celebrated line-up of Fleetwood Mac. Lead single 'Big Love' "
                                  "found an unexpected audience in the flourishing European rave scene, indicating "
                                  "both the band's continued success at harmonising melody and rhythm, and the its "
                                  "increasing dislocation within the musical landscape.",
                   'genre': 'Pop',
                   'views': '199',
                   'likes': '89'}
             },
        'Girlpool':
            {'0': {'r_id': '6',
                   'name': 'Before The World Was Big',
                   'year': '2015',
                   'image': '/images/records/Girlpool - Before The World Was Big.jpg',
                   'description': 'Relief and elation fight each other as Girlpool release their new record Before '
                                  'the World Was Big! Thank goodness for that; following on from their EP of spry, '
                                  'confrontational jangle pop, they offer more songs about personal growth and '
                                  'identity, intertwined with unbelievable melodies that are modestly stated but '
                                  'deeply felt. Phew.',
                   'genre': 'Alternative',
                   'views': '77',
                   'likes': '34'}},
        'Janelle Monae':
            {'0': {'r_id': '7',
                   'name': 'Dirty Computer',
                   'year': '2018',
                   'image': '/images/records/Janelle Monae - Dirty Computer.jpg',
                   'description': 'Inventive, trend-bending hip-pop soulsmith Janelle Monáe returns with a host of '
                                  'collaborators for Dirty Computer. Her first album in five years finds her '
                                  'celebrating the spectra of sexuality with rubbery pop - some of which co-written '
                                  'by the late Prince himself. The album also hosts the dulcet tones of Brian Wilson, '
                                  'Zoë Kravitz, Grimes and Pharrell Williams.',
                   'genre': 'R&B',
                   'views': '176',
                   'likes': '67'}},
        'Kendrick Lamar':
            {'0': {'r_id': '8',
                   'name': 'DAMN',
                   'year': '2017',
                   'image': '/images/records/Kendrick Lamar - DAMN.jpg',
                   'description': 'The biggest of big deals in 2017: a new full-length album from Kendrick Lamar '
                                  'himself. Damn features fairly large guests like Rihanna and, um, U2, but Kendrick '
                                  'doesn’t need any big-name support to tell a narrative and craft wonderful beats. '
                                  'This soon-to-be-album-of-the-year record is released by Polydor.',
                   'genre': 'Hip-Hop',
                   'views': '164',
                   'likes': '89'},
             '1': {'r_id': '25',
                   'name': 'To Pimp a Butterfly',
                   'year': '2015',
                   'image': '/images/records/Kendrick Lamar - To Pimp A Butterfly.jpg',
                   'description': "Lamar's third full-length album seemed to pick up plaudits and awards as easily as "
                                  "the Compton-born rapper appeared to reassert West Coast Hip-hop's claim to "
                                  "preeminence, past and present. Such success serves to obscure the technical "
                                  "accomplishment of the record, brought together over five studios and utilising the "
                                  "production talent of KOZ, Pharell Williams, Thundercat and many others.",
                   'genre': 'Hip-Hop',
                   'views': '99',
                   'likes': '45'}
             },
        'Lizzo':
            {'0': {'r_id': '9',
                   'name': 'Cuz I Love You',
                   'year': '2019',
                   'image': '/images/records/Lizzo - Cuz I Love Yo.jpg',
                   'description': 'The debut album from Lizzo, featuring the hit singles "Juice," "Truth Hurts,'
                                  '" and a brand new version of “Good As Hell” featuring Arianna Grande. When you '
                                  'love yourself, anything becomes possible. Channeling boundless self-confidence '
                                  'through a downright earth-quaking voice, colorful persona, and undeniable star '
                                  'power, Lizzo struts into the spotlight and steps up with a whole lot of sass, '
                                  'spirit, and soul. Embracing her vocal range like never before and celebrating '
                                  'herself to the fullest, she speaks her mind, censors nothing, and delivers an '
                                  'enviable level of honesty, pure passion, and fresh fire.',
                   'genre': 'Pop',
                   'views': '86',
                   'likes': '60'}},
        'Lucy Dacus':
            {'0': {'r_id': '10',
                   'name': 'Historian',
                   'year': '2019',
                   'image': '/images/records/Lucy Dacus - Historian.jpg',
                   'description': 'Indie-rock sensation Lucy Dacus returns with her second album, Historian. She '
                                  'feels as though, she left every bit of herself on the tape, saying everything she '
                                  'wanted to say. A fuller sound than debut record, No Burden, has been brought '
                                  'about with mixing input from producer John Congleton (He’s worked with just about '
                                  'everyone) and instrumental help from guitarist Jacob Blizzard. LP and CD on '
                                  'Matador.',
                   'genre': 'Indie',
                   'views': '143',
                   'likes': '89'}},
        'Pictish Trail':
            {'0': {'r_id': '11',
                   'name': 'Thumb World',
                   'year': '2020',
                   'image': '/images/records/Pictish Trail - Thumb World.jpg',
                   'description': 'Scottish producer Johnny Lynch prepares the release of his eighth album as '
                                  'Pictish Trail, following four years on from his Scottish Album of the '
                                  'Year-winning Future Echoes. Probably his weirdest and most collaborative work '
                                  'yet, Thumb World was forged alongside visual artist Swatpaz, a process that had '
                                  'them both imagining that the music was taking place in a retro ‘80s arcade game '
                                  'world.',
                   'genre': 'Alternative',
                   'views': '45',
                   'likes': '20'}},
        'Porridge Radio':
            {'0': {'r_id': '12',
                   'name': 'Every Bad',
                   'year': '2020',
                   'image': '/images/records/Porridge Radio - Every Bad.jpg',
                   'description': 'Heavily tipped newcomers Porridge Radio announce their debut studio album Every '
                                  'Bad, following exposure from BBC 6 Music and Radio X among others. Formed around '
                                  'an initial solo project by now-lead singer Dana Margolin and her bedroom-composed '
                                  'tracks, their thoughtful, DIY indie approach has made them one of the most '
                                  'exciting new bands in Britain. ',
                   'genre': 'Alternative',
                   'views': '135',
                   'likes': '62'}},
        'Proclaimers':
            {'0': {'r_id': '13',
                   'name': 'Sunshine On Leith',
                   'year': '1988',
                   'image': '/images/records/Proclaimers - Sunshine on Leith.jpg',
                   'description': "Sunshine on Leith is the second studio album by Scottish folk rock duo The "
                                  "Proclaimers, released in August 1988 though Chrysalis Records. The record spawned "
                                  "four singles, \"I\'m Gonna Be (500 Miles)\", which topped charts in Australia, "
                                  "New Zealand and Iceland, \"Sunshine on Leith\", a ballad which has become an "
                                  "anthem for Scottish football club Hibernian F.C., the No. 3 Australian hit \"I\'m "
                                  "on My Way\", and the Australian-exclusive \"Then I Met You\". The non-single "
                                  "\"Cap in Hand\" also came to prominence in 2014 with the Scottish Independence "
                                  "referendum.",
                   'genre': 'Rock',
                   'views': '78',
                   'likes': '41'}},
        'Robyn':
            {'0': {'r_id': '14',
                   'name': 'Body Talk',
                   'year': '2010',
                   'image': '/images/records/Robyn - Body Talk.jpg',
                   'description': "Melding dancehall with bubblegum pop, heartbroken love songs with hilariously "
                                  "catty weirdness, and euphorically catchy melodies with propulsive rhythms, "
                                  "Body Talk-- which combines the five-song Body Talk Pt. 3 with, outside of Pt. 1's "
                                  "uncommonly wise \"Cry When You Get Older\", the highlights from the first two "
                                  "mini-albums-- is a deeply affecting pop record.",
                   'genre': 'Dance',
                   'views': '89',
                   'likes': '47'},
             '1': {'r_id': '26',
                   'name': 'Robyn',
                   'year': '2005',
                   'image': '/images/records/Robyn - Robyn.jpg',
                   'description': "Robyn's move to a more dance-pop orientated sound succeeded in bringing widespread "
                                  "attention to the Swedish singer-songwriter on this, her first release on her own "
                                  "Konichiwa Records. Boasting the breakout hit 'With Every Heartbeat', 'Robyn' gave "
                                  "credence to the new dawn of synth-led dance-pop, spawning a host of pale imitators, "
                                  " if only to leave them in the dust on every subsequent outing. ",
                   'genre': 'Pop',
                   'views': '76',
                   'likes': '37'}},
        'Snail Mail':
            {'0': {'r_id': '15',
                   'name': 'Lush',
                   'year': '2018',
                   'image': '/images/records/Snail Mail - Lush.jpg',
                   'description': 'Snail Mail’s full-length debut album, Lush, is a debut for the record books — a '
                                  'refreshing marvel of songwriting and technical composition, that’s both cohesive '
                                  'and explosive — Her voice rises and falls with electricity throughout, '
                                  'spinning with bold excitement and new beginnings at every turn. Lush feels at '
                                  'times like an emotional rollercoaster, only fitting for Jordan’s explosive, '
                                  'dynamic personality.',
                   'genre': 'Indie',
                   'views': '122',
                   'likes': '88'}},
        'Soccer Mommy':
            {'0': {'r_id': '16',
                   'name': 'color theory',
                   'year': '2020',
                   'image': '/images/records/Soccer Mommy - Color theory.jpg',
                   'description': 'color theory by Soccer Mommy (AKA Sophie Allison) is the follow up to 2018’s '
                                  'rather marvellous Clean. Here she lays herself bare to listeners through '
                                  'unflinchingly honest lyrics that detail her struggles with mental health and her '
                                  'family. It seems that writing about these issues has been a cathartic process for '
                                  'the resilient 22 year-old.',
                   'genre': 'Alternative',
                   'views': '123',
                   'likes': '76'},
             '1': {'r_id': '27',
                   'name': 'Clean',
                   'year': '2018',
                   'image': '/images/records/Soccer Mommy - Clean.jpg',
                   'description': "With her official debut album, Sophia Regina Allison added studio polish and the "
                                  "support of a full band to the distinctive melodic sound - by turns plaintive and "
                                  "playful - she had honed on a slew of self-released Bandcamp offerings EPs. 'Clean' "
                                  "demonstrates the ongoing development of an artist already in command of "
                                  "considerable songwriting purpose.",
                   'genre': 'Alternative',
                   'views': '35',
                   'likes': '9'}
             },
        'Taylor Swift':
            {'0': {'r_id': '17',
                   'name': '1989',
                   'year': '2014',
                   'image': '/images/records/Taylor Swift - 1989.jpg',
                   'description': "Taylor Swift, seven-time GRAMMY award winner, and the youngest recipient in "
                                  "history of the music industry’s highest honor, the GRAMMY Award for Album of the "
                                  "Year. '1989' is a touchstone - Taylor's songwriting and sonic evolution surprises "
                                  "us more than ever before. Heavily keyboard and beat-driven, the pop sensibilities "
                                  "that have always been the hallmark of Taylor’s music now move front and centre on "
                                  "'1989'.",
                   'genre': 'Pop',
                   'views': '97',
                   'likes': '58'},
             '1': {'r_id': '28',
                   'name': 'Red',
                   'year': '2012',
                   'image': '/images/records/Taylor Swift - Red.jpg',
                   'description': "'Red' served as Taylor Swift's first full-throated assault on the pop market, "
                                  "bringing the vocal and songwriting charm she had already honed on her three "
                                  "previous, decreasingly country-situated outings. The attempt was disarmingly "
                                  "successful, converting countless new listeners to the brio and chops many had been "
                                  "disinclined to credit on her earlier releases. The release of seven singles from "
                                  "album testifies not only to its strength, and the commercial bent of the "
                                  "Swift-machine, but to the enlarged and enraptured audience Swift had found."
                 ,
                   'genre': 'Pop',
                   'views': '73',
                   'likes': '33'},
             '2': {'r_id': '29',
                   'name': 'Lover',
                   'year': '2019',
                   'image': '/images/records/Taylor Swift - Lover.jpg',
                   'description': "Attempting to rehabilitate Taylor Swift after 2017's poorly received 'reputation', "
                                  "'Lover' served to reassure her fanbase that the previous album was nothing but a "
                                  "stumble for the Swift-juggernaut. While many struggled to hide their titters at the "
                                  "musician's gushing over what they hope is her apex-Englishboy, 'Lover' offered "
                                  "evidence - if it were still required - of Swift's control of her songwriting "
                                  "talent. 'The Man', 'Paper Rings' and 'Soon You'll Get Better' stand as particular "
                                  "highlights across the 18 tracks with which Swift indicates how fertile her "
                                  "marriage of pop and AOR has been.",
                   'genre': 'Pop',
                   'views': '193',
                   'likes': '80'}
             },
        'Waxahatchee':
            {'0': {'r_id': '18',
                   'name': 'Ivy Trip',
                   'year': '2015',
                   'image': '/images/records/Waxahatchee - Ivy Trip.jpg',
                   'description': "Katie Crutchfield's southern roots are undeniable. The name of her solo musical "
                                  "project Waxahatchee comes from a creek not far from her childhood home in Alabama "
                                  "and seems to represent both where she came from and where she's going. Ivy Tripp, "
                                  "drifts confidently from its predecessors and brings forth a more informed and "
                                  "powerful recognition of where Crutchfield has currently found herself. The lament "
                                  "and grieving for her youth seem to have been replaced with control and sheer "
                                  "self-honesty.",
                   'genre': 'Alternative',
                   'views': '77',
                   'likes': '23'}},
        'Wolf Alice':
            {'0': {'r_id': '19',
                   'name': 'My Love Is Cool',
                   'year': '2015',
                   'image': '/images/records/Wolf Alice - My Love Is Cool.jpg',
                   'description': 'The debut album from London’s Wolf Alice, My Love Is Cool take further leaps into '
                                  'rock territory following their folksy beginnings. Very in tune with the modern '
                                  'strain of motorik krautrock whilst retaining an ear for melody, it’s like a '
                                  'diluted Sonic Youth for the kids. Out on CD and vinyl double LP from Dirty Hit.',
                   'genre': 'Alternative',
                   'views': '78',
                   'likes': '42'}}}

    shops = [
        {'s_id': '0',
         'name': 'CableCar Music',
         'image': '/images/shops/CableCar Music.jpg',
         'description': 'CableCar Music opened its doors in 2010 in to a Glasgow music scene that'
                        ' was loosing many of its great record shops. Passionate to halt the decline,'
                        ' CableCar focused on showcasing the best of the Scottish independent scene,'
                        ' past and present, and cultivating a sense of community between artist and listener.',
         'views': '0',
         'likes': '0'},
        {'s_id': '1',
         'name': 'Roundabout Records',
         'image': '/images/shops/Roundabout Records.jpg',
         'description': 'Home to Glasgow’s finest range of new release Metal, Hardcore and Punk LPs,'
                        ' Roundabout Records is a decades-old city institution. If we don’t have it,'
                        ' you wouldn’t want to be listening to it.',
         'views': '0',
         'likes': '0'},
        {'s_id': '2',
         'name': 'Whiteinch 12inch',
         'image': '/images/shops/Whiteinch 12inch.jpg',
         'description': 'Specialising in dance music, with 12”s sourced from'
                        ' across the globe. Check out our instore white-labels and'
                        ' exclusive pressings of the best work from local producers.',
         'views': '0',
         'likes': '0'},
        {'s_id': '3',
         'name': 'Lost + Found',
         'image': '/images/shops/Lost + Found.jpg',
         'description': 'At Lost + Found we like to put you back in touch with the records of yesteryear that you '
                        'thought you would never hear again. Covering all genre - but specialising in the music of '
                        'the 60s to the 80s - our collection covers everything from Acid Folk to Zouk, and all points '
                        'in between.',
         'views': '0',
         'likes': '0'}]

    stock = {
        'CableCar Music':
            {'0': {'stock_item': '0'},
             '1': {'stock_item': '1'},
             '2': {'stock_item': '2'},
             '3': {'stock_item': '3'},
             '5': {'stock_item': '4'},
             '6': {'stock_item': '25'},
             '7': {'stock_item': '26'},
             '8': {'stock_item': '27'},
             '9': {'stock_item': '28'},
             '10': {'stock_item': '29'},
             '11': {'stock_item': '10'},
             '12': {'stock_item': '15'},
             '13': {'stock_item': '20'},
             '14': {'stock_item': '22'},
             '15': {'stock_item': '8'}},
        'Roundabout Records':
            {'0': {'stock_item': '6'},
             '1': {'stock_item': '7'},
             '2': {'stock_item': '8'},
             '3': {'stock_item': '19'},
             '4': {'stock_item': '21'},
             '5': {'stock_item': '23'},
             '6': {'stock_item': '24'},
             '7': {'stock_item': '25'},
             '8': {'stock_item': '28'}},
        'Whiteinch 12inch':
            {'0': {'stock_item': '9'},
             '1': {'stock_item': '10'},
             '2': {'stock_item': '11'},
             '3': {'stock_item': '12'},
             '4': {'stock_item': '1'},
             '5': {'stock_item': '2'}},
        'Lost + Found':
            {'0': {'stock_item': '13'},
             '1': {'stock_item': '14'},
             '2': {'stock_item': '1'},
             '3': {'stock_item': '2'},
             '4': {'stock_item': '3'},
             '5': {'stock_item': '4'},
             '6': {'stock_item': '15'},
             '7': {'stock_item': '16'},
             '8': {'stock_item': '17'},
             '9': {'stock_item': '18'},
             '10': {'stock_item': '19'},
             '11': {'stock_item': '5'}}
    }

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
                   },
             '2': {'title': 'DIMinishing returns',
                   'review': 'Living up to his name, this aint for fans of Camp.',
                   },
             '4': {'title': 'Better with every listen',
                   'review': 'Though there are only two of them, there is just '
                             'more and more to hear everytime I put this on. '
                             'Sound like a choir. On acid. ',
                   },
             '8': {'title': 'Who can stop him?',
                   'review': 'Resisted for as long as I could. I was wrong. '
                             'This is right. ',
                   },
             '12': {'title': 'Showing guitars still have somewhere to go!',
                    'review': 'Picked this up after seeing them at End of the Pier in 2019. My friend had thrown up '
                              'over my shoes, but I could not move away to clean them up. Entranced!',
                    }},
        'Kenny_TestUser':
            {'0': {'title': 'Uncle Tam wisnae wrang',
                   'review': 'Even better on vinyl.',
                   },
             '2': {'title': 'Not a weak tune in the bunch',
                   'review': 'Found out about in on the internet, ironically. Even bought a copy for my sister. She '
                             'hated it though, so now I have two. No complaints.',
                   },
             '3': {'title': 'Weird Pressing?',
                   'review': 'My copy shifts about in pitch all over the place. Still manages to sound better than on '
                             'Spotify. Maybe give it a listen before you put your money down.',
                   },
             '5': {'title': 'No arguments here',
                   'review': 'Classic.', },
             '7': {'title': 'Better than the purple one',
                   'review': 'Pretty sure Monae is from the future. I hope so anyway, gives me something to look '
                             'forward to!',
                   }},
        'Fabia_TestUser':
            {'2': {'title': 'CGFTW',
                   'review': "Those who only know Donald Glover from Community are really missing out. I've got "
                             "everything the guy has ever put out, but this is probably my favourite of the lot. "
                             "Funny and funky.",
                   },
             '14': {'title': "Girl's got our backs",
                    'review': 'Robyn really takes her time with her records, and it shows best here. Not a single '
                              'beat or string a moment or note out of place. I stuck it on when I first got together '
                              'with my ex, and then again when we broke up. Worked both ways.',
                    },
             '15': {'title': 'Really coming together',
                    'review': "Snail Mail just keeps getting better and better and Lush proves that she's got miles "
                              "to go yet. Great to fall asleep too, gentle, wistful, mysterious. Also just good!",
                    }},
        'Brogo_TestUser':
            {'11': {'title': 'More to this guy than just the label!',
                    'review': "I know so many people who listen to the stuff coming out on Lost Maps, who don't pay "
                              "any attention to Johnny's own stuff. His ear for the bands he has on their carries "
                              "over to his own stuff as well!",
                    },
             '16': {'title': 'So disappointed',
                    'review': "Someone told me I should get this, 'cos it sounds like Best Coast. Someone should tell "
                              "her that too.",
                    }},
        'Maisles_TestUser':
            {'3': {'title': 'Feel real Good.',
                   'review': "Saw someone else on here complaining about the pressing. Mine is fine! Don't know if "
                             "that is good news or bad. She should record with Vile again, can't believe how good "
                             "that would be! Check out Nameless, Faceless. If you don't like that you won't like "
                             "this, and I won't like you!",
                   },
             '9': {'title': 'Can hear this coming down the street from about 3 windows!',
                   'review': "Wish I could get this in Cardi B's hands - Lizzo shows you CAN shout and sing at the "
                             "time.",
                   },
             '17': {'title': 'Bought this for my sis, so I could cover for having a copy in the house!',
                    'review': "Normally wouldn't touch this with yours, but had to admit I loved Style after catching "
                              "myself belting it out in the shower for the whole of last week. I won’t tell you if I "
                              "like any of the others.",
                    },
             '18': {'title': 'Lush',
                    'review': "Caught her live at SXSW in 2017. Can’t believe how well this record nails her sound. "
                              "Or maybe how well she recreates it live haha.",
                    },
             '19': {'title': 'Should be getting more love.',
                    'review': 'Just wish I had a turntable setup for the bath!',
                    }},
        'Charlie_TestUser':
            {'20': {'title': 'Pose a question',
                    'review': "These poseurs have been chancing their arm for far to long. Beat it.",
                    },
             '21': {'title': 'Pleasantly surprised',
                    'review': "When someone told me Danny Glover had released a p-funk album, I couldn't believe it. "
                              "And on hearing this, I still can't. ",
                    },
             '22': {'title': 'No extras',
                    'review': "Having been there from the start, I already had 'I've Got a Friend Called Emily Ferris' "
                              "and 'How to Carve a Carrot into a Rose' (that one's signed). I'm glad people have a "
                              "chance to pick these up, but c'mon, where were you?",
                    },
             '23': {'title': 'snaggle-tooth',
                    'review': "'Rumours' went straight to their head, apparently. Presumably up their noses.",
                    },
             '24': {'title': 'Tango in the Night',
                    'review': "Candle in the wind more like.",
                    },
             '25': {'title': 'Slathered',
                    'review': "Like an all-you-can-eat buffet, this seems like a good idea at the time, if that time "
                              "was the early 90s. Or wanted to be.",
                    },
             '26': {'title': 'Still sounds fresh',
                    'review': "Worn in to brain from too many listens. I can switch the amp off and still hear every "
                              "beat.",
                    },
             '27': {'title': '6 (out of 10) Music',
                    'review': "This is a real Soccer Mommy or chips moment.",
                    },
             '28': {'title': 'No Country for Old Men',
                    'review': "So glad she's pivoted to pop.",
                    },
             '29': {'title': 'Should be the theme to IndyRef2.',
                    'review': 'What a fall from grace! Am I the only one who can hear it?',
                    }}
    }

    lists = {
        'Aitcho_TestUser':
            {'0': {'list_name': 'my list',
                   'record': '0'},
             '1': {'list_name': 'my list',
                   'record': '3'},
             '2': {'list_name': 'my list',
                   'record': '6'},
             '3': {'list_name': 'my list',
                   'record': '13'},
             '4': {'list_name': 'my list',
                   'record': '10'},
             '5': {'list_name': 'my list',
                   'record': '19'},
             '6': {'list_name': 'PRESENTS',
                   'record': '21'},
             '7': {'list_name': 'PRESENTS',
                   'record': '25'},
             '8': {'list_name': 'PRESENTS',
                   'record': '26'},
             '9': {'list_name': 'PRESENTS',
                   'record': '28'},
             '10': {'list_name': 'PRESENTS',
                    'record': '29'}},
        'Kenny_TestUser':
            {'0': {'list_name': 'my list',
                   'record': '4'},
             '1': {'list_name': 'my list',
                   'record': '5'},
             '2': {'list_name': 'my list',
                   'record': '15'},
             '3': {'list_name': 'my list',
                   'record': '18'}},
        'Maisles_TestUser':
            {'0': {'list_name': 'my list',
                   'record': '2'},
             '1': {'list_name': 'my list',
                   'record': '1'},
             '2': {'list_name': 'my list',
                   'record': '0'},
             '3': {'list_name': 'my list',
                   'record': '12'},
             '4': {'list_name': 'my list',
                   'record': '11'},
             '5': {'list_name': 'must bring up in conversation',
                   'record': '2'},
             '6': {'list_name': 'must bring up in conversation',
                   'record': '11'},
             '7': {'list_name': 'must bring up in conversation',
                   'record': '0'}},
        'Charlie_TestUser':
            {'0': {'list_name': 'Owned',
                   'record': '15'},
             '1': {'list_name': 'Owned',
                   'record': '9'},
             '2': {'list_name': 'Owned',
                   'record': '4'},
             '3': {'list_name': 'Owned',
                   'record': '2'},
             '4': {'list_name': 'Owned',
                   'record': '10'},
             '5': {'list_name': 'Owned',
                   'record': '7'},
             '6': {'list_name': 'When I get paid...',
                   'record': '8'},
             '7': {'list_name': 'When I get paid...',
                   'record': '19'},
             '8': {'list_name': 'When I get paid...',
                   'record': '5'},
             '9': {'list_name': 'When I get paid...',
                   'record': '14'},
             '10': {'list_name': 'When I get paid...',
                    'record': '16'},
             '11': {'list_name': 'When I get paid...',
                    'record': '13'}}
    }

    for a in artists:
        add_artist(a['name'], a['description'], a['image'], a['insta'])
        if a['name'] in records.keys():
            for r in records[a['name']].keys():
                r_id = records[a['name']][r]['r_id']
                artist = Artist.objects.get(name=a['name'])
                name = records[a['name']][r]['name']
                year = records[a['name']][r]['year']
                image = records[a['name']][r]['image']
                views = records[a['name']][r]['views']
                likes = records[a['name']][r]['likes']
                description = records[a['name']][r]['description']
                genre = records[a['name']][r]['genre']
                add_record(r_id, artist, name, year, image, views, likes, description, genre)

    #    for r in records:
    #        artist = Artist.objects.get(name=r['artist'])
    #        add_record(r['r_id'], artist, r['name'], r['year'], r['image'], r['views'], r['likes'])

    for s in shops:
        add_shop(s['s_id'], s['name'], s['description'], s['views'], s['likes'], s['image'])
        if s['name'] in stock.keys():
            for st in stock[s['name']].keys():
                shop = Shop.objects.get(name=s['name'])
                new_stock = stock[s['name']][st]['stock_item']
                stock_item = Record.objects.get(r_id=new_stock)
                add_stock(shop, stock_item)

    for u in users:
        add_user(u['username'], u['email'], u['password'])
        if u['username'] in reviews.keys():
            for rev in reviews[u['username']].keys():
                record = Record.objects.get(r_id=rev)
                author = User.objects.get(username=u['username'])
                title = reviews[u['username']][rev]['title']
                review = reviews[u['username']][rev]['review']
                add_review(record, author, title, review)
        if u['username'] in lists.keys():
            for li in lists[u['username']].keys():
                author = User.objects.get(username=u['username'])
                list_name = lists[u['username']][li]['list_name']
                new_list_item = lists[u['username']][li]['record']
                record = Record.objects.get(r_id=new_list_item)
                add_list_item(author, list_name, record)

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

def add_artist(name, description, image, insta):
    a = Artist.objects.get_or_create(name=name, description=description, image=image, insta=insta)[0]
    return a


def add_record(r_id, artist, name, year, image, views, likes, description, genre):
    r = Record.objects.get_or_create(r_id=r_id,
                                     a_id=artist, name=name, year=year, image=image, views=views,
                                     likes=likes, description=description, genre=genre)[0]
    return r


def add_shop(s_id, name, description, views, likes, image):
    s = Shop.objects.get_or_create(s_id=s_id, name=name, description=description, views=views,
                                   likes=likes, image=image)[0]
    return s


def add_stock(shop, stock_item):
    st = Stock.objects.get_or_create(shop=shop, stock_item=stock_item)
    return st


def add_user(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    return u


def add_review(record, author, title, review):
    rev = Review.objects.get_or_create(record=record, author=author, title=title, review=review)[0]
    return rev


def add_list_item(author, list_name, record):
    l_i = List.objects.get_or_create(author=author, list_name=list_name, record=record)[0]
    return l_i


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

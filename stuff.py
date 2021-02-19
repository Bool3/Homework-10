from judgement import sim_euclidean, sim_pearson, top_matches
from SONGDB import db, song_tbl
from enum import Enum

# song: {SID: rating, SID: rating}

def get_song_ratings(song, database=db, students_to_avoid=[]):
    """Returns all ratings for a given song except those of students in students_to_avoid:list.
       The order of the ratings is the order in which students appear in the database (in this case, alphabetical)."""
    ratings = {}

    for sID, s_ratings in database.items():
        if sID not in students_to_avoid:

            if song in s_ratings.keys():
                ratings[sID] = s_ratings[song]

            else:
                ratings[sID] = None
                pass

    return ratings

song_key_db = {song: get_song_ratings(song) for song in song_tbl}

assert len(song_key_db) == 47
assert len(song_key_db['15 Step']) == 44
assert song_key_db['Young Dumb and Broke'] == {
    'adeer': 2.0, 'afischl': 5.0, 'ahurwit': None, 'asmetan': 4.0,
    'awelch': 2.0, 'bthai': 4.0, 'cfinn': 1.0, 'cmizrah': 5.0,
    'cmoshre': 4.0, 'dpace': 4.0, 'epaige': 2.0, 'esmith': 3.0,
    'fmeiste': 3.0, 'geidelm': 4.0, 'gsaouaf': 4.0, 'jbeall': 4.0,
    'jfletch': 3.0, 'jleesou': 3.0, 'jliu': 5.0, 'jmandel': 4.0,
    'jparson': 3.0, 'jsarkis': 3.0, 'kmcderm': 5.0, 'kyamada': 5.0,
    'lmcderm': 5.0, 'lrobins': None, 'mchurch': 5.0, 'menayat': 5.0,
    'mgoodma': 4.0, 'mnadel': 4.0, 'namin': 1.0, 'nellis': 5.0,
    'nfighte': 5.0, 'nkim': 3.0, 'nomwami': 5.0, 'nwolf': 2.0,
    'rsuddat': 2.0, 'sfogg': 3.0, 'ssilver': 2.0, 'staylor': 4.0,
    'taldave': 4.0, 'tcatala': 2.0, 'wdepue': 3.0, 'wmaisle': 3.0
    }  # yes, I did find this manually and I regret it
assert song_key_db['Touch-Tone Telephone']['menayat'] == 4.0
assert song_key_db['Campus']['dpace'] == 5.0


def compress_similarities(song, threshold: float, sim_function=sim_euclidean):
    """Reduces top_matches via a threshold on the similarites."""
    matches = top_matches(song, song_key_db, n=0, sim_function=sim_function)
    connections = []

    for s, r in matches:
        if r >= threshold:
            connections.append(s)
    
    return connections


# First I looked at any broad patterns in the similarities (I used Euclidean)
# I found that pretty much everything was very similar to 'Symphone Concertante' and 'Riders on the Storm'
# I removed those songs from the database and resigned them to their own category ('Popular')
# I then chose anchor songs based on which songs I thought best represented a genre
# Then I looked at the songs most similar to the anchors using a threshold on the similarity scores
# If the anchors had too many similar songs in common, I swapped anchors
# I repeated this process until I had multiple anchors that defined spaces and groups that were different enough
# Then I lowered the threshold and started adding songs to the anchor groups, where songs that were more similar went into their respective groups
# If I had some trouble (like if a song wasn't very similar to any of the anchors), I examined songs in particular to see which songs they were most similar to, and assigned them to that group


# establish and remove ignored songs - these are put in the 'popular' category
ignore = ['Symphone Concertante', 'Riders on the Storm', 'Hammer To Fall']

for song in ignore:
    song_key_db.pop(song)

# Carry on My Wayward Son: ROCK
# Circles: BEDROOM POP
# Got it Good: R&B
# Blue Train: JAZZ
# Moonlight Sonata: CLASSICAL
# Sunshine: RAP
# Coast of Carolina: INDIE ROCK

# testing / observation code (I did the assigning of the groups manually)

anchors = ['Circles', 'Carry on My Wayward Son', 'Coast of Carolina', "Blue Train", "Sunshine", "Moonlight Sonata", "Got it Good"]

test = ['15 Step', 'Blue Train', 'Born Under a Bad Sign', 'Broken Bearings', 'Cabin Fever', 'Campus', 'Carolina In My Mind', 'Cayendo', 'Clash', 'Coast of Carolina', 'Coffee Bean', 'Electric Funeral', 'Feeling Good', "For What It's Worth", 'Got it Good', 'Hammer To Fall', 'Higher Ground', "I'll Never Smile Again", 'Kiss', 'Kyoto', 'Ligeiros', 'Magazine', 'Miami 2017 ', 'Moonlight Sonata', 'Pacific Coast Party', 'Pollyana', 'Putty Boy Strut', 'Quarantine Speech', 'Rain On Me', "Rapture's Delight", "Rollin' Stone ", 'Scrubs', 'Space Cowboy', 'Strasbourg/ St. Denis', 'Sunshine', 'Survivor', 'Sweden', 'Time Alone With You', 'Touch-Tone Telephone', 'Treaty', 'Walking On A Dream', "We're Going to Be Friends", 'Young Dumb and Broke']

print("-----------")
for anchor in test:
    if anchor not in ignore:
        print(anchor)

        #print(compress_similarities(anchor, 0)) #107
        print(top_matches(anchor, song_key_db, n=0))

        print("")


wayward_son = ["Rollin' Stone ", "Kiss", "For What It's Worth", "Pacific Coast Party"]
circles = ["Young Dumb and Broke", "Walking On A Dream", "Feeling Good", "We're Going to Be Friends"]
coast_carolina = ["Pollyana", "Cabin Fever", "Magazine", "Miami 2017 ", "Campus", "Kyoto", "Broken Bearings", "Cayendo", "Quarantine Speech", "Carolina In My Mind", "15 Step", "Treaty", "Clash"]
got_good = ["Survivor", "Ligeiros", "Rain On Me", "Coffee Bean", "Scrubs", "Time Alone With You", "Touch-Tone Telephone", "Sweden"]
moonlight = ["I'll Never Smile Again"]
sunshine = ["Rapture's Delight", "Putty Boy Strut"]
blue_train = ["Strasbourg/ St. Denis", "Higher Ground", "Born Under a Bad Sign", "Space Cowboy"]
popular = ['Symphone Concertante', 'Riders on the Storm', 'Hammer To Fall']

# then i found averages

def average(l: list):
    s = 0

    for e in l:
        s += e

    return s / len(l)
        

def find_averages(group):
    ret = []
    for x in group:
        avg_list = []
        for y in group:
            if y != x:
                avg_list.append(sim_euclidean(x, y, song_key_db))
        ret.append(average(avg_list))
    
    return ret


print( find_averages(wayward_son) )
print( average(find_averages(wayward_son)) )

print( find_averages(circles) )
print( average(find_averages(circles)) )

print( find_averages(coast_carolina) )
print( average(find_averages(coast_carolina)) )

print( find_averages(got_good) )
print( average(find_averages(got_good)) )

print( find_averages(sunshine) )
print( average(find_averages(sunshine)) )

print( find_averages(blue_train) )
print( average(find_averages(blue_train)) )

print( find_averages(popular) )
print( average(find_averages(popular)) )

# data in spreadsheet "Homework 10 Results" shared with you via google drive
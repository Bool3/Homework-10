from judgement import sim_euclidean, sim_pearson
from SONGDB import db, song_tbl

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


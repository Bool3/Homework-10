import math


def shared(song_a, song_b, database):
    """Returns a list of the students who've rated both song_a and song_b given a database."""
    db_song_a = database[song_a]
    db_song_b = database[song_b]

    # make sets of the students that have rated each song
    a = set(sID for sID in db_song_a if db_song_a[sID] != None)
    b = set(sID for sID in db_song_b if db_song_b[sID] != None)

    # find and return the intersection of the sets
    shared = list(a.intersection(b))

    return shared


def sim_euclidean(song_a, song_b, database):
    """Returns a similarity score from the euclidean distance between the ratings of two students given a database."""
    both_rated = shared(song_a, song_b, database)
    point_summation = 0

    for sID in both_rated:
        point_summation += abs(database[song_a][sID] - database[song_b][sID]) ** 2
    
    euclidean_distance = math.sqrt(point_summation)

    return 1 / (1 + euclidean_distance)  # this is done because the similarity score should go up as songs are more similar


def sim_pearson(studentID_a, studentID_b, database):
    """Returns a similarity score from the pearson correlation coefficient between the ratings of two students given a database."""
    both_rated = shared(studentID_a, studentID_b, database)
    n = len(both_rated)

    sum_a = 0
    sum_b = 0
    sq_sum_a = 0
    sq_sum_b = 0
    sum_ab = 0

    # find all sums
    for song in both_rated:
        sum_a += database[studentID_a][song]
        sum_b += database[studentID_b][song]
        sum_ab += database[studentID_a][song] * database[studentID_b][song]
        sq_sum_a += database[studentID_a][song] ** 2
        sq_sum_b += database[studentID_b][song] ** 2

    numerator = sum_ab - (sum_a * sum_b) / n

    denominator = math.sqrt((sq_sum_a - sum_a ** 2 / n) * (sq_sum_b - sum_b ** 2 / n))
    
    return numerator / denominator


def top_matches(studentID, database, n=5, sim_function=sim_euclidean):
    """Returns the top n matches using the sim_function for a student given a database."""
    matches = []
    
    # sorting function for .sort() : sort by the similarity score
    def sort_by_sim_score(e):
        return e[1]

    # make a list of the similarity scores between the key student and all other students
    for sID in database:
        if sID != studentID:
            matches.append((sID, sim_function(studentID, sID, database)))  # list of (student ID, similarity score)

    matches.sort(key=sort_by_sim_score, reverse=True)

    # return a list of the top n matches
    return [matches[i] for i in range(n) if i <= len(matches) - 1]
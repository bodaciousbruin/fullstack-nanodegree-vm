#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def executeQuery(query):
    '''connects to database, creates a cursor, executes supplied query
    commits if necessary, disconnects connection'''
    
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)

    if not 'select' in query:
        connection.commit()

    connection.close()
    

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    
    query = '''
    truncate matches
    restart identity
    CASCADE
    '''
    executeQuery(query)


def deletePlayers():
    """Remove all the player records from the database."""
    query = '''
    truncate players
    restart identity
    cascade
    '''
    executeQuery(query)


def countPlayers():
    """Returns the number of players currently registered."""
    query = "select count(*) from players"
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    countResult = cursor.fetchall()
    #print "countResult = " + str(countResult)
    return countResult[0][0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
      
    """
    #sanitize input against javascript injection
    name = bleach.clean(name)
    
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("insert into players (name) values (%s)", (name,))
    connection.commit()
    connection.close()

    


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # this query assumes that the following views have been established:
    # create view played_matches as select players.id, players.name, count(match_outcomes.matchid) as matches from players left join match_outcomes on (players.id = match_outcomes.playerid) group by players.id;

    # create view player_wins as select players.id, players.name, count(match_outcomes.matchid) as wins from players left join match_outcomes on (players.id = match_outcomes.playerid and match_outcomes.outcome = 'winner') group by players.id;
    query = "select player_wins.id, player_wins.name, wins, matches from played_matches, player_wins where player_wins.id = played_matches.id order by wins desc;"
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    standingsResult = cursor.fetchall()
    # print "standingsResult = " + str(standingsResult)
    return standingsResult


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """



-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create table players (
    id serial primary key,
    name text
);

create table matches (
    matchId serial primary key,
    p1Id integer references players (id),
    p2Id integer references players (id)
);

create table match_outcomes (
    matchId integer references matches,
    outcome text,
    playerId integer references players (id)
);

create view played_matches as select players.id, players.name, count(match_outcomes.matchid) as matches from players left join match_outcomes on (players.id = match_outcomes.playerid) group by players.id;

create view player_wins as select players.id, players.name, count(match_outcomes.matchid) as wins from players left join match_outcomes on (players.id = match_outcomes.playerid and match_outcomes.outcome = 'winner') group by players.id;


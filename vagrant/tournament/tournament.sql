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
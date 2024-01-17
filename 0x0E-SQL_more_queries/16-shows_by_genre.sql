-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT ts.title, tg.name
FROM tv_genres AS tg
RIGHT OUTER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
RIGHT OUTER JOIN tv_shows ts ON tsg.show_id = ts.id
ORDER BY ts.title, tg.name;

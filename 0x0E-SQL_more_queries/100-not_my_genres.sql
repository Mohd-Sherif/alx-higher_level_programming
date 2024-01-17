-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT name
FROM tv_genres
WHERE id NOT IN (
	SELECT tg.id
	FROM tv_genres AS tg
	INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
	INNER JOIN tv_shows ts ON tsg.show_id = ts.id
	WHERE ts.title = 'Dexter'
	)
ORDER BY name;

SELECT ad.actor_id, ad.director_id
FROM ActorDirector as ad
GROUP BY ad.actor_id, ad.director_id
HAVING COUNT(ad.director_id) >= 3
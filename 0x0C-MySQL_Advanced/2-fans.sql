-- Rank the country origins of bands and order by the number of fans.
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;

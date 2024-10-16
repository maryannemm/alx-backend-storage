-- Task 3: Old school band
-- This script lists all bands with 'Glam rock' as their main style, ranked by longevity

SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;


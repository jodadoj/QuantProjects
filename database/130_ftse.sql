ALTER TABLE stocks
ADD COLUMN IF NOT EXISTS ftse_100 BOOLEAN;

DROP TABLE IF EXISTS temp_ftse_100_tickers;

CREATE TABLE temp_ftse_100_tickers (
    company_name VARCHAR(50),
    ticker VARCHAR(30),
    sector VARCHAR(50)
);

COPY temp_ftse_100_tickers (company_name, ticker, sector)
FROM 'D:\Programming\Projects\QuantProjects\src\output\ftse_lists\2023-06-20-ftse_100.csv'
DELIMITER ',' CSV;

-- change to todays date at some point

UPDATE stocks
SET ftse_100 = CASE WHEN ticker IN
(SELECT ticker FROM temp_ftse_100_tickers)
AND country = 'United Kingdom'
THEN TRUE ELSE FALSE END;

DROP TABLE temp_ftse_100_tickers;
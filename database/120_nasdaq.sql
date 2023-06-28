ALTER TABLE stocks
ADD COLUMN IF NOT EXISTS nasdaq100 BOOLEAN;

DROP TABLE IF EXISTS temp_nasdaq100_tickers;

CREATE TABLE temp_nasdaq100_tickers (
    company_name VARCHAR(50),
    ticker VARCHAR(30)
);

COPY temp_nasdaq100_tickers (company_name, ticker)
FROM '..\src\output\nasdaq_lists\2023-06-06-nasdaq100.csv'
DELIMITER ',' CSV;

-- change to todays date at some point

UPDATE stocks
SET nasdaq100 = CASE WHEN ticker IN
(SELECT ticker FROM temp_nasdaq100_tickers)
AND country = 'United States';
THEN TRUE ELSE FALSE END;

DROP TABLE temp_nasdaq100_tickers;
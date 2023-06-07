ALTER TABLE stocks
ADD COLUMN IF NOT EXISTS sp500 BOOLEAN;

CREATE TABLE temp_sp500_tickers (
    ticker VARCHAR(30),
    company_name VARCHAR(50),
    date_added VARCHAR(30),
    cik VARCHAR(30)
);

COPY temp_sp500_tickers (ticker, company_name, date_added, cik)
FROM '..\src\output\sp500_lists\2023-06-06-sp500.csv'
DELIMITER ',' CSV;

-- change to todays date at some point

UPDATE stocks
SET sp500 = CASE WHEN ticker IN
(SELECT ticker FROM temp_sp500_tickers)
AND country = 'United States';
THEN TRUE ELSE FALSE END;

DROP TABLE temp_sp500_tickers;
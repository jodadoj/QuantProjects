DROP TABLE stocks IF EXISTS;

CREATE TABLE stocks (
    ticker VARCHAR(10) PRIMARY KEY,
    company_name VARCHAR(255),
    currency CHAR(3),
    exchange VARCHAR(10),
    mic_code VARCHAR(20),
    country VARCHAR(30),
    security_type VARCHAR(50)
);

COPY stocks (
  ticker,
 	company_name,
  currency,
  exchange,
  mic_code,
  country,
  security_type
                  )
FROM '..\download\12data_stocks.csv'
DELIMITER ';' CSV;


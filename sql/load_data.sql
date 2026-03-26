USE ecommerce;

LOAD DATA INFILE '/var/lib/mysql-files/FDS_analysis.csv'
INTO TABLE survey_raw
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
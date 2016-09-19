CREATE DATABASE  twitter_project;

CREATE EXTERNAL TABLE twitter_project.streamed_tweets(id string,tweet STRING, us_district STRING) ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n'
              STORED AS TEXTFILE
              LOCATION '/user/cloudera/twitter';

CREATE EXTERNAL TABLE twitter_project.us_district(district_name STRING,district_code string) ROW FORMAT
              DELIMITED FIELDS TERMINATED BY '\t'
              LINES TERMINATED BY '\n'
              STORED AS TEXTFILE
              LOCATION '/user/cloudera/usdistricts';

CREATE TABLE twitter_project.final_tweets(id string,tweet STRING, us_district STRING);

SELECT	st.id,
	st.tweet,
	usd.
	


drop table if exists inet_mac;
create table inet_mac(
	id integer PRIMARY KEY,
	mac_add macaddr,
	ip inet,
	country varchar(32),
	date date);


CREATE OR REPLACE PROCEDURE genData()
  LANGUAGE plpgsql AS
$proc$
BEGIN
  INSERT INTO inet_mac(id, mac_add, ip, country, date) values (0, '00:00:00:00:00:00'::macaddr, '12.13.14.15'::INET, 'Russia', '2002-04-04');
	for r in 1..100 loop
  		INSERT INTO inet_mac(id, mac_add, ip, country, date) values (r, CONCAT(
                '0',TRUNC(RANDOM() * 8), ':' ,
                '0',TRUNC(RANDOM() * 8), ':' ,
                '0',TRUNC(RANDOM() * 8), ':' ,
                '0',TRUNC(RANDOM() * 8), ':' ,
                '0',TRUNC(RANDOM() * 8), ':' ,
                '0',TRUNC(RANDOM() * 8)
                )::MACADDR, CONCAT(
  		TRUNC(RANDOM() * 250 + 2), '.' , 
  		TRUNC(RANDOM() * 250 + 2), '.', 
  		TRUNC(RANDOM() * 250 + 2), '.',
 		TRUNC(RANDOM() * 250 + 2)
		)::INET, (array['UK', 'RUSSIA', 'USA'])[floor(random() * 3 + 1)], CONCAT('12-12-200', TRUNC(RANDOM()*8))::DATE);
	end loop;
END
$proc$;


CREATE OR REPLACE PROCEDURE nextId(INOUT nextId integer DEFAULT null)
  LANGUAGE plpgsql AS
$proc$
BEGIN
   SELECT MAX(id)+1 FROM inet_mac
   INTO nextId;
END
$proc$;

CREATE OR REPLACE PROCEDURE transformIpToCountry(ipGiven inet, INOUT countryResult varchar(32) DEFAULT null)
  LANGUAGE plpgsql AS
$proc$
BEGIN
   SELECT country FROM inet_mac WHERE ip = ipGiven
   INTO countryResult;
END
$proc$;

CREATE OR REPLACE PROCEDURE transformIpToInt(ipGiven inet, INOUT rawResult integer DEFAULT null)
  LANGUAGE plpgsql AS
$proc$
BEGIN
   SELECT (ipGiven - '0.0.0.0'::inet) as ip_integer
   INTO rawResult;
END
$proc$;

call genData();
call nextId();
call transformIpToCountry('12.13.14.15'::INET);
call transformIpToInt('12.13.14.15'::INET);



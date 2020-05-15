[2:55 PM] Chen, Song
    
-- to count MA data


select * 
from drg1.claim
limit 10; 


--* To count the total records *--
select count(*) as n_records
from drg1.claim; 
-- Results-- 
-- 78,035,396 records in 1-2 minutes



--* create tables *--
create table chens.summary_stats as 
select 
count(*) as n_records
, count(distinct claim_number ) as n_claims
, count(distinct payer_id) as n_payer_id 
, count(distinct billing_pr_npi) as n_npi
, count(distinct facility_id) as n_fac
, count(distinct ehr_patient_id) as n_pat
from drg1.claim; 


--* General Statistics *--
select * from pg_stat_all_tables
where schemaname = 'drg1';


select * from pg_stat_all_tables
where schemaname = 'drg2';


-- to explore the encounter table
select count(*) from drg2.encounter; 
-- result: 81,516,466 records 


create table chens.summary_by_year_encounter as 
select year
, count(*) 
from drg2.encounter
group by 1
order by 1; 


-- 


--drop table chens.abc; 
create table chens.summary_by_year_claim as
select yr
,count(*) as N_records
from drg1.claim
group by yr;  


create table chens.summary_by_state_provider as
select state_x
,count(*) as N_records
from drg2.provider
group by 1;  


select year
,count(*) as N_records
from drg2.submit_header
group by 1;  














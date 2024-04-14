{{ config(materialized='view') }}

select 			
cast(rideable_type as string) as rideable_type,	
cast(member_casual as string) as member_casual,	
cast(ride_id as string) as ride_id,			
cast(start_station_name as string) as start_station_name,						
cast(end_station_id as string) as end_station_id,
cast(start_lat as numeric) as start_lat,		
cast(start_lng as numeric) as start_lng,
cast(started_at as TIMESTAMP) as started_at,			
cast(ended_at as TIMESTAMP) as ended_at,			
cast(end_lat as numeric) as end_lat,				
cast(end_lng as numeric) as end_lng,	
cast(start_station_id as string) as start_station_id,			
cast(end_station_name as string) as end_station_name			
from {{ source('stg','rides_data') }}
where started_at is not null and ended_at is not null
and start_station_name is not null and start_station_name <> 'nan' and end_station_name is not null and end_station_name <> 'nan' 
and ride_id is not null and ride_id <> 'nan'
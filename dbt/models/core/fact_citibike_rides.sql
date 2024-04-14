{{ config( materialized='table') }}

dim_stations as (
    select * from {{ ref('dim_stations') }}
),

with citibikes_rides as (
    select * from {{ ref('stg_cities_bikies_rides') }}
)

select 	
    started_at,			
    ended_at,
    member_casual,	
    rideable_type,					
    ride_id,	
    start_lat,		
    start_lng,	
    timestamp_diff(ended_at, started_at, minute) as duration,
    case
        when extract(hour from {{ started_at }}) between 0 and 5 then 'Night'
        when extract(hour from {{ started_at }}) between 6 and 11 then 'Morning'
        when extract(hour from {{ started_at }}) between 12 and 17 then 'Afternoon'
        when extract(hour from {{ started_at }}) between 18 and 23 then 'Evening'
    end as day_part_start,	
    start_station_name,	
    end_lat,				
    end_lng,		
    start_station.station_id_int as start_station_id,			
    end_station_name,				
    end_station.station_id_int as end_station_id
    from citibikes_rides 
    inner join dim_stations as start_station on start_station_name = start_station.name 
    inner join dim_stations as end_station on end_station_name = end_station.name
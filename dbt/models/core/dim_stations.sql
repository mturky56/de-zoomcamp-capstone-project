{{ config(materialized="table") }}
select station_id_int, short_name, name from {{ ref('citibike_stations') }}
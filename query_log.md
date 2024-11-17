```sql

    SELECT county_name, COUNT(polling_place_id) AS pollingplace_count 
    FROM ids706_data_engineering.default.ped19_pollingplaces 
    GROUP BY county_name 
    ORDER BY pollingplace_count DESC;

```

```response from databricks
Query received, executing next...
```

```sql

    SELECT county_name, COUNT(polling_place_id) AS pollingplace_count 
    FROM ids706_data_engineering.default.ped19_pollingplaces 
    GROUP BY county_name 
    ORDER BY pollingplace_count DESC;

```

```response from databricks
None
```


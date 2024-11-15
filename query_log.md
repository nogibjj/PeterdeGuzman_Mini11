```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 75)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces2020 USING DELTA LOCATION 'dbfs:/Workspace/Shared/PeterdeGuzman_Mini11/data/polling_place_20201103.csv'
---------------------------------------------------------------------------^^^
            

```

```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 75)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces2020 USING DELTA LOCATION 'ids706_data_engineering.default.ped19_pollingplaces'
---------------------------------------------------------------------------^^^
            

```

```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 75)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces2020 USING DELTA LOCATION 's3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/9527823c-d82f-4675-bbd3-4da373f118ee'
---------------------------------------------------------------------------^^^
            

```

```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 75)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces2020 USING DELTA LOCATION 's3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/9527823c-d82f-4675-bbd3-4da373f118ee'
---------------------------------------------------------------------------^^^
            

```

```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 75)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces2020 USING DELTA LOCATION 's3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/9527823c-d82f-4675-bbd3-4da373f118ee'
---------------------------------------------------------------------------^^^
            

```

```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 75)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces2020 USING DELTA LOCATION 's3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/9527823c-d82f-4675-bbd3-4da373f118ee'
---------------------------------------------------------------------------^^^
            

```

```sql
 SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; 
```

```response from databricks
Error occurred: 
[PARSE_SYNTAX_ERROR] Syntax error at or near 'LOCATION'. SQLSTATE: 42601 (line 2, pos 71)

== SQL ==

            CREATE OR REPLACE TEMPORARY VIEW pollingplaces USING DELTA LOCATION 's3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/9527823c-d82f-4675-bbd3-4da373f118ee'
-----------------------------------------------------------------------^^^
            

```


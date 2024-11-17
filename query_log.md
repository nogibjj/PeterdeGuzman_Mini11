
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
| county_name   |   pollingplace_count |
|:--------------|---------------------:|
| WAKE          |                  824 |
| MECKLENBURG   |                  780 |
| GUILFORD      |                  660 |
| FORSYTH       |                  404 |
| BUNCOMBE      |                  320 |
| CUMBERLAND    |                  300 |
| DURHAM        |                  228 |
| UNION         |                  208 |
| GASTON        |                  184 |
| DAVIDSON      |                  172 |
| NEW HANOVER   |                  172 |
| ORANGE        |                  164 |
| ROWAN         |                  164 |
| CATAWBA       |                  160 |
| PITT          |                  160 |
| CABARRUS      |                  156 |
| ROBESON       |                  156 |
| ALAMANCE      |                  152 |
| JOHNSTON      |                  144 |
| HENDERSON     |                  140 |
| BURKE         |                  132 |
| IREDELL       |                  116 |
| HAYWOOD       |                  116 |
| WAYNE         |                  112 |
| WILKES        |                  108 |
| CARTERET      |                  104 |
| COLUMBUS      |                  104 |
| MOORE         |                  104 |
| BRUNSWICK     |                  100 |
| ONSLOW        |                   96 |
| SURRY         |                   96 |
| WILSON        |                   96 |
| NASH          |                   96 |
| SAMPSON       |                   92 |
| LINCOLN       |                   92 |
| RANDOLPH      |                   88 |
| STANLY        |                   88 |
| LENOIR        |                   88 |
| BEAUFORT      |                   84 |
| CRAVEN        |                   84 |
| CLEVELAND     |                   84 |
| EDGECOMBE     |                   84 |
| CALDWELL      |                   80 |
| WATAUGA       |                   80 |
| DUPLIN        |                   76 |
| AVERY         |                   76 |
| PENDER        |                   76 |
| HALIFAX       |                   76 |
| CHATHAM       |                   72 |
| STOKES        |                   72 |
| FRANKLIN      |                   72 |
| BLADEN        |                   68 |
| ASHE          |                   68 |
| RUTHERFORD    |                   68 |
| MCDOWELL      |                   68 |
| CHEROKEE      |                   64 |
| DARE          |                   64 |
| RICHMOND      |                   64 |
| TRANSYLVANIA  |                   60 |
| ROCKINGHAM    |                   60 |
| MACON         |                   60 |
| HOKE          |                   60 |
| GRANVILLE     |                   60 |
| DAVIE         |                   56 |
| WARREN        |                   56 |
| MONTGOMERY    |                   56 |
| NORTHAMPTON   |                   52 |
| HARNETT       |                   52 |
| MARTIN        |                   52 |
| HERTFORD      |                   52 |
| JACKSON       |                   52 |
| BERTIE        |                   48 |
| VANCE         |                   48 |
| YADKIN        |                   48 |
| MADISON       |                   48 |
| CURRITUCK     |                   44 |
| PERSON        |                   44 |
| YANCEY        |                   44 |
| ALEXANDER     |                   40 |
| PAMLICO       |                   40 |
| GREENE        |                   40 |
| LEE           |                   40 |
| CASWELL       |                   36 |
| CLAY          |                   36 |
| ANSON         |                   36 |
| PASQUOTANK    |                   36 |
| MITCHELL      |                   36 |
| PERQUIMANS    |                   28 |
| SCOTLAND      |                   28 |
| POLK          |                   28 |
| JONES         |                   28 |
| HYDE          |                   28 |
| CHOWAN        |                   24 |
| TYRRELL       |                   24 |
| WASHINGTON    |                   24 |
| GATES         |                   24 |
| SWAIN         |                   20 |
| ALLEGHANY     |                   16 |
| GRAHAM        |                   16 |
| CAMDEN        |                   12 |
```


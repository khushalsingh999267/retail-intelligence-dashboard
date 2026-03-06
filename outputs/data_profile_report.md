# Data Profile Report

## Dataset Overview

- **Rows:** 30000
- **Columns:** 9

## Column Info (CSV)

| Column           | Dtype   |   Missing Values |
|:-----------------|:--------|-----------------:|
| YEAR             | int64   |                0 |
| MONTH            | int64   |                0 |
| SUPPLIER         | object  |               33 |
| ITEM CODE        | object  |                0 |
| ITEM DESCRIPTION | object  |                0 |
| ITEM TYPE        | object  |                0 |
| RETAIL SALES     | float64 |                1 |
| RETAIL TRANSFERS | float64 |                0 |
| WAREHOUSE SALES  | float64 |                0 |

## Identified Key Columns

- **Date/Time:** YEAR, MONTH
- **Sales/Revenue:** RETAIL SALES, WAREHOUSE SALES
- **Profit:** Not Present (Infer from Sales - Transfers if applicable)
- **Product:** ITEM DESCRIPTION, ITEM CODE
- **Category:** ITEM TYPE
- **Customer:** Not Present
- **Location/Region:** Not Present (Supplier as proxy for regional distribution)
- **Marketing:** Metadata in JSON (Trends/Seasonality mentioned)

## Sample Data

|   YEAR |   MONTH | SUPPLIER                          |   ITEM CODE | ITEM DESCRIPTION                    | ITEM TYPE   |   RETAIL SALES |   RETAIL TRANSFERS |   WAREHOUSE SALES |
|-------:|--------:|:----------------------------------|------------:|:------------------------------------|:------------|---------------:|-------------------:|------------------:|
|   2020 |       1 | REPUBLIC NATIONAL DISTRIBUTING CO |      100009 | BOOTLEG RED - 750ML                 | WINE        |           0    |                  0 |                 2 |
|   2020 |       1 | PWSWN INC                         |      100024 | MOMENT DE PLAISIR - 750ML           | WINE        |           0    |                  1 |                 4 |
|   2020 |       1 | RELIABLE CHURCHILL LLLP           |        1001 | S SMITH ORGANIC PEAR CIDER - 18.7OZ | BEER        |           0    |                  0 |                 1 |
|   2020 |       1 | LANTERNA DISTRIBUTORS INC         |      100145 | SCHLINK HAUS KABINETT - 750ML       | WINE        |           0    |                  0 |                 1 |
|   2020 |       1 | DIONYSOS IMPORTS INC              |      100293 | SANTORINI GAVALA WHITE - 750ML      | WINE        |           0.82 |                  0 |                 0 |
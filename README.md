# Auto PostgreSQL

Service for creating PostgreSQL dbs. For training purposes only!

## Usage instructions

After creating db you can use it in your code, for example:

```python
import psycopg2 as pg


with pg.connect(database='test', user='test', password='test', host='some.domain', port=55432) as conn:
    with conn.cursor() as cur:
        cur.execute('create table if not exists Test(id integer primary key);')
        cur.execute('insert into Test values (1), (2), (8);')
        cur.execute('select * from Test;')
        print(cur.fetchall())
```

# Python-MySQLdb-Module
Python MySQLdb Module for MySQL.

## Dependencies
MySQLdb

## Requirements
Python v*

Auto Increment id

## Note
Params defined as 'date' or 'created' will allow mysql date functions like NOW()

## Code Example
```python
from flask import request
from flask import Response
import json
import mysqldb.py

#params = request.args #flask request arguments
params = {'name':'John', 'city':'San Francisco', 'country':'US', 'created':'NOW()'}

execute = mysqldb.insert('events',params)
return Response (json.dumps(execute, default=str, ensure_ascii=False, encoding="ISO-8859-1"))

#returns last auto_increment id of new row.
```

## Author

Evin Weissenberg

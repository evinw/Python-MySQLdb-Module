# Python-MySQLdb-Module
Python MySQLdb Module for MySQL.

## Dependencies
MySQLdb

## Code Example
```python
from flask import request
from flask import Response
import json
import mysqldb.py

execute = mysqldb.insert('events',request.args)
return Response (json.dumps(execute, default=str, ensure_ascii=False, encoding="ISO-8859-1"))
```

## Author

Evin Weissenberg

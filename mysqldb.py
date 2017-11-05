import MySQLdb as mydb
db = mydb.connect('host', 'username', 'password', 'database')
cursor = db.cursor()

def select(table, where, params, order_by_filter ='', order_direction ='DESC', limit=''):

    query = "SELECT * FROM %s WHERE %s = '%s' ORDER by '%s' '%s' %s" % (table, where, params, order_by_filter, order_direction, limit)
    cursor.execute(query)
    data = cursor.fetchall()
    if not cursor.rowcount:
        return False
    else:
        return data

def insert(table, params):

    param_key = ''
    values_string = ''
    
    for key, value in params.items():

        if key == 'date' or key == 'created':
            param_key += '%s,' % key
            values_string += "%s," % value
        else:
            param_key += '%s,' % key
            values_string += "'%s'," % value

    param_key_ = param_key.rstrip(',')
    param_value_ = values_string.rstrip(',')

    query = "INSERT INTO %s ( %s ) VALUES ( %s ) " % (table, param_key_, param_value_)
    cursor.execute(query)
    db.commit()
    id = cursor.lastrowid

    if id == None:
        return False
    else:
        return id
#
#
def update(table, params, where = None, filter = None):

    where_ = ""
    if where != None and filter != None:
        where_ = "WHERE %s = '%s' " % (where, filter)

    params_str = ""
    for key, value in params.items():
        if key == 'date' or key == 'created':
            params_str += " %s = %s," % (key, value)
        else:
            params_str += " %s = '%s'," % (key, value)


    query = "UPDATE %s SET %s %s" % (table, params_str.rstrip(','), where_)
    cursor.execute(query)
    db.commit()
    if cursor.rowcount != 0:
        return True
    else:
        return False

#
def delete(table, where, filter):

    where_ = ""
    if where != None and filter != None:
        where_ = "WHERE %s = '%s' " % (where, filter)

    query = "DELETE FROM %s %s" % (table, where_)
    cursor.execute(query)
    db.commit()
    if cursor.rowcount != 0:
        return True
    else:
        return False

from web.db import Db, Sql

try:
    con = Db().getConnection()
    cursor = con.cursor()
    cursor.execute(Sql.marketselect4)
    result = cursor.fetchall()
    for o in result:
        print(o)
except:
    print('Error')
finally:
    Db().close(con,cursor)
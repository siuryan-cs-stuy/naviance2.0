import sqlite3

f = "app.db"
db = sqlite3.connect(f)
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS favorites (college_id INTEGER, user_id INTEGER);')
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username TEXT, password TEXT);')
db.close()

def getID(user):
    f = "app.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT id FROM users WHERE username = "%s";' %(user))
    result = c.fetchall()
    db.close()
    return results[0][0]

def adduser(username,password):
    f = "app.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    if empty():
         c.execute('INSERT INTO users VALUES("%d","%s", "%s");' %(result,username, password))
         #need to finish
    if get_pass(username) is None:
        c.execute('SELECT max(id) FROM users;')
        result = c.fetchall()
        result = result[0][0] + 1
        c.execute('INSERT INTO users VALUES("%d","%s", "%s");' %(result,username, password))
        db.commit()
        db.close()
        return true
    db.close()
    return false

def empty():
    f = "app.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    
    
def get_pass(username):
    f = "app.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT password FROM users WHERE username= "%s\";' %(username))
    result = c.fetchall()
    if result == []:
        db.close()
        return None
    else:
        db.close()
        return result[0][0]
    
def addfav(c_id, s_id):
    f = "app.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT * FROM users WHERE college_id == "%d" AND user_id == "%d";'%(c_id, s_id))
    result = c.fetchall()
    if result == []:
        c.execute('INSERT INTO favorites VALUES("%d","%d");'%(c_id,s_id))
        db.commit()
        db.close()
        return true
    db.close()
    return false

def getfavs(s_id):
    f = "app.db"
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute('SELECT school_id FROM favorites WHERE student_id == "%d";' %(s_id))
    result = c.fetchall()
    db.close()
    return result

adduser

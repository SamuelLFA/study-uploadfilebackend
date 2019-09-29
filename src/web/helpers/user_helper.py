import bcrypt
from configs.db_connection import users

def userExist(email):
  if users.find({"Email": email}).count() == 0:
    return False
  else:
    return True

def verifyUser(email, password):
  if not userExist(email):
    return False

  password_hash = users.find({
    "Email": email
  })[0]["Password"]

  if bcrypt.checkpw(password.encode('utf8'), password_hash):
    return True
  else:
    return False
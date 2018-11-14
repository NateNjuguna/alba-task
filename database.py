import sqlite3

class Database:

  connection = sqlite3.connect('database.db', check_same_thread = False)

  def __init__(self, table_name):
    cursor = self.connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `alba_one` (`date` TEXT, `description` TEXT, `latitude` REAL, `longitude` REAL, `phone_number` TEXT, `username` TEXT)")
    self.connection.commit()

  def __del__(self):
    self.connection.close()

  def add(self, entry):
    self.verify_entry(entry)
    cursor = self.connection.cursor()
    cursor.execute("INSERT INTO `alba_one` VALUES (:date, :description, :latitude, :longitude, :phone_number, :username)", entry)
    self.connection.commit()

  def get_all(self):
    cursor = self.connection.cursor()
    return cursor.execute("SELECT * FROM `alba_one`").fetchall()

  def search(self, keyword):
    cursor = self.connection.cursor()
    return cursor.execute("SELECT * FROM `alba_one` WHERE `date` LIKE :keyword OR `description` LIKE :keyword OR `latitude` LIKE :keyword OR `longitude` LIKE :keyword OR `phone_number` LIKE :keyword OR `username` LIKE :keyword", {'keyword': '%'+keyword+'%'}).fetchall()
  
  def verify_entry(self, entry):
    if 'date' not in entry or 'description' not in entry or 'latitude' not in entry or 'longitude' not in entry or 'phone_number' not in entry or 'username' not in entry: 
      raise ValueError('The entry provided is invalid')

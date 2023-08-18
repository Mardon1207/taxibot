from tinydb import TinyDB,Query
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('contact')
        
    def save(self,chat_id,contact):
        date={"chat_id":chat_id,
              "contact":contact}
        self.table.insert(date)

    def izla(self, chat_id):
        user=Query()
        dic=self.table
        return dic.search(user.chat_id==chat_id)
    
    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)   
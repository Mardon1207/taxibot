from tinydb import TinyDB,Query
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('rasm')
        
    def save(self,chat_id,rasm):
        date={"chat_id":chat_id,
              "rasm":rasm}
        self.table.insert(date)

    def izla(self, chat_id):
        user=Query()
        dic=self.table
        return dic.search(user.chat_id==chat_id)
    
    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)   
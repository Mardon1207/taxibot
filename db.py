from tinydb import TinyDB,Query
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        
    def save(self,chat_id,ism,phone,user,qayer):
        users=Document(
            {"ism":ism,
             "phone":phone,
             "user":user,
             "qayer":qayer},doc_id=chat_id)
        self.db.insert(users)

    def izla(self, chat_id):
        user=Query()
        self.db.search(doc_id=chat_id)

    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==str(chat_id))    
from tinydb import TinyDB,Query
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        
    def save(self,chat_id,ism,qayer):
        user=Document(
            {"ism":ism,
             "qayer":qayer},doc_id=chat_id)
        self.db.insert(user)

    def add_ism(self, chat_id,ism):
        ism={"ism":ism}
        self.db.update(ism,doc_ids=[chat_id])

    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==str(chat_id))    
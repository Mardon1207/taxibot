from tinydb import TinyDB,Query
from tinydb.database import Document

class DB:
    def __init__(self,path):
        self.db = TinyDB(path,indent=4)
        self.table = self.db.table('taxi')
        
    def save(self,chat_id,ism,phone,havola,qayer,rasm):
        date={"chat_id":chat_id,
              "ism":ism,
              "phone":phone,
              "havola":havola,
              "qayer":qayer,
              "rasm":rasm}
        self.table.insert(date)

    def izla(self, chat_id):
        user=Query()
        dic=self.table
        return dic.search(user.chat_id==chat_id)


    def remove(self, chat_id):
        user=Query()
        self.table.remove(user.chat_id==chat_id)    

    def hamma(self):
        return self.table.all()

    def manzil(self,qayer):
        user=Query()
        return self.table.search(user.qayer==qayer)
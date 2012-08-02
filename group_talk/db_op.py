import structure 
import datetime
import logging
from misc import *
logger = logging.getLogger(__name__)

class DB_oper():
    def add_user(self,jid):
        
        #structure.init()
        new_user = structure.connection.User()
        if not isinstance(jid,str):
            jid = str(jid)
        new_user['jid']=jid
        new_user['join_time']=datetime.datetime.utcnow()
        new_user['nickname'] =self.get_default_nick(jid)
        logger.info('adding new User')
        new_user.save()
        logger.info('add new user successfully')

    def get_default_nick(self,jid):
        return jid.split('@')[0]

    def delete_user(self,user):
        user.delete()
        self.do_unsubscribe(user['jid'])
        self.do_unsubscribe(user['jid'],'unsubscribed')

    def find_user_flag(self,jid):
        u =  structure.connection.User.find_one({'jid':jid})
        return u['flag']

    def find_user_by_jid(self,jid):
        return structure.connection.User.find_one({'jid':jid})
    
    def find_user_by_nick(self,nickname):
        return structure.connection.User.find_one({'nickname':nickname})
    
    def set_nickname(self,jid,nickname):
        structure.connection.User.collection.update({'jid':jid},{'$set':{'nickname':nickname}})

    def check_user_exist(self,jid):
        u = self.find_user_by_jid(jid)
        if u :
            return True
        else:
            return False
    def check_nick_exist(self,nickname):
        u = self.find_user_by_nick(nickname)
        if u :
            return True
        else:
            return False
    @staticmethod
    def db_init():   
        structure.init()
        
if __name__=='__main__':
    structure.init()
    test = DB_oper()
    #user=test.find_user_by_jid(r'ghy@abc')
    #test.delete_user(user)
    #test.set_nick_name(r'hghgh@abc','hello')
    for u in structure.connection.User.find():
        print u['jid'],u['nickname'],u['flag']

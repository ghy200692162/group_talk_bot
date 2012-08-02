from db import *

class Messages():
    
    def get_message_reveivers(self):
        return self.get_online_users()

    def dispatch_message(self,msg,receivers):
        for receiver in receivers:
            self.send_message(receiver,msg)

    def push_message(self,msg,current_jid,timestamp=None):
        nick,msg =  self.validate(current_jid,msg)
        if nick and msg:
            receivers = [x for x in self.get_message_reveivers() if x != current_jid]
            self.dispatch_message(msg,receivers)
        elif nick is None:
            logging.info('%s dose not a group number',current_jid.as_string())
        elif msg is None:
            logging.info('%s just an empty message whcih is not allowed!!',current_jid.as_string())
        
    def validate(self,current_jid,msg):
           sender =  self.find_user_by_jid(current_jid.as_string())
           if sender:
                nick = sender['nickname'] 
                if msg is None:
                    return [nick,msg]
                else:
                    msg='['+str(nick)+'] : '+msg
                    return [nick,msg]    
           else:
                return [None,None]


import logging

from misc import *
from content import *
from content_handler import *

logger = logging.getLogger(__name__)

class Command():
    
    def dispatch_command(self,command,stanza):
        command = command[1:]
        print 'the command is %s ' % (command)
        if self.validate_perm(stanza.from_jid,command):
            if command[0]!='-':
                do_command = getattr(self,'do_'+command,None)
                if callable(do_command):
                    do_command(stanza)
            elif command[0]=='-':
                print 'to process content'
                self.process_content(stanza)
        else:
            self.send_message(stanza.from_jid,statements.get('NO_PERMISSION'))
            

    def do_kickoff(self,stanza):
        jid = str(stanza.body).split(' ')[1]
        logger.info('kick off user whose JID is %s',jid)
        u=self.find_user_by_jid(jid)
        self.delete_user(u)

    def do_changenick(self,stanza):
        jid = stanza.from_jid.bare().as_string()
        new_nickname = str(stanza.body).split(' ')[1]
        if self.check_nick_exist(new_nickname):
            self.send_message(stanza.from_jid,statements.get('NICK_EXIST'))
        else:
            logger.info('changing nickname to %s ',new_nickname)
            self.set_nickname(jid,new_nickname)

    def validate_perm(self,jid,command):
        jid = jid.bare().as_string()
        user_flag = self.find_user_flag(jid)
        command_flag = command_perm.get(command)
        if user_flag != command_flag:
            return False
        else:
            return True

    def process_content(self,stanza):
        content = Content.warpper(stanza.body)
        handler_loop(content)        


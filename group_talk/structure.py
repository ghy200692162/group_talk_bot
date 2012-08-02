from mongokit import Document,Connection
from mongokit.schema_document import ValidationError
import datetime
import logging

import config
from misc import *

logger = logging.getLogger(__name__)
global connection
def validate_jid(jid):
    if not re_jid.match(jid):
        raise ValidationError(_('wrong jid format: %s') %jid)
    return True

class User(Document):
    __collection__ = config.connection_prefix+'User'
    __database__ = config.database
    use_schemaless = True
    structure={
        'jid':str,
        'nickname':str,
        'join_time':datetime.datetime,
        'last_login_time':datetime.datetime,
        'flag':int
        }
    required_fields = ['jid']
    validators = {
            'jid':validate_jid,
            }
    default_values = {
                'join_time':datetime.datetime.utcnow(),
                'flag':GT_USER,
            }

def init():
    global connection
    logger.info('connecting to database')
    #conn_args = getattr(config,'conn_args',{})
    connection = Connection()
    logger.info('database connected ')
    connection.register([User])

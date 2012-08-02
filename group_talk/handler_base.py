
def getInstance():
    return Handler_Base()

class Handler_Base():
    def __init__(self,name=None):
        print 'handler ok'

    def process(self,content):
        print '%s is processing' % (__name__)

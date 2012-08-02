import threading

from misc import *
    
def handler_loop(content):
    ins = handle_context(content)#'handle_content',content)
    ins.start()

class handle_context(threading.Thread):


    def __init__(self,content):
        threading.Thread.__init__(self)
        self.content = content
        self.handlers = content.handler_name

    def run(self):
        self.handle_content(self.content)

    def handle_content(self,content):
        print content.handler_name,'***'
        for handler in self.handlers:
              m = __import__(handler)
              print 'in content_handler'
              instance = m.getInstance()
              content= instance.process(content)
        return content
            
if __name__=="__main__":
    m = __import__('handler_base')
    ins = m.getInstance()
    print command_handler_map.get('-base')

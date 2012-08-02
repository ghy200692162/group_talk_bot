from misc import *
class Content():

    def __init__(self,handler_name=[],text=None):
        self.handler_name = handler_name
        self.text = text

    @staticmethod
    def warpper(info): 
        con = info.split(' ')
        msg = con[-1]
        handler_coms = con[0:-1]
        print handler_coms,"&&&&"
        handler_name = Content.find_handler(handler_coms)
        return Content(handler_name,msg)

    @staticmethod
    def find_handler(handler_coms):
        handler_name = []
        for handler_com in handler_coms:
           handler_name.append(command_handler_map.get(handler_com))
        return handler_name


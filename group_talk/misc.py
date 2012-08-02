import re
GT_USER = 1
GT_ADMIN = 2
GT_SYSADMIN = 4

re_jid = re.compile(r'[^@ ]+@(?:[\w-]+\.)+\w{2,4}')

command_perm={
        'changenick':GT_USER,
        'kick':GT_ADMIN,
        '-base':GT_USER,
        }

statements={
        'NO_PERMISSION':'you have no permission to commit this command',
        'USER_EXIST':'you have all alreadly register to this group',
        'NICK_EXIST':'the nickname you want to change to is alreadly used by other group memners,\
                change another one'
        }

command_handler_map={
        '--diary':'diary_handler',
        '--base':'handler_base'
        }

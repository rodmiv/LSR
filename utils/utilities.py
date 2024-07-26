import socket

def next_free_port(port=8000, max_port =9000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while port <= max_port:
        try:
            sock.bind(('',port))
            sock.close()
            return port
        except OSError:
            port += 1
    
    raise IOError('no free ports')

def type_selection(type_line):
    if type_line.lower().find('creature')>=0:
        return 'creature'
    elif type_line.lower().find('sorcery')>=0:
        return 'sorcery'
    elif type_line.lower().find('instant')>=0:
        return 'instant'
    elif type_line.lower().find('enchantment')>=0:
        return 'enchantment'
    elif type_line.lower().find('artifact')>=0:
        return 'artifact'
    elif type_line.lower().find('land')>=0:
        return 'land'
    elif type_line.lower().find('planeswalker')>=0:
        return 'planeswalker'
    else:
        return 'other'
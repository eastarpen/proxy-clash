def modify_key(key:str):
    return key if key[0] != '_' else key[1:]

def object_to_dict(o:object):
    return dict(
            (modify_key(key), value) for key, value in o.__dict__.items() if not callable(value) and not key.startswith('__')
    )

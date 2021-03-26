import os


_DATA = {}


def UrlUtils():
    global _DATA
    if not _DATA:
        tops_app_path = os.environ['PGE_DIRECTORY']
        with open(f'{tops_app_path}/conf/settings.conf') as file:
            lines = file.readlines()
            lines = [line.split('=') for line in lines]
            _DATA = {line[0].strip(): line[1].strip()
                     for line in lines if line}
            if _DATA['GRQ_URL'][-1] == '/':
                _DATA['GRQ_URL'] = _DATA['GRQ_URL'][:-1]
    return _DATA

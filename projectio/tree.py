import os
from glob import glob
from pathlib import Path
from collections import OrderedDict


def dirlist(dirname):
    curdir = Path(os.getcwd()).as_posix() + "/" + dirname

    # remove trailing slash
    shortdir = dirname[:-1] if dirname[-1] == "/" else dirname
    
    pardir = "/".join(shortdir.split("/")[:-1])
    
    dirs_links = OrderedDict()
    files_links = OrderedDict()

    for filename in sorted(os.listdir(curdir)):
        if os.path.isdir(os.path.join(curdir, filename)):
            dirs_links[dirname + "/" + filename] = filename
        else:
            # read display line (first line of text file)
            fullname = curdir + "/" + filename
            with open(fullname, encoding="utf-8") as inf:
                filename_no_txt = filename.replace(".txt", "")
                files_links[filename_no_txt] = inf.readline()

    return {'dirs_links': dirs_links,
            'files_links': files_links,
            'pardir': pardir,
            'shortdir': shortdir,}

import os
from glob import glob
from pathlib import Path
from collections import OrderedDict


def breadcrumbs(f):
    out = []
    dirs = f.split('/')
    for i, d in enumerate(dirs):
        out.append((dirs[i], '/'.join(dirs[:i+1])))
    return out


def dirlist(dirname):
    curdir = Path(os.getcwd()).as_posix() + "/" + dirname

    # remove trailing slash
    shortdir = dirname[:-1] if dirname[-1] == "/" else dirname
    
    pardir = "/".join(shortdir.split("/")[:-1])
    
    dirs_links = OrderedDict()
    files_links = OrderedDict()

    for filename in sorted(os.listdir(curdir)):
        if os.path.isdir(os.path.join(curdir, filename)):
            # use description in description.txt if it exists
            if os.path.isfile(dirname + "/" + filename + "/description.txt"):
                with open(dirname + "/" + filename + "/description.txt", encoding="utf-8") as desc:
                    dir_desc = desc.readline()
            else:
                dir_desc = filename
            dirs_links[dirname + "/" + filename] = dir_desc
        else:
            if filename != 'description.txt' and filename != 'template.txt':
                # read display line (first line of text file)
                fullname = curdir + "/" + filename
                with open(fullname, encoding="utf-8") as inf:
                    filename_no_txt = filename.replace(".txt", "")
                    files_links[filename_no_txt] = inf.readline()

    return {'dirs_links': dirs_links,
            'files_links': files_links,
            'pardir': pardir,
            'shortdir': shortdir,
            'breadcrumbs': breadcrumbs(shortdir),}

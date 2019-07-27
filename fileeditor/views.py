import os
from glob import glob
from pathlib import Path
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'fileeditor/index.html')


@login_required
def dirlist(request, dirname):
    curdir = Path(os.getcwd()).as_posix() + "/" + dirname
    dirs_links = []
    files_links = []

    for filename in os.listdir(curdir):
        if os.path.isdir(os.path.join(curdir, filename)):
            dirs_links.append(dirname + filename)
        else:
            files_links.append(dirname + filename)


    return render(request, 'fileeditor/dirlist.html',
                  {'dirs_links': dirs_links,
                   'files_links': files_links,})


@login_required
def filecreate(request, dirname):
    info = "create"
    return render(request, 'fileeditor/info.html', {'info': info})


@login_required
def fileupdate(request, dirname, filename):
    info = "update"
    return render(request, 'fileeditor/info.html', {'info': info})


@login_required
def filedelete(request, dirname, filename):
    info = "delete"
    return render(request, 'fileeditor/info.html', {'info': info})


@login_required
def fileread(request, dirname, filename):
    info = "read"
    return render(request, 'fileeditor/info.html', {'info': info})

import os
from glob import glob
from pathlib import Path
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import TextFileForm


@login_required
def index(request):
    return render(request, 'fileeditor/index.html')


@login_required
def dirlist(request, dirname):
    curdir = Path(os.getcwd()).as_posix() + "/" + dirname
    shortdir = dirname
    pardir = "/".join(shortdir.split("/")[:-2]) + "/"
    
    dirs_links = []
    files_links = []

    for filename in os.listdir(curdir):
        if os.path.isdir(os.path.join(curdir, filename)):
            dirs_links.append(dirname + filename + "/")
        else:
            files_links.append(filename.replace(".txt", ""))

    return render(request, 'fileeditor/dirlist.html',
                  {'dirs_links': dirs_links,
                   'files_links': files_links,
                   'pardir': pardir,
                   'shortdir': shortdir,})


@login_required
def filecreate(request, dirname):
    info = "create"
    return render(request, 'fileeditor/info.html', {'info': info})


@login_required
def filedelete(request, dirname, filename):
    fullname = Path(os.getcwd()).as_posix() + "/" + dirname + "/" + filename
    info = fullname
    return render(request, 'fileeditor/info.html', {'info': info})


@login_required
def fileread(request, dirname, filename):
    fullname = Path(os.getcwd()).as_posix() + "/" + dirname + "/" + filename + ".txt"

    if request.method == "POST":
        form = TextFileForm(request.POST)
        if form.is_valid():
            new_contents = form.cleaned_data['contents']
            new_contents = new_contents.replace('\r', '')
            with open(fullname, 'w', encoding="utf-8") as outf:
                print(new_contents, file=outf)
            return redirect('fileeditor:dirlist', dirname=dirname)
    else:
        form = TextFileForm()
        contents = Path(fullname).read_text(encoding="utf-8")
        return render(request, 'fileeditor/fileread.html',
                      {'filename': fullname,
                       'contents': contents})

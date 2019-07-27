import os
import subprocess
from pathlib import Path
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import TextFileForm
from projectio import tree


@login_required
def index(request):
    return render(request, 'fileeditor/index.html')


@login_required
def dirlist(request, dirname):
    context = tree.dirlist(dirname)
    return render(request, 'fileeditor/dirlist.html', context)


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
            return redirect('fileeditor:dirlist', dirname=dirname + "/")
    else:
        form = TextFileForm()
        contents = Path(fullname).read_text(encoding="utf-8")
        return render(request, 'fileeditor/fileread.html',
                      {'filename': fullname,
                       'contents': contents})


@login_required
def gitpull(request):
    info = subprocess.check_output(['git', 'pull']).decode("utf-8")
    return render(request, 'fileeditor/info.html', {'info': info})

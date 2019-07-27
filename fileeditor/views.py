from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dirlist(request, dirname):
    return render(request, 'fileeditor/dirlist.html', {'dirname': dirname})

import os
from pathlib import Path
from django.shortcuts import render, redirect

from projectio import tree


def index(request):
    return render(request, 'quizzes/index.html')


def dirlist(request, dirname):
    context = tree.dirlist(dirname)
    return render(request, 'quizzes/dirlist.html', context)


def fileread(request, dirname, filename):
    fullname = Path(os.getcwd()).as_posix() + "/" + dirname + "/" + filename + ".txt"

    contents = Path(fullname).read_text(encoding="utf-8")

    display, description, questions_block = contents.split("===")
    questions = questions_block.splitlines()
    
    return render(request, 'quizzes/quiz.html',
                  {'description': description,
                   'questions': questions})

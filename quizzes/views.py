import os
from pathlib import Path
from django.shortcuts import render, redirect

from projectio import tree, questionparser

def index(request):
    return render(request, 'quizzes/index.html')


def dirlist(request, dirname):
    context = tree.dirlist(dirname)
    return render(request, 'quizzes/dirlist.html', context)


def fileread(request, dirname, filename):
    fullname = Path(os.getcwd()).as_posix() + "/" + dirname + "/" + filename + ".txt"

    contents = Path(fullname).read_text(encoding="utf-8")

    display, description, questions_block = contents.split("===")
    words_display, allans_table = questionparser.parse(questions_block)
            
    return render(request, 'quizzes/quiz.html',
                  {'description': description,
                   'words_display': words_display,
                   'allans_table': allans_table})

#!/bin/bash

source /home/protected/virtualenv/bin/activate
gunicorn polylexis.wsgi

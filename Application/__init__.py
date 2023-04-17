from flask import Flask
from flask import render_template

app=Flask(__name__,template_folder='views')

from Application.controllers import controller_registros
from Application.controllers import controller_reportes
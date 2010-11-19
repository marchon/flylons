from flask import Module
from application.models.foo import Foo
import random

# Attention: this part is important
foo = Module(__name__, url_prefix="/foo")

@foo.route("/")
def index():
    return "Hello foo!"


@foo.route("/create")
def create():
  try:
    new_foo = Foo.create(random.randrange(0,100))
    return "Created successfully! \n" + str(new_foo)
  except Exception, e:
    print e

@foo.route("/<id>")
def get(id):
  try:
    return str(Foo.get(id))
  except Exception, e:
    print e

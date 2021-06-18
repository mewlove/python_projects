# (control + '/' for comments)

#################################################################################
# LIST OF NEARLY ALL THE FRAMEWORKS IN PYTHON
# https://wiki.python.org/moin/GuiProgramming
# 
# Some examples below:
# PyGame is a set of Python modules designed for writing video games
# Turtle, ModernGL, Pyglet, PyOpenGL, PyQt... etc
# Course uses IPyWidgets
# pip install ipywidgets

from ipywidgets import interact, interactive, fixed   #type:ignore
import ipywidgets as widgets   #type:ignore


def func(x):    #type:ignore
    return x   #type:ignore

interact(func, x=10)  #func, default value


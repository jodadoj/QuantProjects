import pyximport # import cython files
pyximport.install() #enables the imports
import hello_world #can now import pyx as if they were py files

hello = ["hello", "world"]

# hello_world.show("Hello world!")
hello_world.show_all(hello)

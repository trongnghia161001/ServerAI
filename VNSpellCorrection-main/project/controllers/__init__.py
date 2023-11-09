import os, glob
from flask import Flask

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]



# https://gist.github.com/vaultah/d63cb4c86be2774377aa674b009f759a
import sys
import importlib
from pathlib import Path


def import_parents(level=1):
    global __package__
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[level]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:  # already removed
        pass

    __package__ = '.'.join(parent.parts[len(top.parts):])
    importlib.import_module(__package__)  # won't be needed after that


"""    
from tastu_teche.pep366_boilerplate import import_parents
if __name__ == '__main__' and __package__ is None:
    import_parents(level=1)
"""

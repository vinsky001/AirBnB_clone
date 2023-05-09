#!/usr/bin/python3

"""
Initializes  the module global (singleton) variables
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

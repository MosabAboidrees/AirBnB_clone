#!/usr/bin/python3
"""Create a unique FileStorage instance for the application."""

from models.engine.file_storage import FileStorage


# Create a unique FileStorage instance for the application
storage = FileStorage()

# Reload any saved data from the JSON file into the storage instance
storage.reload()

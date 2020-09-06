#Requires cx_freeze
#build command: python build.py build
#
import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "os"
    ], 
    "excludes": [
        "tkinter", 
        "PyQt4.QtSql", 
        "sqlite3", 
        "scipy.lib.lapack.flapack",
        "PyQt4.QtNetwork",
        "PyQt4.QtScript",
        "numpy.core._dotblas", 
        "PyQt5"
    ],
    "optimize": 2
    }
        
target = Executable(
    script="audio-remuxer.py",
    icon="lib\icon.ico"
    )

setup(
    name="Audio-Remuxer",
    version="1.0",
    description="FFmpeg audio track remuxer",
    author="downthecrop",
    options = {"build_exe": build_exe_options},
    executables=[target]
    )
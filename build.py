# Requires cx_freeze
# build command: python build.py build
import shutil
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
        "PyQt5",
        "email",
        "asyncio",
        "http",
        "unittest"
    ],
    "optimize": 2,
    "build_exe": "dist"
    }

target = Executable(
    script="audio-remuxer.py",
    icon="lib\\icon.ico"
    )

setup(
    name="Audio-Remuxer",
    version="1.4",
    description="FFmpeg audio track remuxer",
    author="downthecrop",
    options={"build_exe": build_exe_options},
    executables=[target]
    )

# Copy ffmpeg lib and settings
shutil.copyfile(r'lib\\ffmpeg.exe', r'dist\\lib\\ffmpeg.exe')
shutil.copyfile(r'settings.cfg', r'dist\settings.cfg')

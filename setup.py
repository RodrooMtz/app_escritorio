import cx_Freeze
from cx_Freeze import *

# ADD FILES
files = ['themes/']

target = Executable(
    script="main.py",
    base="Win32GUI"
)

# SETUP CX FREEZE
setup(
    name="Resilience",
    version="1.0",
    description="Aplicación para un gimnasio",
    author="Rodrigo",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)

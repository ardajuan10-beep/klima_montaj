from cx_Freeze import setup, Executable, build_exe

build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main_one.pyw',base=base)
]

setup(
    name="Karer Klima Montaj",
    version="3.0",
    description="Klima Montajlamasini Koordine eden program",
    options={'build_exe':build_options},
    executables=executables

)
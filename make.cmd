%~dp0winpython\python-3.6.2\python.exe all-fields-csv-to-rst.py
pushd %~dp0src
cmd /c make.bat html
popd
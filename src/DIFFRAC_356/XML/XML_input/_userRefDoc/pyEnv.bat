rem =================================================
echo Create pymarin environment

set ANACONDA_ROOT=C:\Anaconda3_5.2.0

set PYMARIN_PATH=D:\Programs

set DIFFRAC_MODSDOC_PYENV=D:\Programs\diffrac\XML\XML_input\_userRefDoc

%ANACONDA_ROOT%\Scripts\conda env create -f %PYMARIN_PATH%\pymarin\src\pymarin.yml -p %DIFFRAC_MODSDOC_PYENV%\pymarin_py36 --force

pause



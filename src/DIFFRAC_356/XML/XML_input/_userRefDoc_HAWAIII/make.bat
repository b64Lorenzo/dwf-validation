@ECHO OFF

REM Command file for Sphinx documentation

rem set DIFFRAC_MODSDOC_PYENV=D:\Programs\diffrac\XML\XML_input\_userRefDoc

set PyEnvPath="D:\Programs\pymarin_py36"
set ANACONDA_ROOT=C:\ProgramData\Miniconda3


call %ANACONDA_ROOT%\Scripts\activate %PyEnvPath%
pip install sphinxcontrib-confluencebuilder
pip install sphinx-autodoc-typehints
pause

rem python %PyEnvPath%\Scripts\sphinx-build-script.py -b confluence . _build/confluence -E -a
rem python %ANACONDA_ROOT%\Scripts\sphinx-build-script.py -b confluence . _build/confluence -E -a
rem python %PyEnvPath%\Scripts\sphinx-build -b html sourcedir builddir
python %PyEnvPath%\Scripts\sphinx-build.exe -b confluence . _build/confluence -E -a
pause

conda deactivate 
pause




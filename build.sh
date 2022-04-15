rm -rf dist
python -m pip install --upgrade twine build
python -m build
python -m twine upload dist/* --verbose
rm -rf src/yodas.egg-info
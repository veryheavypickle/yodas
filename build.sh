python -m pip install --upgrade build
python -m build
python -m pip install --upgrade twine
python -m twine upload dist/*
rm dist/*
python3 setup.py bdist_wheel
pip uninstall code-rl --yes
for f in dist/*; do
echo pip install $f;
pip install $f;
pytest
done
#pip install dist/code-rl*

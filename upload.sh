for f in dist/*; do
echo twine upload  $f --verbose;
twine upload  $f --verbose;
done





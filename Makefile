test:
	python -m pytest

docs:
	cd docs && make html

clean:
	rm -rf build dist obsbase.egg-info

build: clean
	python -m build

publish-test: build
	twine upload --repository testpypi dist/*

publish: build
	twine upload dist/*
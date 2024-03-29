import setuptools
from version import __version__
with open("README.md", "r") as fh:
	long_description = fh.read()

with open("requirements.txt", "r") as fh:
	requirements = fh.read().splitlines()

setuptools.setup(
	# Here is the module name.
	name="code_rl",

	# version of the module
	version=__version__,

	# Name of Author
	author="Dheeraj Pai",

	# your Email address
	author_email="dheerajmpaicmu@gmail.com",

	# #Small Description about module
	description="Code RL",

	long_description=long_description,

	# Specifying that we are using markdown file for description
	#long_description=long_description,
	long_description_content_type="text/markdown",

	# Any link to reach this module, ***if*** you have any webpage or github profile
	url="https://github.com/dheerajmpai/code-rl",
	packages=setuptools.find_packages(),


	# if module has dependencies i.e. if your package rely on other package at pypi.org
	# then you must add there, in order to download every requirement of package



	install_requires=requirements,


	license="MIT",

	# classifiers like program is suitable for python3, just leave as it is.
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)

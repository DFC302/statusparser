import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name='statusparser',
	version='2.2.1',
	author="Matthew Greer",
	author_email="pydev302@gmail.com",
        license='MIT',
	description="Retrieve HTTP status codes from list of URLs",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/DFC302/statusparser",
        keywords=['enumeration', 'domain', 'sub', 'tool', 'http', 'status', 'codes'],
	packages=setuptools.find_packages(),
        install_requires=[
            "requests",
            "argparse",
            "colorama",
        ],
        package_data={'': ['LICENSE'], '': ['README.md'],},
        include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
     ],
        entry_points={
            'console_scripts': [
                "statusparser = core.statusparser:main",
            ],
        },
)

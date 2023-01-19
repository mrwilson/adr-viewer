from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adr-viewer',
    url='https://github.com/mrwilson/adr-viewer',
    version='1.3.0',
    description='A visualisation tool for Architecture Decision Records',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alex Wilson',
    author_email='a.wilson@alumni.warwick.ac.uk',
    license='MIT',
    packages=find_packages(),
    install_requires=(
        'click',
        'mistune',
        'bs4',
        'jinja2',
        'bottle',
        'toml'
    ),
    package_data={
        'adrviewer': ['adr_viewer/templates/index.html'],
    },
    entry_points={
        'console_scripts': ['adr-viewer=adr_viewer.adrviewer:main']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Documentation',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)

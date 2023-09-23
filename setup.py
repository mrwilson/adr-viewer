from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='adr-viewer',
    url='https://github.com/mrwilson/adr-viewer',
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
        'bottle'
    ),
    package_data={
        'adr_viewer': ['templates/index.html'],
    },
    entry_points={
        'console_scripts': ['adr-viewer=adr_viewer:main']
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Documentation',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)

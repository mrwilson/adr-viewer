from setuptools import setup, find_packages

setup(
    name='adr-viewer',

    url='https://github.com/mrwilson/adr-viewer',
    version='1.0.0',
    description='A visualisation tool for Architecture Decision Records',

    author='Alex Wilson',
    author_email='a.wilson@alumni.warwick.ac.uk',
    license='MIT',

    packages=find_packages(),
    include_package_data=True,
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
        'Topic :: Software Development :: Documentation'
    ]
)

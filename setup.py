from setuptools import setup

setup(
    name="xontrib-vagrant-tabcomplete",
    version="0.1.0",
    license="GPL3",
    url="https://github.com/Virakal/xontrib-vagrant_tabcomplete",
    description="Vagrant tab autocomplete support for the Xonsh shell",
    author="Jon Goodger",
    author_email="jonno.is@gmail.com",
    packages=['xontrib', 'vagrant_tabcomplete'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    install_requires=['python-vagrant'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ]
)

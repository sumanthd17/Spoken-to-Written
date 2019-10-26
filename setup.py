from distutils.core import setup

setup(
    name='spoken2written',
    version='0.1',
    author='Sumanth Doddapaneni',
    author_email='dsumanth17@gmail.com',
    description='A package to convert spoken english to written english',
    packages=['spoken2written',],
    url="https://github.com/sumanthd17/Spoken-to-Written",
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
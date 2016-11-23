from distutils.core import setup

setup(
    name='torethink',
    version='0.1',
    packages=['torethink'],
    url='https://github.com/mehmetkose/torethink',
    license='MIT License',
    author='Mehmet Kose',
    author_email='mehmet@linux.com',
    description='Rethinkdb Mixin For Tornado Framework.',
    keywords='tornado rethinkdb layer',
    install_requires=[
        'tornado',
        'rethinkdb',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)

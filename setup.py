
from distutils.core import setup

setup(
    name='torethink',
    version='1.3.1',
    packages=['torethink'],
    url='https://github.com/mehmetkose/torethink',
    license='MIT',
    author='Mehmet Kose',
    author_email='mehmet@linux.com',
    description='Rethinkdb Wrapper For Tornado Framework',
    platforms=('Any'),
    keywords='tornado rethinkdb layer'.split(),
    install_requires=[
        'tornado>=4.4',
        'rethinkdb>=2.3',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
    ],
)

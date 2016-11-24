from distutils.core import setup

setup(
    name='torethink',
    version='0.3.0',
    packages=['torethink'],
    url='https://github.com/mehmetkose/torethink',
    license='MIT License',
    author='Mehmet Kose',
    author_email='mehmet@linux.com',
    description='Rethinkdb Mixin For Tornado Framework.',
    platforms=('Any'),
    keywords='tornado rethinkdb layer'.split(),
    install_requires=[
        'tornado>=2.3.0',
        'rethinkdb>=4.4.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)

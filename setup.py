from setuptools import setup

setup(
    name='fleek',
    version='0.1',
    packages=['fleek'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        fleek=fleek.fleek:cli
    ''',
)


from setuptools import setup

VERSION = '0.0.1'

setup(
    name="free-chatting",
    version=VERSION,
    py_modules=[
        'cli',
        'msg',
        'mocks',
    ],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        fc=cli:cli
    """,
)
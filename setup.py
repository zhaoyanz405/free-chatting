from setuptools import setup

VERSION = '0.0.1'

with open('./README.md', 'r') as f:
    readme = f.read()


setup(
    name="free-chatting",
    version=VERSION,
    description="A tool to chat with your friend easily.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zhaoyanz405/free-chatting",
    author="zhaoyanz405,jyeeee",
    author_email="zhaoyanz405@gmail.com,jyeeee@jye.com,",
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
    python_requires='>=3',
    classifiers=[
        'Intended Audience :: Anyone',
        'Topic :: Software Development :: Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords="social tools  chat",
    project_urls={
        'Documentation': 'https://github.com/zhaoyanz405/free-chatting/DOCUMTENT.md',
        'Say Thanks!': 'https://github.com/zhaoyanz405/free-chatting/README.md',
        'Source': 'https://github.com/zhaoyanz405/free-chatting',
        'Tracker': 'https://github.com/zhaoyanz405/free-chatting/issues',
    },
)
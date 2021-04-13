from distutils.core import setup

long_desc = """quoters
``A python library that gives you beautiful quotes.``

# To install
``pip install quoters``

# Documentation
``https://github.com/suman-kr/quoters``
"""

setup(
    name='quoters',
    packages=['quoters'],
    version='0.20',
    license='MIT',
    description='Pythonic random quote generator',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Suman Kumar',
    author_email='skcool.123bgp@gmail.com',
    url='https://github.com/suman-kr/quoters',
    download_url='https://github.com/suman-kr/quoters/archive/0.20.tar.gz',
    keywords=['RANDOM', 'QUOTES', 'SCRAPPER'],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'lxml',
        'html5lib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

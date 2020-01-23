from distutils.core import setup
setup(
  name = 'random-quotes',         
  packages = ['random-quotes'],   
  version = '0.1',      
  license='MIT',        
  description = 'Pythonic random quote generator',   
  author = 'Suman Kumar',                  
  author_email = 'skcool.123bgp@gmail.com',     
  url = 'https://github.com/suman-kr/random-quotes', 
  download_url = 'https://github.com/suman-kr/random-quotes/archive/0.1.tar.gz',   
  keywords = ['RANDOM', 'QUOTES', 'SCRAPPER'],   
  install_requires=[            
          'requests',
          'beautifulsoup4',
          'random',
          'sys',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'nlpPandas'
LONG_DESCRIPTION = 'nlpPandas for NLP Pandas dataframe preprocessing'

from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'nlpPandas',

  #required for multi-level directory packages
  packages=find_packages(),

  version = '1.0.0',
  license='cc-by-nc-sa-4.0',
  description = 'Easy NLP preprocessing for a Pandas dataframe', 
  author = 'Bruce W. Lee',        
  author_email = 'phys.w.s.lee@gmail.com', 
  url = 'https://github.com/brucewlee',
  keywords = ['NLP', 'Pandas', 'Preprocessing'], 
  install_requires=[            # I get to this in a second
          'pandas',
      ],

  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  include_package_data=True,
)

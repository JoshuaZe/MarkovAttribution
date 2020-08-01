from distutils.core import setup
setup(
  name = 'markovattribution',
  packages = ['markovattribution'],
  version = '0.1',
  license='MIT', 
  description = 'Markov modelling for channel attribution',
  long_description=open('README.rst', 'rt').read(),
  author = 'David Searle',
  author_email = 'connect@deepleaf.com.au',
  url = 'https://github.com/dsearle90/MarkovAttribution',
  download_url = 'https://github.com/dsearle90/MarkovAttribution/archive/v_01.tar.gz',
  keywords = ['MARKOV',
              'ATTRIBUTION',
              'CHANNELATTRIBUTION',
              'DIGITALATTRIBUTION',
              'MARKETING',
              'MEDIA'],
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
from distutils.core import setup

install_requires = open('requirements.txt').readlines()

setup(name='nagios-api',
      version="0.2",
      description='Control nagios using an API',
      author='Mark Smith',
      author_email='mark@qq.is',
      url='https://github.com/xb95/nagios-api',
      packages=['nagios'],
      scripts=['nagios-cli', 'nagios-api'],
      install_requires=install_requires,
     )

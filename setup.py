from setuptools import find_packages, setup

setup(name='grpc_helpers',
      version='0.1',
      url='https://github.com/oztqa/grpc_helpers',
      license='MIT',
      author='Eldar Bekbasov',
      author_email='bekbasov@gmail.com',
      description='Methods to simplify the execution of GRPC requests',
      packages=find_packages(),
      long_description=open('README.md').read(),
      platforms='any',
      zip_safe=False,
      install_requires=[
          'grpcio-tools',
          'allure-pytest',
          'PyHamcrest'
      ],
      classifiers=(
          'Development Status :: 4 - Beta',
          'Natural Language :: Russian',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
      ),
      keywords=[
          'grpc', 'py-grpc', 'grpc metadata'
      ],
      )

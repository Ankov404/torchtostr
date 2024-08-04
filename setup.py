from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='torchtostr',
  version='1.1.2',
  author='ankov',
  description='Module for quick and simple transportation of torch tensors arrays by converting them to str and back',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['torch', 'torchvision', 'torchaudio', 'numpy'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='tensors strings torch pytorch',
  project_urls={
    'GitHub': 'https://github.com/Ankov404/stringio'
  }
)
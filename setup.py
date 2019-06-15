import os
from setuptools import setup, Command

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

# Further down when you call setup()
setup(
    # ... Other setup options
)
setup(
    name='s4a',
    version='0.1',
    description='Introduction to SE for AI',
    author='TIm Menzies',
    author_email='timm@ieee.org',
    url='http://github.com/se4ai/code',
    packages=['s4a'],
      long_description="""\
        Introductory code for SE for AI
        Supported algorithms:
            * incremental discretizatin
            * tabu search
            * differential evolution
            * Fast-Frugl Tree
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Data mining, :: Optimizers",
      ],
      keywords='optimization data-mining',
      license='GPL',
      install_requires=[
      ],
    cmdclass={
        'clean': CleanCommand,
    },
    scripts=['bin/s4a'],
)

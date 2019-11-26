from setuptools import setup, find_packages
from platform import system
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


class PostDevelopCommand(develop):
	"""Post-installation for development mode."""
	def run(self):
		if system() == "Windows":
			check_call("pip install pywin32")
		develop.run(self)

class PostInstallCommand(install):
	"""Post-installation for installation mode."""
	def run(self):
		if system() == "Windows":
			check_call("pip install pywin32")
		install.run(self)

_system = system()

install_requires = []
if _system == 'Windows':
 install_requires += [
 #'pywin32'
]

__doc__ = 'Library to provide speech and braille output to a variety of different screen readers and other accessibility solutions.',

with open('readme.md') as readme:
 long_description = readme.read()

setup(
 name = 'accessible_output2',
 url = 'https://github.com/frastlin/accessible_output2',
 author = 'Tyler Spivey',
 author_email = 'tspivey@pcdesk.net',
 version='0.12',
 description = __doc__,
 long_description = long_description,
 package_dir = {'accessible_output2': 'accessible_output2'},
 packages = find_packages(),
 package_data = {"accessible_output2": ["lib/*"]},
 zip_safe = False,
 classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
'Topic :: Adaptive Technologies',
'Topic :: Software Development :: Libraries'
],
 install_requires = install_requires,
 cmdclass={
  'develop': PostDevelopCommand,
  'install': PostInstallCommand,
 },
)

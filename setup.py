from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='pymp4parse',
    version='0.3.0',
    packages=[''],
    url='https://github.com/use-sparingly/pymp4parse',
    license='The MIT License',
    author='Alastair Mccormack',
    author_email='alastair at alu.media',
    description='MP4 / ISO base media file format (ISO/IEC 14496-12 - MPEG-4 Part 12) file parser',
    requires=['bitstring'],
    install_requires=['bitstring'],
    long_description=long_description,
    data_files=[('', ['README.md'])]
)

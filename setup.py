from distutils.core import setup

setup(
    name='mp4parse',
    version='0.1.0',
    packages=[''],
    url='https://github.com/use-sparingly/mp4parse',
    license='The MIT License',
    author='Alastair Mccormack',
    author_email='alastair at alu.media',
    description='MP4 / ISO base media file format (ISO/IEC 14496-12 - MPEG-4 Part 12) file parser',
    requires=['bitstring'],
    install_requires=['bitstring']
)

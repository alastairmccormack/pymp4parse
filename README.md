# MP4 ISO base media file format parser 

Parses out and returns a limited set of MP4 boxes
Spell
Usage:

    import pymp4parse
    
    boxes = pymp4parse.F4VParser.parse(file)
    for box in boxes:
        print box.type
        print dir(box)

## Installation

    pip install https://github.com/use-sparingly/mp4parse/zipball/master

### Prerequisites
Pip should install prerequisites. In case you're manually installing, you'll need:

1. Bitstring - https://pypi.python.org/pypi/bitstring/


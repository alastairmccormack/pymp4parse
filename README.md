# MP4 ISO Base Media File Format Parser 

Parses out and returns a limited set of MP4 boxes

# Usage:

## Parse boxes

    import pymp4parse
    
    boxes = pymp4parse.F4VParser.parse(filename='my.mp4')
    for box in boxes:
        print box.type
        print dir(box)

## Check is MP4 file
    
    >>> pymp4parse.F4VParser.is_mp4(filename='my.mp4')
    True
    >>> pymp4parse.F4VParser.is_mp4(filename='/etc/resolv.conf')
    False
    

## Installation

    pip install https://github.com/use-sparingly/mp4parse/zipball/master

### Prerequisites
Pip should install prerequisites. In case you're manually installing, you'll need:

1. Bitstring - https://pypi.python.org/pypi/bitstring/


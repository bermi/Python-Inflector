__author__ = 'omrio'

import unicodedata


def unicodify(st):
    '''
    Convert the given string to normalized Unicode (i.e. combining characters such as accents are combined)
    If given arg is not a string, it's returned as is, and origType is 'noConversion'.
    @return a tuple with the unicodified string and the original string encoding.
    '''

    # Convert 'st' to Unicode
    if isinstance(st, unicode):
        origType = 'unicode'
    elif isinstance(st, str):
        try:
            st = st.decode('utf8')
            origType = 'utf8'
        except UnicodeDecodeError:
            try:
                st = st.decode('latin1')
                origType = 'latin1'
            except:
                raise UnicodeEncodeError('Given string %s must be either Unicode, UTF-8 or Latin-1' % repr(st))
    else:
        origType = 'noConversion'

    # Normalize the Unicode (to combine any combining characters, e.g. accents, into the previous letter)
    if origType != 'noConversion':
        st = unicodedata.normalize('NFKC', st)

    return st, origType


def deunicodify(unicodifiedStr, origType):
    '''
    Convert the given unicodified string back to its original type and encoding
    '''

    if origType == 'unicode':
        return unicodifiedStr

    return unicodifiedStr.encode(origType)

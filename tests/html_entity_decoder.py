import re 
import htmlentitydefs 
entity_re = re.compile(r'&(%s|#(\d{1,5}|[xX]([\da-fA-F]{1,5})))[ ;]{0,1};' % '|'.join(htmlentitydefs.name2codepoint.keys())) 
def html_entity_decode(s, encoding='ascii'): 
    if not isinstance(s, basestring): 
        raise TypeError('argument 1: expected string, %s found' % s.__class__.__name__) 
    def entity_2_unichr(matchobj): 
        g1, g2, g3 = matchobj.groups() 
        if g3 is not None: 
            codepoint = int(g3, 16) 
        elif g2 is not None: 
            codepoint = int(g2) 
        else: 
            codepoint = htmlentitydefs.name2codepoint[g1] 
        return unichr(codepoint) 
    if isinstance(s, unicode): 
        entity_2_chr = entity_2_unichr 
    else: 
        entity_2_chr = lambda o: entity_2_unichr(o).encode(encoding, 'xmlcharrefreplace') 
    def silent_entity_replace(matchobj): 
        try: 
            return entity_2_chr(matchobj) 
        except ValueError: 
            return matchobj.group(0) 
    return entity_re.sub(silent_entity_replace, s)

print


import httplib2
import xml.dom.minidom

data = """
<spellrequest textalreadyclipped="0" ignoredups="0" ignoredigits="1" ignoreallcaps="1">
<text> %s </text>
</spellrequest>
"""

def spellCheck(word_to_spell):

    con = httplib2.HTTPSConnection("www.google.com")
    con.request("POST", "/tbproxy/spell?lang=en", data % word_to_spell)
    response = con.getresponse()

    dom = xml.dom.minidom.parseString(response.read())
    dom_data = dom.getElementsByTagName('spellresult')[0]

    if dom_data.childNodes:
        for child_node in dom_data.childNodes:
            result = child_node.firstChild.data.split()
        for word in result:
            if word_to_spell.upper() == word.upper():
                return True;
        return False;
    else:
        return True;

from re import match
from rules import name_rules
import pytest


def test_aberP():
    import ipdb; ipdb.set_trace()
    found = []
    strings = ['rat', 'mouse', 'Aberystwyth', 'Aberdyfi', 'Aberdeen', 'Abergavenny', 'Aberuthven']
    for string in strings:
        for regex in name_rules['aberP']:
            found.append(match(regex, string).group())
        return found
    print found
    assert found == ['rat']
    # assert found == ['Aberystwyth', 'Aberdyfi', 'Aberdeen', 'Abergavenny', 'Aberuthven']


def test_not_aberP():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['rat', 'mouse']
    for string in strings:
        for regex in name_rules['aberP']:
            if match(regex, string) is not None:
                m = match(regex, string)
                found.append(match(regex, string).group())
                assert m.group() == string
            else:
                return 'No match'
        return found
    assert found == []


def test_bergQberryS():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['cheese', 'echidna', 'Blencathra', 'Blencogo', 'Blaenau Ffestiniog', 'Blantyre']
    for string in strings:
        for regex in name_rules['aberP']:
            if match(regex, string):
                found.append(match(regex, string).group())
            else:
                return 'No match'
        return found
    assert found == ['Blencathra', 'Blencogo', 'Blaenau Ffestiniog', 'Blantyre']


# # def test_not_bergQberryS():
#     found = []
#     strings = ['cheese', 'echidna']
#     for string in strings:
#         for regex in name_rules['bergQberryS']:
#             if match(regex, string):
#                 found.append(match(regex, string).group())
#             else:
#                 found is None
#         return found
#     assert found is None


def test_casterSchasterScesterSceterScaisterQxeterS():
    found = []
    strings = ['Damaraland mole rat', 'Cape Dune mole rat', 'Lancaster', 'Doncaster', 'Gloucester', 'Caister', 'Manchester', 'Chichester', 'Worcester', 'Chester', 'Exeter', 'Cirencester', 'Colchester', 'Tadcaster', 'Leicester', 'Towcester']
    for string in strings:
        for regex in name_rules["casterSchasterScesterSceterScaisterQxeterS"]:
            if match(regex, string):
                found.append(match(regex, string).group())
            else:
                return 'No match'
        return found
    assert found == ['Doncaster', 'Gloucester', 'Caister', 'Manchester', 'Chichester', 'Worcester', 'Chester', 'Exeter', 'Cirencester', 'Colchester', 'Tadcaster', 'Leicester', 'Towcester']


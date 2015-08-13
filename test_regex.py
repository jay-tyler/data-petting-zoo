from re import match
from rules import name_rules
import pytest


def test_aberP():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['rat', 'mouse', 'Aberystwyth', 'Aberdyfi', 'Aberdeen', 'Abergavenny', 'Aberuthven']
    for string in strings:
        for regex in name_rules['aberP']:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]


def test_not_aberP():
    # import ipdb; ipdb.set_trace()
    strings = ['rat', 'mouse']
    for string in strings:
        for regex in name_rules['aberP']:
            m = match(regex, string)
            assert m is None


def test_bergQberryS():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['cheese', 'echidna', 'Blencathra', 'Blencogo', 'Blaenau Ffestiniog', 'Blantyre']
    for string in strings:
        for regex in name_rules['bergQberryS']:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]


def test_not_bergQberryS():
    found = []
    strings = ['cheese', 'echidna']
    for string in strings:
        for regex in name_rules['aberP']:
            m = match(regex, string)
            assert m is None


def test_casterSchasterScesterSceterScaisterQxeterS():
    found = []
    strings = ['Damaraland mole rat', 'Cape Dune mole rat', 'Lancaster', 'Doncaster', 'Gloucester', 'Caister', 'Manchester', 'Chichester', 'Worcester', 'Chester', 'Exeter', 'Cirencester', 'Colchester', 'Tadcaster', 'Leicester', 'Towcester']
    for string in strings:
        for regex in name_rules['casterSchasterScesterSceterScaisterQxeterS']:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]
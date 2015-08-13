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


def test_blenPblaenP():
    found = []
    strings = ['cheese', 'echidna', 'Blencathra', 'Blencogo', 'Blaenau Ffestiniog', 'Blantyre']
    for string in strings:
        for regex in name_rules['blenPblaenP']:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]


def test_not_blenPblaenP():
    strings = ['cheese', 'echidna']
    for string in strings:
        for regex in name_rules['aberP']:
            m = match(regex, string)
            assert m is None


def test_dunPdumPdonPdouneP():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['Damaraland mole rat', 'Somalian Stripe mole rat', 'Dundee', 'Dumbarton', 'Dungannon', 'Dumfries', 'Donegal']
    for string in strings:
        for regex in name_rules["dunPdumPdonPdouneP"]:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]


def test_not_dunPdumPdonPdouneP():
    strings = ['Damaraland mole rat', 'Somalian stripe mole rat']
    for string in strings:
        for regex in name_rules["dunPdumPdonPdouneP"]:
            m = match(regex, string)
            assert m is None


def test_gillPgillSghyllPghyllA():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['Cape dune mole rat', 'Namibian mole rat', 'Gillamoor', 'Garrigill', 'Dungeon Ghyll']
    for string in strings:
        for regex in name_rules["gillPgillSghyllPghyllA"]:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]

def test_not_gillPgillSghyllPghyllA():
    strings = ['Cape dune mole rat', 'Namibian mole rat']
    for string in strings:
        for regex in name_rules["gillPgillSghyllPghyllA"]:
            m = match(regex, string)
            assert m is None


def test_eaglesPeglosPeglewsPecclesP():
    # import ipdb; ipdb.set_trace()
    found = []
    strings = ['Ethiopian mole rat', 'Silvery mole rat', 'Eaglesham', 'Egloskerry', 'Ecclefechan']
    for string in strings:
        for regex in name_rules["eaglesPeglosPeglewsPecclesP"]:
            m = match(regex, string)
            if m is not None:
                found.append(m.group())
    assert found == strings[2:]


def test_not_eaglesPeglosPeglewsPecclesP():
    strings = ['Ethiopian mole rat', 'Silvery mole rat']
    for string in strings:
        for regex in name_rules["gillPgillSghyllPghyllA"]:
            m = match(regex, string)
            assert m is None


import pytest
from engine import patinls, patinstr
import numpy as np


def test_list_match():
    # eximport pdb; pdb.set_trace()
    slist = ['Acomb', 'rat', 'mouse']
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    assert patinls(slist, patlist).group() == 'Ac'


def test_list_not_match():
    slist = ['comb', 'rat', 'mouse']
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    assert patinls(slist, patlist) is None


def test_list_not_string():
    slist = [3, 'rat', 'mouse']
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    with pytest.raises(TypeError):
        patinls(slist, patlist)


def test_list_nan():
    slist = np.nan
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    assert patinls(slist, patlist) is None


def test_string_match():
    string = 'Acomb'
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    assert patinstr(string, patlist)


def test_string_not_match():
    string = 'mice'
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    assert patinstr(string, patlist) is None


def test_string_nan():
    string = ''
    patlist = ("(Ac)", "(Acc)", "(ock$)")
    assert patinstr(string, patlist) is None

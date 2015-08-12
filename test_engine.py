
import pytest
from engine import patinls, patinstr, setgb, setfam, setalt
import numpy as np


def test_proper_columns():
    expected_columns = ['geoid', 'name', 'asciiname', 'altname', 'lat', 'long',
        'feature_class', 'feature_code', 'country_code', 'cc2', 'adm1', 'adm2',
        'adm3', 'adm4', 'pop', 'elev', 'delev', 'timezone', 'moddate']
    proper_df = setgb('data/pristine/GB.txt')
    for column_name in expected_columns:
        assert column_name in proper_df.columns


def test_remove_extra():
    extra = ['05', '00', '01', 'NIR', '03']
    proper_df = setgb('data/pristine/GB.txt')
    for item in extra:
        for index, row in proper_df.iterrows():
            assert item not in row


def test_set_fam():
    df = setgb('data/pristine/GB.txt')
    df_fam = setfam(df)
    assert 'ls_namefam' in df_fam.columns


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

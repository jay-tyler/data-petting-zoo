
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

def test_list_match():
    slist = ['Acomb', 'rat', 'mouse']
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    assert patinls(slist, patlist).group() == 'Acomb'


def test_list_not_match():
    slist = ['comb', 'rat', 'mouse']
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    assert patinls(slist, patlist) is None


def test_list_not_string():
    slist = [3, 'rat', 'mouse']
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    with pytest.raises(TypeError):
        patinls(slist, patlist)


def test_list_nan():
    slist = np.nan
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    assert patinls(slist, patlist) is None


def test_string_match():
    string = 'Acomb'
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    assert patinstr(string, patlist)


def test_string_not_match():
    string = 'mice'
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    assert patinstr(string, patlist) is None


def test_string_nan():
    string = ''
    patlist = ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))")
    assert patinstr(string, patlist) is None


def test_set_fam():
    df_head = setgb('data/pristine/GB.txt').head()
    df_fam_head = setfam(df_head)
    assert 'ls_namefam' in df_fam_head.columns


def test_hasparent():
    df_head = setgb('data/pristine/GB.txt').head()
    df_alt_head = setalt(setfam(df_head))
    assert 'parent' in df_alt_head.columns


def test_not_have_altname():
    df_head = setgb('data/pristine/GB.txt').head()
    df_alt_head = setalt(setfam(df_head))
    assert 'altname' not in df_alt_head.columns
    assert 'ls_altname' not in df_alt_head.columns


def test_parent():
    df_head = setgb('data/pristine/GB.txt').head()
    df_alt_head = setalt(setfam(df_head))
    assert df_alt_head.ix[0, 'name'] == 'Zennor'
    assert df_alt_head.ix[0, 'parent'] == 'nan'
    assert df_alt_head.ix[0, 'name'] == 'Zennor'
    assert df_alt_head.ix[0, 'parent'] == 'nan'

def test_not_parent():
    df_head = setgb('data/pristine/GB.txt').head()
    df_alt_head = setalt(setfam(df_head))
    assert df_alt_head.ix[0, 'name'] == 'Zennor'
    assert df_alt_head.ix[0, 'parent'] == 'nan'

# def test_altname_in_parentname():
#     df_head = setgb('data/pristine/GB.txt').head()
#     df_alt_head = setalt(setfam(df_head))
#     assert 'Zelah' in df_alt_head['parent']


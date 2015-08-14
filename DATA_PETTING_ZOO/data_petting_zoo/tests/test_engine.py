
import pytest
from ..engine import patinls, patinstr, set_gb, set_fam, set_alt, get_fam, query_name
from ..rules import name_rules
import numpy as np
import pandas as pd
import math
from re import match

# testgb = pd.read_csv('testgb.csv')

def test_proper_columns():
    expected_columns = ['geoid', 'name', 'asciiname', 'altname', 'lat', 'long',
                        'feature_class', 'feature_code', 'country_code', 'cc2', 'adm1', 'adm2',
                        'adm3', 'adm4', 'pop', 'elev', 'delev', 'timezone', 'moddate']
    proper_df = set_gb('testgb.csv')
    for column_name in expected_columns:
        assert column_name in proper_df.columns


def test_remove_extra():
    extra = ['05', '00', '01', 'NIR', '03']
    proper_df = set_gb('testgb.csv')
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
    df_head = set_gb('gb_part.csv')
    df_fam_head = set_fam(df_head)
    assert 'ls_namefam' in df_fam_head.columns


def test_hasparent():
    df_head = set_gb('gb_part.csv')
    df_alt_head = set_alt(set_fam(df_head))
    assert 'parent' in df_alt_head.columns


def test_not_have_altname():
    df_head = set_gb('gb_part.csv').head()
    df_alt_head = set_alt(set_fam(df_head))
    assert 'altname' not in df_alt_head.columns
    assert 'ls_altname' not in df_alt_head.columns


def test_parent():
    df_head = set_gb('gb_part.csv').head()
    df_fam_head = set_fam(df_head)
    df_alt_head = set_alt(df_fam_head)
    last_alt_head = df_alt_head.ix[5:, :]
    assert 'Zelah' not in last_alt_head
    assert 'Ythsie' not in last_alt_head


# # def test_parent():
# #     df_head = set_gb('data/pristine/NEWGB.csv').head()
# #     df_fam_head = setfam(df_head)
# #     df_alt_head = set_alt(df_fam_head)
# #     # first_alt_head = df_alt_head.ix[:5, :]
# #     last_alt_head = df_alt_head.ix[5:, :]
# #     for index_fam, row_fam in df_fam_head.iterrows():
# #         for index_alt, row_alt in df_fam_head.iterrows():
# #             if df_fam_head.ix[index_fam, 'altname']:
# #                 assert df_fam_head.ix[index_fam, 'name'] in last_alt_head.ix[index_alt, 'altname']
# #             else:
# #                 assert df_fam_head.ix[index_fam, 'name'] not in last_alt_head.ix[index_alt, 'altname']


def test_alt_hasnot_parent():
    df_head = set_gb('gb_part.csv').head()
    df_fam_head = set_fam(df_head)
    df_alt_head = set_alt(df_fam_head)
    for index, row in df_alt_head.iterrows():
        for index in range(5):
            assert math.isnan(df_alt_head.ix[index, 'parent'])


# # def test_alt_parent():
# #     # import ipdb; ipdb.set_trace()
# #     df_head = set_gb('data/pristine/NEWGB.csv').head()
# #     df_fam_head = setfam(df_head)
# #     df_alt_head = set_al(df_fam_head)
# #     assert df_alt_head.ix[0, 'name'] == 'Zennor'
# #     assert math.isnan(df_alt_head.ix[0, 'parent']) is True

def test_alt_has_parent():
    df_head = set_gb('gb_part.csv').head()
    df_fam_head = set_fam(df_head)
    df_alt_head = set_alt(df_fam_head)
    last_alt_head = df_alt_head.ix[5:, :]
    for index, row in last_alt_head.iterrows():
        assert len(last_alt_head.ix[index, 'parent']) > 0


def test_alt_row():
    df_head = set_gb('gb_part.csv').head()
    df_fam_head = set_fam(df_head)
    df_alt_head = set_alt(df_fam_head)
    assert df_alt_head.ix[0, 'name'] == df_fam_head.ix[0, 'name']
    assert math.isnan(df_alt_head.ix[0, 'parent'])


def test_get_fam():
    df_part = set_gb('gb_part.csv')
    df_fam = set_fam(df_part)
    df_worth = get_fam(df_fam, "worthSworthySwardineS")[0]
    for index, row in df_worth.iterrows():
        for regex in name_rules["worthSworthySwardineS"]:
            m = match(regex, df_worth.ix[index, 'name'])
            if m is not None:
                assert True

def test_query_name_true():
    df_part = set_gb('gb_part.csv')
    query_zelah = query_name(df_part, 'Zelah')
    query_zeals = query_name(df_part, 'Zeals')
    assert query_zelah[0]
    assert query_zeals[1]


def test_query_name_false():
    df_part = set_gb('gb_part.csv')
    query_zelah = query_name(df_part, 'Zelah')
    query_zeals = query_name(df_part, 'Zeals')
    assert not query_zelah[1]
    assert not query_zeals[0]

# def test_query_placename_true():
#     df_part = set_gb('gb_part.csv')
#     query_zelah = query_name(df_part, 'Zelah')
#     query_zeals = query_name(df_part, 'Zeals')
#     assert query_zelah[0]
#     assert query_zeals[1]


# # def mlen(inlist):
# #     try:
# #         response = len(inlist)
# #     except TypeError:
# #         response = 0
# #     return response


# # def test_count_rows():
# #     df_head = set_gb('data/pristine/NEWGB.csv').head()
# #     df_fam_head = setfam(df_head)
# #     df_alt_head = set_alt(df_fam_head)
# #     alt_names_count = df_fam_head['ls_altname'].map(lambda x: mlen(x))
# #     assert len(df_fam_head.index) + alt_names_count == len(df_alt_head.index)


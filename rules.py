# Regex patterns that match naming conventions. See here:
# https://en.wikipedia.org/wiki/List_of_generic_forms_in_place_names_in_the_United_Kingdom_and_Ireland
name_rules = {
    "aberP": ("(Aber)",),
    "acPaccPockS": ("(Ac)", "(Acc)", "(ock$)"),
    "afonSavonQ": ("(afon$)", "([aA]von)"),
    "arPardP": ("(Ar)", "(Ard)"),
    "byS": ("(by$)",),
    "ashP": ("(Ash)",),
    "astP": ("(Ast)",),
    "auchenPauchinPauchachP": ("(Auchen)", "(Auchin)", "(Auchach)"),
    "auchterP": ("(Auchter)",),
    "axPexePaxeAeskA": ("(Ax)", "(Exe)", "(Usk)", "(Esk)"),
    "aySeyS": ("(ay$)", "(ey$)"),
}

# Pick only feature codes that correspond to towns and cities, see
# http://www.geonames.org/export/codes.html
geofeat_rules = ("PPL", "PPLA", "PPLA2", "PPLA3", "PPLA4", "PPLC", "PPLCH",
    "PPLF", "PPLG", "PPLH", "PPLL", "PPLQ", "PPLR", "PPLS", "PPLW")

#Description of engine API

##Setup functions

The engine for data-petting-zoo has several setup functions that enable
setting up the pandas dataframe from scratch. This is useful for filtering
tweaks, etc.

These functions include:

* setgb(file_path) --> DataFrame: file_path is path to GB.txt geonames

This function reads the GB.txt dataset from file_path and returns a dataframe
after applying filters for adm1 regions and geofeatures.

* setalt(DataFrame, column_names=None) --> DataFrame: DataFrame should only be the dataframe that
comes after setgb if columns is left undefined; columns is a list of column names that
the resulting dataframe should contain. This list should include 'parent.'

* setfam(DataFrame) --> DataFrame: DataFrame can be any with a 'name' column

This function applies the regexes from name_rules and establishes an 'ls_namefam'
column which contains a Python list containing 'namekey's for applying to the
row. np.nan is used to designate rows without membership to any name family.

##Query functions

* patinls(slist, patlist) --> re.match object or none: slist is a list contained
within the dataframe, patlist is any iterable containing valid regex strings
This function searches the slist for any regex match defined by the iterable
patlist. Handling for np.nan is provided (returning None).

* patinstr(string, patlist) --> re.match object or none: string is any python
string object and patlist is any iterable containing valid regex strings.
This function searches string for any regex match definied by the iterable
patlist. Handling for np.nan is provided (returning None).

* getfamdf(DataFrame, namekey) --> DataFrame: DataFrame input can be any
dataframe that contains an 'ls_namefam' column; namekey should be one of
the namekeys defined as a key in name_rules.
The returned DataFrame will be a sub-DataFrame containing rows with instances
of namekey in 'ls_namefam.'

#Description of geonames columns

* adm4: parish councils. Codes and names [here](http://specification.sifassociation.org/implementation/UK/1.3/CodeSets.html#CodeSets). [Wiki](https://en.wikipedia.org/wiki/Parish_councils_in_England).

#Links to Related Resources

* [Guide to English Placenames](http://kepn.nottingham.ac.uk/)
* [Wiki List of Generic Nameforms](https://en.wikipedia.org/wiki/List_of_generic_forms_in_place_names_in_the_United_Kingdom_and_Ireland#cite_note-oswelsh-1)
* [Guide to Welsch Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/welsh-placenames.html)
* [Guide to Gaelic Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/gaelic-placenames.html)
* [Guide to Scandinavian Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/scandinavian-placenames.html)
* [Guide to Scots Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/scots-placenames.html)
* [Scottish Placename Society](http://www.spns.org.uk/)

#Licensing

* Primary geonames dataset is taken from [geonames.org](http://www.geonames.org) which is distributed
under a [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/).
* GVA data provided by the UK Office of National Statistics, via [here](http://www.ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-339598).
This data is bound to an [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
* Our work is distributed according the MIT license included in this repo

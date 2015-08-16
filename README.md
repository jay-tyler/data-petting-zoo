# What's in a Name: A Data Petting Zoo
Most of the names of towns and cities in the UK came before English was the de
facto language. They were named at a period in time where there were several
groups co-existing on the British Isles and each had a language closer to
the Germanic roots of the English language. Each place name is dripping with
associations of adjectivial meaning and bindings to cultural groups that no
longer distinctly exist. For this reason, a visual exploration of the data is
interesting. 

It is worth noting that we take a naive approach to the data; everything is
matched based on general patterns as opposed to cherry-picking based on
careful historical research. We feel our approach is interesting and generally valid,
but should not be taken as canonical. There will be names grouped into associations
of meaning that don't belong in those associations. This data is more about visualizing
trends, and very good data regarding *any one particular placename* can be
obtained from one of the fine scholastic sources listed below.

## Description of engine API

### Setup functions

The engine for data-petting-zoo has several setup functions that enable
setting up the pandas dataframe from scratch. This is useful for filtering
tweaks, etc.

These functions include:

* set_gb(file_path) --> DataFrame: file_path is path to GB.txt geonames

This function reads the GB.txt dataset from file_path and returns a dataframe
after applying filters for adm1 regions and geofeatures.

* set_alt(DataFrame, column_names=None) --> DataFrame: DataFrame should only be the dataframe that
comes after setgb if columns is left undefined; columns is a list of column names that
the resulting dataframe should contain. This list should include 'parent.'

* set_fam(DataFrame) --> DataFrame: DataFrame can be any with a 'name' column

This function applies the regexes from name_rules and establishes an 'ls_namefam'
column which contains a Python list containing 'namekey's for applying to the
row. np.nan is used to designate rows without membership to any name family.

### Query functions

* patinls(slist, patlist) --> re.match object or none

`slist` is a list contained within the dataframe, patlist is any iterable containing 
valid regex strings. This function searches the slist for any regex match defined
by the iterable patlist. Handling for np.nan is provided (returning None).

* patinstr(string, patlist) --> re.match object or none

`string` is any python string object and patlist is any iterable containing valid regex strings.
This function searches string for any regex match definied by the iterable
patlist. Handling for np.nan is provided (returning None).

* get_fam(DataFrame, namekey) --> DataFrame, namekey, None. 

DataFrame input can be any dataframe that contains an 'ls_namefam' column; namekey should be one of
the namekeys defined as a key in name_rules. The returned DataFrame will be a sub-DataFrame containing rows with instances
of namekey in 'ls_namefam.' None is returned as a placename for consistency with other APIs.

* query_placename(DataFrame, placestring) --> DataFrame, namekey, placename.

Input should be any dataframe that contains 'ls_namefame' and 'name' columns, and placestring
is user input (or otherwise) that putatively corresponds to an actual named
place in the UK; query_placename will attempt to find a place (or something close)
and will return the corresponding sub-DataFrame corresponding to the namefamily
as well as a namekey indicating that family.

* query_name_or_fam(DataFrame, placestring) --> DataFrame, namekey, placename.

Attempts to execute query_placename() with arguments provided. If this fails,
returns a DataFrame consisting of a single place match with a namekey of None
and the placename match. If both queries fail, returns None.

## Links to Related Resources

* [Guide to English Placenames](http://kepn.nottingham.ac.uk/)
* [Wiki List of Generic Nameforms](https://en.wikipedia.org/wiki/List_of_generic_forms_in_place_names_in_the_United_Kingdom_and_Ireland#cite_note-oswelsh-1)
* [Guide to Welsch Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/welsh-placenames.html)
* [Guide to Gaelic Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/gaelic-placenames.html)
* [Guide to Scandinavian Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/scandinavian-placenames.html)
* [Guide to Scots Placenames](https://www.ordnancesurvey.co.uk/resources/historical-map-resources/scots-placenames.html)
* [Scottish Placename Society](http://www.spns.org.uk/)

## Licensing

* Primary geonames dataset is taken from [geonames.org](http://www.geonames.org) which is distributed
under a [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/).
* GVA data provided by the UK Office of National Statistics, via [here](http://www.ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-339598).
This data is bound to an [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
* Our work is distributed according the MIT license included in this repo

## On D3

### Primary article for walking through shapefile-to-GeoJSON conversion
and SVG map creation:

- http://bost.ocks.org/mike/map/

### On the general update pattern:

- http://bl.ocks.org/mbostock/3808221

### Simple Slider

- http://bl.ocks.org/mbostock/6452972

### Things Involving Histograms/Bar Charts

- http://alignedleft.com/tutorials/d3/making-a-bar-chart
- http://stackoverflow.com/questions/13654658/d3-axis-tick-alignment
- http://bl.ocks.org/mbostock/3048450
- https://gist.github.com/mbostock/1933560
- http://jaketrent.com/post/use-d3-rangebands/
- https://gist.github.com/enjalot/6641917
- http://stackoverflow.com/questions/20367899/d3-js-controlling-ticks-and-bins-on-a-histogram
- http://bl.ocks.org/mbostock/1624660

# Regex patterns that match naming conventions. See here:
# https://en.wikipedia.org/wiki/List_of_generic_forms_in_place_names_in_the_United_Kingdom_and_Ireland
name_rules = {
    "aberP": ("(.*\s*Aber.*)",),
    "acPaccPockS": ("(.*\s*Ac.*)", "(.*\s*Acc.*)", "(.*\w+ock($|[\s+.*]))"),
    "afonSavonQ": ("(.*\w+afon($|[\s+.*]))", "(.*[aA]von.*)"),
    "arPardP": ("(.*\s*Ar.*)", "(.*\s*Ard.*)"),
    "ashP": ("(.*\s*Ash.*)",),
    "astP": ("(.*\s*Ast.*)",),
    "auchenPauchinPauchachP": ("(.*\s*Auchen.*)", "(.*\s*Auchin.*)", "(.*\s*Auchach.*)"),
    "auchterP": ("(.*\s*Auchter.*)",),
    "axPexePaxeAeskA": ("(.*\s*Ax.*)", "(.*\s*Exe.*)", "(.*Axe.*)", "(.*Esk.*)"),
    "aySeyS": ("(.*\w+ay($|[\s+.*]))", "(.*\w+ey($|[\s+.*]))"),
    "balPballaPballyPballP": ("(.*\s*Bal.*)", "(.*\s*Balla.*)", "(.*\s*Bally.*)", "(.*\s*Ball.*)"),
    "beckPbeckSbecA": ("(.*\s*Beck.*)", "(.*\w+beck($|[\s+.*]))", "(.*Bec.*)"),
    "benAbeinnQBeannQ": ("(.*Ben.*)", "(.*[bB]einn.*)", "(.*[bB]eann.*)"),
    "bergQberryS": ("(.*[bB]erg.*)", "(.*\w+berry($|[\s+.*]))"),
    "bexP": ("(.*\s*Bex.*)",),
    "blenPblaenP": ("(.*\s*Blen.*)", "(.*\s*Blaen.*)", "(.*\s*Blan.*)"),
    "bostS": ("(.*\w+bost($|[\s+.*]))",),
    "bournePbourneSburnS": ("(.*\s*Bourne.*)", "(.*\w+bourne($|[\s+.*]))", "(.*\w+burn($|[\s+.*]))"),
    "bradP": ("(.*\s*Brad.*)",),
    "breP": ("(.*\s*Bre.*)",),
    "burySboroughSbroughSburghS": ("(.*\w+bury($|[\s+.*]))", "(.*\w+borough($|[\s+.*]))", "(.*\w+brough($|[\s+.*]))",
     "(.*\w+burgh($|[\s+.*]))"),
    "bySbiP": ("(.*\w+By($|[\s+.*]))", "(.*\s*Bi.*)"),
    "cardenScardineS": ("(.*\w+carden($|[\s+.*]))", "(.*\w+cardine($|[\s+.*]))"),
    "caerPcarP": ("(.*\s*Caer.*)", "(.*\s*Car.*)"),
    "casterSchasterScesterSceterScaisterQxeterS": ("(caster($|[\s+.*]))", "(chaster($|[\s+.*]))",
        "(cester($|[\s+.*]))", "(ceter($|[\s+.*]))", "([cC]aister)", "(xeter($|[\s+.*]))"),
    "cheapQchepPchippingA": ("(.*[cC]heap.*)", "(.*\s*Chep.*)", "(.*Chipping)"),
    "combeScwmPcoombeA": ("(.*\w+combe($|[\s+.*]))", "(.*\s*Cwm.*)", "(.*Coombe.*)"),
    "coedS": ("(.*\w+coed($|[\s+.*]))",),
    "cotScottS": ("(.*\w+cot($|[\s+.*]))", "(.*\w+cott($|[\s+.*]))"),
    "craigPcraigAcragPcragAcreagPcreagAgraigPgraigA": ("(.*\s*Craig.*)",
        "(.*Craig.*)", "(.*\s*Crag.*)", "(.*Crag.*)", "(.*\s*Creag.*)", "(.*Creag.*)", "(.*\s*Graig.*)", "(.*Graig.*)"),
    "culP": ("(.*\s*Cul.*)",),
    "cwmPcumP": ("(.*\s*Cwm.*)", "(.*\s*Cum.*)"),
    "cumI": ("(.+cum.+)",),
    "dalP": ("(.*\s*Dal.*)",),
    "daleS": ("(.*\w+dale($|[\s+.*]))",),
    "deanSdeanAdenSdonS": ("(.*\w+dean($|[\s+.*]))", "(.*Dean)", "(.*\w+don($|[\s+.*]))", "(.*\w+den($|[\s+.*]))"),
    "dinPdinasPdinasA": ("(.*\s*Din.*)", "(.*Dinas.*)"),
    "dolPdullA": ("(.*\s*Dol.*)", "(.*Dull.*)"),
    "donSdenS": ("(.*\w+don($|[\s+.*]))", "(.*\w+den($|[\s+.*]))"),
    "drumP": ("(.*\s*Drum.*)",),
    "dubhSdubhPdubhAdowQdhuQduffQ": ("(.*Dubh.*)", "(.*[Dd]ow.*)", "(.*[Dd]hu.*)", "(.*[Dd]uff.*)"),
    "dunPdumPdonPdouneP": ("(.*\s*Dun.*)", "(.*\s*Dum.*)", "(.*\s*Don.*)", "(.*\s*Doune.*)"),
    "eaglesPeglosPeglewsPecclesP": ("(.*\s*Eagles.*)", "(.*\s*Eglos.*)", "(.*\s*Eccle.*)", "(.*\s*Eglews.*)"),
    "eilianA": ("(.*Eilian)",),
    "eySayS": ("(.*\w+ey($|[\s+.*]))", "(.*\w+ay($|[\s+.*]))"),
    "eySeaQeigQ": ("(.*\w+ey($|[\s+.*]))", "(.*[Ee]a.*)", "(.*[Ee]ig.*)"),
    "fieldS": ("(.*\w+field($|[\s+.*]))",),
    "finP": ("(.*\s*Fin.*)",),
    "firthSfrithQ": ("(.*\w+firth($|[\s+.*]))", "(.*[Ff]rith.*)"),
    "firthSfirthA": ("(.*\w+firth($|[\s+.*]))", "(.*Firth.*)"),
    "fordSforthS": ("(.*\w+ford($|[\s+.*]))", "(.*\w+forth($|[\s+.*]))"),
    "fosQfossSfossA": ("(.*[Ff]os.*)", "(.*\w+foss($|[\s+.*]))", "(.*Foss.*)"),
    "fossQforceA": ("(.*[Ff]oss.*)", "(.*Force)"),
    "garPgartP": ("(.*\s*Gar.*)", "(.*\s*Gart.*)"),
    "garthS": ("(.*\w+garth($|[\s+.*]))",),
    "gateAgateS": ("(.*Gate)", "(.*\w+gate($|[\s+.*]))"),
    "gillPgillSghyllPghyllA": ("(.*\s*Gill.*)", "(.*\w+gill($|[\s+.*]))", "(.*\s*Ghyll.*)", "(.*\w+ghyll($|[\s+.*]))"),
    "glenPglenSglenA": ("(.*\s*Glen.*)", "(.*\w+glen($|[\s+.*]))", "(.*Glen.*)"),
    "gowtA": ("(.*Gowt.*)",),
    "hamS": ("(.*\w+ham($|[\s+.*]))",),
    "hitheShytheA": ("(.*\w+hithe($|[\s+.*]))", "(.*Hythe.*)"),
    "holmQ": ("(.*[Hh]olm.*)",),
    "hopeS": ("(.*\w+hope($|[\s+.*]))",),
    "howeA": ("(.*Howe.*)",),
    "hurstShirstS": ("(.*\w+hurst($|[\s+.*]))", "(.*\w+hirst($|[\s+.*]))"),
    "inchPinchAinschA": ("(.*\s*Inch.*)", "(.*Inch.*)", "(.*Insch.*)"),
    "ingS": ("(.*\w+ing($|[\s+.*]))",),
    "ingIingeS": ("(.+ing.+)", "(.*\w+ing($|[\s+.*]))"),
    "inverPinnerP": ("(.*\s*Inver.*)", "(.*\s*Inner.*)"),
    "keldAkeldS": ("(.*Keld.*)", "(.*\w+keld($|[\s+.*]))",),
    "kethSchethS": ("(.*\w+keth($|[\s+.*]))", "(.*\w+cheth($|[\s+.*]))"),
    "kilP": ("(.*\s*Kil.*)",),
    "kinP": ("(.*\s*Kin.*)",),
    "kingP": ("(.*\s*King.*)",),
    "kirkPkirkS": ("(.*\s*Kirk.*)", "(.*\w+kirk($|[\s+.*]))"),
    "knockPknockA": ("(.*\s*Knock.*)", "(.*Knock.*)",),
    "kylePkylesP": ("(.*\s*Kyle.*)", "(.*\s*Kyles.*)"),
    "lanPlhanPllanP": ("(.*\s*Lan.*)", "(.*\s*Lhan.*)", "(.*\s*Llan.*)"),
    "langP": ("(.*\s*Lang.*)",),
    "lawQlowQ": ("(.*[Ll]aw.*)", "(.*[Ll]ow.*)"),
    "leI": ("(.+-le.+)",),
    "leaSleySleighSleighA": ("(.*\w+lea($|[\s+.*]))", "(.*\w+ley($|[\s+.*]))", "(.*\w+leigh($|[\s+.*]))", "(.*Leigh.*)"),
    "linPllynA": ("(.*\s*Lin.*)", "(.*Llyn.*)"),
    "lingPlyngP": ("(.*\s*ling.*)", "(.*\s*lyng.*)"),
    "lochAloughAloughsA": ("(.*Loch.*)", "(.*Lough.*)", "(.*Loughs.*)"),
    "magnaA": ("(.*Magna.*)",),
    "mawrAmawrS": ("(.*Mawr.*)", "(.*\w+mawr($|[\s+.*]))",),
    "mereSmerS": ("(.*\w+mere($|[\s+.*]))", "(.*\w+mer($|[\s+.*]))"),
    "minsterAminsterS": ("(.*Minster.*)", "(.*\w+minster($|[\s+.*]))"),
    "moreS": ("(.*\w+more($|[\s+.*]))",),
    "mossPmossA": ("(.*\s*Moss.*)", "(.*Moss.*)"),
    "mouthS": ("(.*\w+mouth($|[\s+.*]))",),
    "mynyddPmynyddA": ("(.*\s*Mynydd.*)", "(.*Mynydd.*)",),
    "nanPnansPnancP": ("(.*\s*Nan.*)", "(.*\s*Nans.*)", "(.*\s*Nanc.*)"),
    "nantP": ("(.*\s*Nant.*)",),
    "nessS": ("(.*\w+ness($|[\s+.*]))",),
    "norP": ("(.*\s*Nor.*)",),
    "pantA": ("(.*Pant.*)",),
    "parvaA": ("(.*Parva.*)",),
    "penP": ("(.*\s*Pen.*)",),
    "pitP": ("(.*\s*Pit.*)",),
    "polP": ("(.*\s*Pol.*)",),
    "pontPpontS": ("(.*\s*Pont.*)", "(.*\w+pont($|[\s+.*]))"),
    "poolS": ("(.*\w+pool($|[\s+.*]))",),
    "portSportA": ("(.*\w+port($|[\s+.*]))", "(.*Port.*)"),
    "porthP": ("(.*\s*Porth.*)",),
    "shawAshawS": ("(.*Shaw.*)", "(.*\w+shaw($|[\s+.*]))"),
    "shepPshipP": ("(.*\s*Shep.*)", "(.*\s*Ship.*)"),
    "stanP": ("(.*\s*Stan)", ),
    "steadS": ("(.*\w+stead($|[\s+.*]))",),
    "sterS": ("(.*\w+ster($|[\s+.*]))",),
    "stokeAstokeS": ("(.*Stoke.*)", "(.*\w+stoke($|[\s+.*]))", ),
    "stowPstowAstowSstolS": ("(.*\s*Stow.*)", "(.*Stow.*)", "(.*\w+stow($|[\s+.*]))", "(.*\w+stol($|[\s+.*]))"),
    "strathP": ("(.*\s*Strath.*)",),
    "streatQstreetQ": ("(.*[Ss]treet.*)", "(.*[Ss]treat.*)"),
    "sudPsutP": ("(.*\s*Sud.*)", "(.*\s*Sut.*)"),
    "swinP": ("(.*\s*Swin.*)",),
    "tarnP": ("(.*\s*Tarn.*)",),
    "thorpPthorpePthorpeSthorpesS": ("(.*\s*Throp.*)", "(.*\s*Thrope.*)", "(.*\w+thorpe($|[\s+.*]))",
        "(.*\w+thorpes($|[\s+.*]))"),
    "thwaiteStwattStwattA": ("(.*\w+twaite($|[\s+.*]))", "(.*\w+twatt($|[\s+.*]))", "(.*Twatt.*)"),
    "tillyPtulliePtullouchPtilliPtulliP": ("(.*\s*Tilly.*)", "(.*\s*Tullie.*)",
        "(.*\s*Tullouch.*)", "(.*\s*Tilli.*)", "(.*\s*Tulli.*)"),
    "toftS": ("(.*\w+toft($|[\s+.*]))",),
    "treP": ("(.*\s*Tre.*)",),
    "treathQdreathS": ("(.*[Tt]reath.*)", "(.*\w+dreath($|[\s+.*]))",),
    "tunPtunStonStonI": ("(.*\s*tun.*)", "(.*\w+tun($|[\s+.*]))", "(.*\w+ton($|[\s+.*]))", "(.+ton.+)"),
    "uponI": ("(.+upon.+)",),
    "wealdPwoldS": ("(.*\s*Weald.*)", "(.*\w+wold($|[\s+.*]))"),
    "whelP": ("(.*\s*whel.*)",),
    "wickSwichSwychSwykeS": ("(.*\w+wick($|[\s+.*]))", "(.*\w+wich($|[\s+.*]))", "(.*\w+wych($|[\s+.*]))", "(.*\w+wyke($|[\s+.*]))"),
    "wickS": ("(.*\w+wick($|[\s+.*]))",),
    "winP": ("(.*\s*Win.*)", ),
    "worthSworthySwardineS": ("(.*\w+worth($|[\s+.*]))", "(.*\w+worthy($|[\s+.*]))", "(.*\w+wardine($|[\s+.*]))"),
    "ynysA": ("(.*Ynys.*)",),
}


# Pick only feature codes that correspond to towns and cities, see
# http://www.geonames.org/export/codes.html
geofeat_rules = ("PPL", "PPLA", "PPLA2", "PPLA3", "PPLA4", "PPLC", "PPLCH",
    "PPLF", "PPLG", "PPLH", "PPLL", "PPLQ", "PPLR", "PPLS", "PPLW")


# Language codes used here:
# https://en.wikipedia.org/wiki/List_of_generic_forms_in_place_names_in_the_United_Kingdom_and_Ireland
wiki_codes = {
    'Bry': 'Brythonic',
    'C': 'Cumbric',
    'K': 'Cornish',
    'I': 'Irish',
    'L': 'Latin',
    'ME': 'Middle English',
    'NF': 'Norman French',
    'OE': 'Old English',
    'ON': 'Old Norse',
    'P': 'Pictish',
    'SG': 'Scots Gaelic',
    'W': 'Welsh'
}

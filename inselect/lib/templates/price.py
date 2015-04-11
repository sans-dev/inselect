# -*- coding: UTF-8 -*-
"""Template for Ben Prices's Plectoptera microscope slides
"""

import re
from functools import partial

from inselect.lib.metadata import MetadataTemplate
from inselect.lib.parse import parse_matches_re, parse_int_gt0


template = MetadataTemplate(
{
    'Name': 'Price Plecoptera slides',
    'Object label': u'{catalogNumber}_{Location-value}_{Taxonomy-value}',
    'Cropped file suffix': u'.jpg',
    'Fields': [
        {
            "Name": "catalogNumber",
            "Label": "Catalog number",
            "URI": "http://rs.tdwg.org/dwc/terms/catalogNumber",
            "Mandatory": True,
            "Parser": partial(parse_matches_re, re.compile('^[0-9]{9}$'),
                        'Invalid value [{0}]: should contain nine digits'),
        },
        {
            "Name": "Location",
            "Mandatory": True,
            "ChoicesWithData" : [
                (u'Drawer 1', 804508),
                (u'Drawer 2', 804607),
                (u'Drawer 3', 804613),
                (u'Drawer 4', 804529),
                (u'Drawer 5', 804603),
                (u'Drawer 6', 118909),
                (u'Drawer 7', 804579),
                (u'Drawer 8', 804573),
                (u'Drawer 9', 804582),
                (u'Drawer 10', 804569),
                (u'Drawer 11', 804575),
                (u'Drawer 12', 804561),
                (u'Drawer 13', 804567),
                (u'Drawer 14', 804563),
                (u'Drawer 15', 804586),
                (u'Drawer 16', 804585),
                (u'Drawer 17', 804589),
                (u'Drawer 18', 804558),
                (u'Drawer 19', 804630),
                (u'Drawer 20', 804504),
                (u'Drawer 21', 804458),
                (u'Drawer 22', 804482),
                (u'Drawer 23', 804628),
                (u'Drawer 24', 804433),
                (u'Drawer 25', 804636),
                (u'Drawer 26', 118911),
                (u'Drawer 27', 118910),
                (u'Drawer 28', 804536),
                (u'Drawer 29', 804538),
                (u'Drawer 30', 804551),
                (u'Drawer 31', 804597),
                (u'Drawer 32', 804437),
                (u'Drawer 33', 92458),
                (u'Drawer 34', 804451),
                (u'Drawer 35', 804517),
                (u'Drawer 36', 804513),
                (u'Drawer 37', 118913),
                (u'Drawer 38', 804675),
                (u'Drawer 39', 118912),
                (u'Drawer 40', 804639),
                (u'Drawer 41', 804441),
                (u'Drawer 42', 804510),
                (u'Drawer 43', 804662),
                (u'Drawer 44', 804684),
                (u'Drawer 45', 804689),
                (u'Drawer 46', 804501),
                (u'Drawer 47', 804554),
                (u'Drawer 48', 804470),
                (u'Drawer 49', 804469),
                (u'Drawer 50', 804663),
                (u'Drawer 51', 804609),
                (u'Drawer 52', 804655),
                (u'Drawer 53', 804657),
                (u'Drawer 54', 804601),
            ],
        },
        {
            "Name": "Taxonomy",
            "Mandatory": True,
            "ChoicesWithData": [
                (u'[Antarctoperla]', 1257604),
                (u'[Austroperla]', 1257645),
                (u'[Chloroperla]', 1257707),
                (u'[Dinotoperla]', 1257492),
                (u'[Isopteryx]', 522431),
                (u'[Leptoperla]', 1257855),
                (u'[Leuctra]', 1257862),
                (u'[Nemoura]', 1257940),
                (u'[Paragripopteryx]', 1258069),
                (u'[Perlidae]', 521620),
                (u'[Plecoptera]', 371327),
                (u'[Tasmanoperla]', 1258214),
                (u'[Trinotoperla]', 1258227),
                (u'acicularis, Despax, [Isoperla]', 1257793),
                (u'acicularis, Despax, [Isoperla], T', 535022),
                (u'affinis, Morton, [Capnia]', 1257667),
                (u'albida, Kempny, [Leuctra], T', 1257864),
                (u'alticola, Despax, [Leuctra], T', 1257866),
                (u'ambigua, Despax, [Isoperla]', 1257795),
                (u'ambigua, Despax, [Isoperla], T', 535023),
                (u'anglica, Kimmins, [Rhabdiopteryx], T', 1258168),
                (u'apicalis, Kimmins, [Perlodinella], T', 1258117),
                (u'apicalis, Newman, [Chloroperla]', 522429),
                (u'armata, Kempny, [Leuctra]', 1257867),
                (u'aroucana, Kimmins, [Anacroneuria]', 1257586),
                (u'atra, Morton, [Capnia]', 1257669),
                (u'aurita, Navás, [Leuctra]', 1257868),
                (u'australica, Enderlein, [Leptoperla]', 1257856),
                (u'australica, Tillyard, [Spaniocerca]', 1258184),
                (u'australis, Tillyard, [Stenoperla]', 524328),
                (u'australis, Tillyard, [Trinotoperla]', 524354),
                (u'avicularis, Morton, [Nemoura]', 1257944),
                (u'barnardi, Tillyard, [Aphanicercella]', 1257613),
                (u'barnardi, Tillyard, [Aphanicercella], T', 535021),
                (u'bicaudata, Linnaeus, [Diura]', 1257738),
                (u'bifasciata, Kimmins, [Udamocercia], T', 1258241),
                (u'bifrons, Newman, [Zwicknia]', 1257670),
                (u'bituberculata, Kimmins, [Nemoura], T', 1257945),
                (u'borealis, Morton, [Amphinemura]', 1257568),
                (u'brachyptera, Despax, [Capnioneura], T', 1257692),
                (u'braueri, Kempny, [Leuctra]', 1257870),
                (u'brevipennis, Kimmins, [Dinotoperla], T', 1257494),
                (u'brevistyla, Ris, [Protonemura]', 1258133),
                (u'budtzi, Esben-Petersen, [Leuctra]', 1257871),
                (u'bullata, Kimmins, [Spaniocerca], T', 1258185),
                (u'californica, Newport, [Pteronarcys]', 1258162),
                (u'cambrica, Stephens, [Nemoura]', 1257948),
                (u'capensis, Tillyard, [Aphanicerca]', 1257609),
                (u'carinthiaca, Kempny, [Leuctra]', 1257875),
                (u'cephalotes, Curtis, [Dinocras]', 1257491),
                (u'cincta, Morton, [Leuctra]', 1257868),
                (u'cincta, Morton, [Leuctra], T', 1257874),
                (u'cinerea, Olivier, [Amphinemura]', 267300),
                (u'cingulata, Kempny, [Leuctra]', 1257875),
                (u'clymene, Newman, [Neoperla]', 1258002),
                (u'conica, Klapalek, [Capnia]', 1257681),
                (u'corsicana, Morton, [Protonemura]', 1258134),
                (u'corsicana, Morton, [Protonemura], T', 535026),
                (u'cylindrica, De Geer, [Perla]', 1257885),
                (u'cyrene, Newman, [Austroperla]', 1257646),
                (u'denticulata, Tillyard, [Aphanicercopsis]', 1257619),
                (u'despaxi, Mosely, [Leuctra]', 1257879),
                (u'digitata, Kempny, [Leuctra]', 1257880),
                (u'dorsalis, Kimmins, [Kyphopteryx], T', 1257853),
                (u'dubitans, Morton, [Nemoura]', 1257957),
                (u'erratica, Claassen, [Nemoura]', 1257958),
                (u'evansi, Kimmins, [Dinotoperla], T', 1257496),
                (u'exigua, Kimmins, [Leptoperla], T', 1257859),
                (u'falcata, Kimmins, [Protonemura], T', 1258135),
                (u'filigera, Kimmins, [Amphinemura], T', 1257570),
                (u'flavomaculata, Mosely, [Leuctra], T', 1257883),
                (u'flexuosa, Aubert, [Nemoura]', 1257959),
                (u'fontana, Kimmins, [Dinotoperla], T', 1257498),
                (u'fontium, Ris, [Dictyogenus]', 1257483),
                (u'fraterna, Morton, [Leuctra]', 1257884),
                (u'fulvescens, Hare, [Nesoperla]', 1258031),
                (u'fumosa, Stephens, [Nemoura]', 267300),
                (u'furcillatus, Tillyard, [Zelandobius]', 1258248),
                (u'fusca, Kimmins, [Dinotoperla], T', 1257499),
                (u'fusciventris, Stephens, [Leuctra]', 1257885),
                (u'geniculata, Stephens, [Leuctra]', 1257887),
                (u'grammatica subarmata, Despax, [Chloroperla]', 1257805),
                (u'grammatica subarmata, Despax, [Chloroperla], T', 1257824),
                (u'grammatica, Poda, [Isoperla]', 1257805),
                (u'griseipennis, Pictet, [Perla]', 1257815),
                (u'hamulata, Morton, [Isopteryx], T', 1257710),
                (u'handlirschi, Kempny, [Leuctra]', 1257890),
                (u'hingstoni, Kimmins, [Capnia], T', 1257677),
                (u'hippopus, Kempny, [Leuctra]', 1257891),
                (u'hrabei, Rauser, [Protonemura]', 1258136),
                (u'imhoffi, Pictet, [Besdolus]', 1257485),
                (u'inconspicua, Pictet, [Nemoura]', 1257987),
                (u'inermis, Kempny, [Leuctra]', 1257893),
                (u'insularis, Morton, [Isoperla]', 1257807),
                (u'intricata, Ris, [Protonemura]', 1258138),
                (u'intricatus, Pictet, [Perlodes]', 1258076),
                (u'kempnyi, Mosely, [Leuctra], T', 1257894),
                (u'klapaleki, Kempny, [Leuctra]', 1257885),
                (u'lamellosa, Despax, [Leuctra]', 1257898),
                (u'lateralis, Pictet, [Protonemura]', 1258139),
                (u'latipennis, Tillyard, [Notonemoura]', 1258042),
                (u'lunata, Kimmins, [Mesyatsia], T', 535025),
                (u'luteipes, Kimmins, [Amphinemura], T', 1257571),
                (u'manevali, Kimmins, [Isopteryx], T', 1257712),
                (u'marginata, Panzer, [Perla]', 1258094),
                (u'marginata, Pictet, [Nemoura]', 1257966),
                (u'maxima carlukiana, Klapalek, [Perla]', 1258085),
                (u'maxima, Scopoli, [Perla]', 1258095),
                (u'mclachlani, Kimmins, [Protonemura], T', 1258142),
                (u'meyeri, Pictet, [Protonemura]', 1258143),
                (u'microcephalus, Pictet, [Perlodes]', 1258110),
                (u'minima, Barnston, [Allocapnia], T', 535015),
                (u'minor, Kimmins, [Trinotoperla]', 1258232),
                (u'minuta, Klapalek, [Anacroneuria], T', 1257591),
                (u'minuta, Klapalek, [Tyrrhenoleuctra]', 1258239),
                (u'mirabilis, Martynov, [Protonemura]', 524320),
                (u'mishmica, Kimmins, [Protonemura], T', 1258145),
                (u'monspessulana, Despax, [Nemoura], T', 1257968),
                (u'montana, Despax, [Pachyleuctra]', 524298),
                (u'montana, Kimmins, [Capnia], T', 1257678),
                (u'montana, Kimmins, [Protonemura], T', 1258146),
                (u'mortoni, Kempny, [Leuctra]', 1257901),
                (u'mortoni, Klapalek, [Perlodes]', 1258111),
                (u'moselyi, Despax, [Isoperla], T', 535018),
                (u'moselyi, Despax, [Nemoura], T', 1257969),
                (u'moselyi, Morton, [Leuctra]', 1257902),
                (u'nebulosa, Linnaeus, [Taeniopteryx]', 1258213),
                (u'neglecta, Albarda, [Rhabdiopteryx]', 1258170),
                (u'nigra, Olivier, [Leuctra]', 1257904),
                (u'nigra, Pictet, [Capnia]', 1257681),
                (u'nigricoxa, Kimmins, [Dinotoperla], T', 1257500),
                (u'nigrifrons, Kimmins, [Cardioperla], T', 535016),
                (u'nimborella, Mosely, [Protonemura], T', 535019),
                (u'nimborum, Ris, [Protonemura]', 1258148),
                (u'nitida, Kimmins, [Neoperla], T', 1258017),
                (u'nitida, Pictet, [Protonemura]', 1258149),
                (u'nivata, Kimmins, [Trinotoperla], T', 1258233),
                (u'nubila, Kimmins, [Amphinemura], T', 1257572),
                (u'obscura, Zetteistedt, [Isoperla]', 1257815),
                (u'obtusa, Ris, [Nemoura]', 1257970),
                (u'occidentalis, Despax, [Protonemura]', 1258154),
                (u'opposita, Walker, [Dinotoperla], T', 535017),
                (u'oxylepis, Despax, [Isoperla]', 1257816),
                (u'oxylepis, Despax, [Isoperla], T', 535024),
                (u'pacifica, Banks, [Hesperoperla]', 1257510),
                (u'pedestris, Kimmins, [Capnia], T', 1257682),
                (u'perfecta, Walker, [Paranemoura], T', 535014),
                (u'pilosa, Despax, [Chloroperla]', 1257828),
                (u'pilosa, Despax, [Chloroperla], T', 1257818),
                (u'praecox, Morton, [Protonemura]', 1258151),
                (u'prasina, Newman, [Stenoperla]', 1258194),
                (u'prima, Kempny, [Leuctra]', 1257906),
                (u'pseudocingulata, Mendl, [Leuctra], T', 1257907),
                (u'pseudocylindrica, Despax, [Leuctra]', 1257908),
                (u'pulchella, Tillyard, [Desmonemoura]', 1257731),
                (u'putata, Newman, [Brachyptera]', 1257653),
                (u'pyrenaica, Mosely, [Protonemura], T', 1258152),
                (u'rectus, Kempny, [Diura]', 1257738),
                (u'rectus, Kempny, [Isogenus]', 1257738),
                (u'renata, Kimmins, [Amphinemura], T', 1257574),
                (u'reticulata, Kimmins, [Riekoperla], T', 535020),
                (u'ribauti, Despax, [Pachyleuctra]', 1258059),
                (u'risi, Despax, [Nemoura]', 1257958),
                (u'risi, Jacobson & Bianchi, [Protonemura]', 1258154),
                (u'risi, Morton, [Brachyptera]', 1257654),
                (u'rivulorum, Pictet, [Isoperla]', 1257819),
                (u'rosinae, Kempny, [Leuctra]', 1257909),
                (u'rubens, Klapalek, [Neoperla]', 524292),
                (u'rugosa, Kimmins, [Riekoperla], T', 535027),
                (u'scutigera, Kimmins, [Protonemura], T', 1258155),
                (u'serricauda, Kimmins, [Dinotoperla], T', 1257734),
                (u'seticornis, Klapalek, [Brachyptera]', 1257655),
                (u'sigma, Despax, [Nemoura]', 1257963),
                (u'signifera, Kempny, [Leuctra]', 1257912),
                (u'sinensis, Wu & Claassen, [Peltoperla]', 1258081),
                (u'sinuata, Ris, [Nemoura]', 1257979),
                (u'standfussi, Ris, [Amphinemura]', 1257575),
                (u'strandi, Kempny, [Chloroperla]', 1257805),
                (u'tasmanica, Kimmins, [Leptoperla], T', 1257860),
                (u'tasmanica, Tillyard, [Spaniocerca]', 524326),
                (u'teriolensis, Kempny, [Leuctra]', 1257914),
                (u'testacea, Hagen, [Phanoperla]', 1258125),
                (u'tibetana, Kimmins, [Capnia], T', 1257683),
                (u'tillyardi, Kimmins, [Spaniocerca]', 524327),
                (u'tillyardi, Kimmins, [Spaniocerca], T', 1258188),
                (u'torrentium, Pictet, [Chloroperla]', 1257717),
                (u'tragula, Kimmins, [Amphinemura], T', 1257576),
                (u'triangularis, Ris, [Amphinemura]', 1257577),
                (u'trifasciata, Pictet, [Brachyptera]', 1257656),
                (u'tripunctata, Scopoli, [Chloroperla]', 1257718),
                (u'tuberculata, Despax, [Protonemura]', 1258157),
                (u'uncata, Kimmins, [Filchneria], T', 1257768),
                (u'uniformis, Kimmins, [Dinotoperla], T', 1257735),
                (u'varia, Kimmins, [Leptoperla], T', 1257861),
                (u'variegata, Olivier, [Nemoura]', 1257950),
                (u'venosa, Stephens, [Chloroperla]', 1257805),
                (u'vidua, Klapalek, [Capnia]', 1257686),
                (u'viridinervis, Pictet, [Isoperla]', 1257828),
                (u'vitripennis, Burmeister, [Marthamea]', 1257921),
                (u'zelandica, Tillyard, [Spaniocerca]', 1258189),
            ],
        },
    ]
})

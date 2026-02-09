from enum import Enum
from typing import ClassVar


class BaseNpiEnum(Enum):
    pass


class NpiStateAbbreviation(BaseNpiEnum):
    """State/territory abbreviation (value) -> full name (.display_name)."""

    AA = "AA"
    AE = "AE"
    AK = "AK"
    AL = "AL"
    AP = "AP"
    AR = "AR"
    AS = "AS"
    AZ = "AZ"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DC = "DC"
    DE = "DE"
    FL = "FL"
    FM = "FM"
    GA = "GA"
    GU = "GU"
    HI = "HI"
    IA = "IA"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    MA = "MA"
    MD = "MD"
    ME = "ME"
    MH = "MH"
    MI = "MI"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MS = "MS"
    MT = "MT"
    NC = "NC"
    ND = "ND"
    NE = "NE"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NV = "NV"
    NY = "NY"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    PR = "PR"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VA = "VA"
    VI = "VI"
    VT = "VT"
    WA = "WA"
    WI = "WI"
    WV = "WV"
    WY = "WY"

    _display_names: ClassVar[dict[str, str]] = {
        "AA": "ARMED FORCES AMERICA",
        "AE": "ARMED FORCES EUROPE/CANADA/MIDDLE EAST/AFRICA",
        "AK": "ALASKA",
        "AL": "ALABAMA",
        "AP": "ARMED FORCES PACIFIC",
        "AR": "ARKANSAS",
        "AS": "AMERICAN SAMOA",
        "AZ": "ARIZONA",
        "CA": "CALIFORNIA",
        "CO": "COLORADO",
        "CT": "CONNECTICUT",
        "DC": "DISTRICT OF COLUMBIA",
        "DE": "DELAWARE",
        "FL": "FLORIDA",
        "FM": "MICRONESIA, FEDERATED STATES OF",
        "GA": "GEORGIA",
        "GU": "GUAM",
        "HI": "HAWAII",
        "IA": "IOWA",
        "ID": "IDAHO",
        "IL": "ILLINOIS",
        "IN": "INDIANA",
        "KS": "KANSAS",
        "KY": "KENTUCKY",
        "LA": "LOUISIANA",
        "MA": "MASSACHUSETTS",
        "MD": "MARYLAND",
        "ME": "MAINE",
        "MH": "MARSHALL ISLANDS",
        "MI": "MICHIGAN",
        "MN": "MINNESOTA",
        "MO": "MISSOURI",
        "MP": "MARIANA ISLANDS, NORTHERN",
        "MS": "MISSISSIPPI",
        "MT": "MONTANA",
        "NC": "NORTH CAROLINA",
        "ND": "NORTH DAKOTA",
        "NE": "NEBRASKA",
        "NH": "NEW HAMPSHIRE",
        "NJ": "NEW JERSEY",
        "NM": "NEW MEXICO",
        "NV": "NEVADA",
        "NY": "NEW YORK",
        "OH": "OHIO",
        "OK": "OKLAHOMA",
        "OR": "OREGON",
        "PA": "PENNSYLVANIA",
        "PR": "PUERTO RICO",
        "RI": "RHODE ISLAND",
        "SC": "SOUTH CAROLINA",
        "SD": "SOUTH DAKOTA",
        "TN": "TENNESSEE",
        "TX": "TEXAS",
        "UT": "UTAH",
        "VA": "VIRGINIA",
        "VI": "VIRGIN ISLANDS",
        "VT": "VERMONT",
        "WA": "WASHINGTON",
        "WI": "WISCONSIN",
        "WV": "WEST VIRGINIA",
        "WY": "WYOMING",
    }

    @property
    def display_name(self) -> str:
        """Full name for display, e.g. NY -> NEW YORK."""
        return self._display_names.get(self.value, self.value)


class NpiEnumerationType(BaseNpiEnum):
    NPI_1 = "NPI-1"
    NPI_2 = "NPI-2"


class NpiStatus(BaseNpiEnum):
    A = "ACTIVE"
    I = "INACTIVE"  # noqa
    P = "PENDING"
    R = "REJECTED"
    S = "SUSPENDED"
    T = "TERMINATED"
    U = "UNCLAIMED"
    W = "WITHDRAWN"
    X = "EXPIRED"
    Y = "DECEASED"


class NpiSex(BaseNpiEnum):
    M = "MALE"
    F = "FEMALE"
    X = "UNSPECIFIED"
    U = "UNDISCLOSED"


class NpiCountryAbbreviation(BaseNpiEnum):
    """Country code (value) -> full name in caps (.display_name), e.g. US -> UNITED STATES."""

    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CS = "CS"
    CU = "CU"
    CV = "CV"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    MG = "MG"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    ST = "ST"
    SV = "SV"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    XK = "XK"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"

    _display_names: ClassVar[dict[str, str]] = {
        "AD": "ANDORRA",
        "AE": "UNITED ARAB EMIRATES",
        "AF": "AFGHANISTAN",
        "AG": "ANTIGUA AND BARBUDA",
        "AI": "ANGUILLA",
        "AL": "ALBANIA",
        "AM": "ARMENIA",
        "AN": "NETHERLANDS ANTILLES",
        "AO": "ANGOLA",
        "AQ": "ANTARCTICA",
        "AR": "ARGENTINA",
        "AT": "AUSTRIA",
        "AU": "AUSTRALIA",
        "AW": "ARUBA",
        "AX": "ALAND ISLANDS",
        "AZ": "AZERBAIJAN",
        "BA": "BOSNIA AND HERZEGOVINA",
        "BB": "BARBADOS",
        "BD": "BANGLADESH",
        "BE": "BELGIUM",
        "BF": "BURKINA FASO",
        "BG": "BULGARIA",
        "BH": "BAHRAIN",
        "BI": "BURUNDI",
        "BJ": "BENIN",
        "BM": "BERMUDA",
        "BN": "BRUNEI DARUSSALAM",
        "BO": "BOLIVIA",
        "BR": "BRAZIL",
        "BS": "BAHAMAS",
        "BT": "BHUTAN",
        "BV": "BOUVET ISLAND",
        "BW": "BOTSWANA",
        "BY": "BELARUS",
        "BZ": "BELIZE",
        "CA": "CANADA",
        "CC": "COCOS (KEELING) ISLANDS",
        "CD": "CONGO, THE DEMOCRATIC REPUBLIC OF THE",
        "CF": "CENTRAL AFRICAN REPUBLIC",
        "CG": "CONGO",
        "CH": "SWITZERLAND",
        "CI": "IVORY COAST",
        "CK": "COOK ISLANDS",
        "CL": "CHILE",
        "CM": "CAMEROON",
        "CN": "CHINA",
        "CO": "COLOMBIA",
        "CR": "COSTA RICA",
        "CS": "SERBIA AND MONTENEGRO",
        "CU": "CUBA",
        "CV": "CAPE VERDE",
        "CX": "CHRISTMAS ISLAND",
        "CY": "CYPRUS",
        "CZ": "CZECH REPUBLIC",
        "DE": "GERMANY",
        "DJ": "DJIBOUTI",
        "DK": "DENMARK",
        "DM": "DOMINICA",
        "DO": "DOMINICAN REPUBLIC",
        "DZ": "ALGERIA",
        "EC": "ECUADOR",
        "EE": "ESTONIA",
        "EG": "EGYPT",
        "EH": "WESTERN SAHARA",
        "ER": "ERITREA",
        "ES": "SPAIN",
        "ET": "ETHIOPIA",
        "FI": "FINLAND",
        "FJ": "FIJI",
        "FK": "FALKLAND ISLANDS (MALVINAS)",
        "FO": "FAROE ISLANDS",
        "FR": "FRANCE",
        "GA": "GABON",
        "GB": "GREAT BRITAIN",
        "GD": "GRENADA",
        "GE": "GEORGIA",
        "GF": "FRENCH GUIANA",
        "GG": "GUERNSEY",
        "GH": "GHANA",
        "GI": "GIBRALTAR",
        "GM": "GAMBIA",
        "GN": "GUINEA",
        "GP": "GUADELOUPE",
        "GQ": "EQUATORIAL GUINEA",
        "GR": "GREECE",
        "GS": "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
        "GT": "GUATEMALA",
        "GW": "GUINEA-BISSAU",
        "GY": "GUYANA",
        "HK": "HONG KONG",
        "HM": "HEARD ISLAND AND MCDONALD ISLANDS",
        "HN": "HONDURAS",
        "HR": "CROATIA",
        "HT": "HAITI",
        "HU": "HUNGARY",
        "ID": "INDONESIA",
        "IE": "IRELAND",
        "IL": "ISRAEL",
        "IM": "ISLE OF MAN",
        "IN": "INDIA",
        "IO": "BRITISH INDIAN OCEAN TERRITORY",
        "IQ": "IRAQ",
        "IR": "IRAN, ISLAMIC REPUBLIC OF",
        "IS": "ICELAND",
        "IT": "ITALY",
        "JE": "JERSEY",
        "JM": "JAMAICA",
        "JO": "JORDAN",
        "JP": "JAPAN",
        "KE": "KENYA",
        "KG": "KYRGYZSTAN",
        "KH": "CAMBODIA",
        "KI": "KIRIBATI",
        "KM": "COMOROS",
        "KN": "SAINT KITTS AND NEVIS",
        "KP": "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
        "KR": "KOREA, REPUBLIC OF",
        "KW": "KUWAIT",
        "KY": "CAYMAN ISLANDS",
        "KZ": "KAZAKHSTAN",
        "LA": "LAO PEOPLE'S DEMOCRATIC REPUBLIC",
        "LB": "LEBANON",
        "LC": "SAINT LUCIA",
        "LI": "LIECHTENSTEIN",
        "LK": "SRI LANKA",
        "LR": "LIBERIA",
        "LS": "LESOTHO",
        "LT": "LITHUANIA",
        "LU": "LUXEMBOURG",
        "LV": "LATVIA",
        "LY": "LIBYAN ARAB JAMAHIRIYA",
        "MA": "MOROCCO",
        "MC": "MONACO",
        "MD": "MOLDOVA, REPUBLIC OF",
        "MG": "MADAGASCAR",
        "MK": "MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
        "ML": "MALI",
        "MM": "MYANMAR",
        "MN": "MONGOLIA",
        "MO": "MACAO",
        "MQ": "MARTINIQUE",
        "MR": "MAURITANIA",
        "MS": "MONTSERRAT",
        "MT": "MALTA",
        "MU": "MAURITIUS",
        "MV": "MALDIVES",
        "MW": "MALAWI",
        "MX": "MEXICO",
        "MY": "MALAYSIA",
        "MZ": "MOZAMBIQUE",
        "NA": "NAMIBIA",
        "NC": "NEW CALEDONIA",
        "NE": "NIGER",
        "NF": "NORFOLK ISLAND",
        "NG": "NIGERIA",
        "NI": "NICARAGUA",
        "NL": "NETHERLANDS",
        "NO": "NORWAY",
        "NP": "NEPAL",
        "NR": "NAURU",
        "NU": "NIUE",
        "NZ": "NEW ZEALAND",
        "OM": "OMAN",
        "PA": "PANAMA",
        "PE": "PERU",
        "PF": "FRENCH POLYNESIA",
        "PG": "PAPUA NEW GUINEA",
        "PH": "PHILIPPINES",
        "PK": "PAKISTAN",
        "PL": "POLAND",
        "PM": "SAINT PIERRE AND MIQUELON",
        "PN": "PITCAIRN",
        "PS": "PALESTINIAN TERRITORY, OCCUPIED",
        "PT": "PORTUGAL",
        "PW": "PALAU",
        "PY": "PARAGUAY",
        "QA": "QATAR",
        "RE": "REUNION",
        "RO": "ROMANIA",
        "RU": "RUSSIAN FEDERATION",
        "RW": "RWANDA",
        "SA": "SAUDI ARABIA",
        "SB": "SOLOMON ISLANDS",
        "SC": "SEYCHELLES",
        "SD": "SUDAN",
        "SE": "SWEDEN",
        "SG": "SINGAPORE",
        "SH": "SAINT HELENA",
        "SI": "SLOVENIA",
        "SJ": "SVALBARD AND JAN MAYEN",
        "SK": "SLOVAKIA",
        "SL": "SIERRA LEONE",
        "SM": "SAN MARINO",
        "SN": "SENEGAL",
        "SO": "SOMALIA",
        "SR": "SURINAME",
        "ST": "SAO TOME AND PRINCIPE",
        "SV": "EL SALVADOR",
        "SY": "SYRIAN ARAB REPUBLIC",
        "SZ": "SWAZILAND",
        "TC": "TURKS AND CAICOS ISLANDS",
        "TD": "CHAD",
        "TF": "FRENCH SOUTHERN TERRITORIES",
        "TG": "TOGO",
        "TH": "THAILAND",
        "TJ": "TAJIKISTAN",
        "TK": "TOKELAU",
        "TL": "TIMOR-LESTE",
        "TM": "TURKMENISTAN",
        "TN": "TUNISIA",
        "TO": "TONGA",
        "TR": "TURKEY",
        "TT": "TRINIDAD AND TOBAGO",
        "TV": "TUVALU",
        "TW": "TAIWAN",
        "TZ": "TANZANIA, UNITED REPUBLIC OF",
        "UA": "UKRAINE",
        "UG": "UGANDA",
        "UM": "UNITED STATES MINOR OUTLYING ISLANDS",
        "US": "UNITED STATES",
        "UY": "URUGUAY",
        "UZ": "UZBEKISTAN",
        "VA": "HOLY SEE (VATICAN CITY STATE)",
        "VC": "SAINT VINCENT AND THE GRENADINES",
        "VE": "VENEZUELA",
        "VG": "VIRGIN ISLANDS, BRITISH",
        "VN": "VIET NAM",
        "VU": "VANUATU",
        "WF": "WALLIS AND FUTUNA",
        "WS": "SAMOA",
        "XK": "KOSOVO",
        "YE": "YEMEN",
        "YT": "MAYOTTE",
        "ZA": "SOUTH AFRICA",
        "ZM": "ZAMBIA",
        "ZW": "ZIMBABWE",
    }

    @property
    def display_name(self) -> str:
        """Full name in caps for display, e.g. US -> UNITED STATES."""
        return self._display_names.get(self.value, self.value)

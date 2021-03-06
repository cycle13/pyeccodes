def load(h):
    return ({'abbr': 'cin',
             'code': 1,
             'title': 'CIN Convective inhibition',
             'units': 'J kg**-1'},
            {'abbr': 'orog', 'code': 2, 'title': 'OROG Orography', 'units': 'm'},
            {'abbr': 'zust',
             'code': 3,
             'title': 'ZUST Friction velocity',
             'units': 'm s**-1'},
            {'abbr': 'mean2t',
             'code': 4,
             'title': 'MEAN2T Mean temperature at 2 metres',
             'units': 'K'},
            {'abbr': 'mean10ws',
             'code': 5,
             'title': 'MEAN10WS Mean of 10 metre wind speed',
             'units': 'm s**-1'},
            {'abbr': 'meantcc',
             'code': 6,
             'title': 'MEANTCC Mean total cloud cover',
             'units': '0 - 1'},
            {'abbr': 'dl', 'code': 7, 'title': 'DL Lake depth', 'units': 'm'},
            {'abbr': 'lmlt',
             'code': 8,
             'title': 'LMLT Lake mix-layer temperature',
             'units': 'K'},
            {'abbr': 'lmld',
             'code': 9,
             'title': 'LMLD Lake mix-layer depth',
             'units': 'm'},
            {'abbr': 'lblt',
             'code': 10,
             'title': 'LBLT Lake bottom temperature',
             'units': 'K'},
            {'abbr': 'ltlt',
             'code': 11,
             'title': 'LTLT Lake total layer temperature',
             'units': 'K'},
            {'abbr': 'lshf',
             'code': 12,
             'title': 'LSHF Lake shape factor',
             'units': 'dimensionless'},
            {'abbr': 'lict',
             'code': 13,
             'title': 'LICT Lake ice temperature',
             'units': 'K'},
            {'abbr': 'licd', 'code': 14, 'title': 'LICD Lake ice depth', 'units': 'm'},
            {'abbr': 'dndzn',
             'code': 15,
             'title': 'DNDZN Minimum vertical gradient of refractivity inside trapping '
                      'layer',
             'units': 'm**-1'},
            {'abbr': 'dndza',
             'code': 16,
             'title': 'DNDZA Mean vertical gradient of refractivity inside trapping layer',
             'units': 'm**-1'},
            {'abbr': 'dctb', 'code': 17, 'title': 'DCTB Duct base height', 'units': 'm'},
            {'abbr': 'tplb',
             'code': 18,
             'title': 'TPLB Trapping layer base height',
             'units': 'm'},
            {'abbr': 'tplt',
             'code': 19,
             'title': 'TPLT Trapping layer top height',
             'units': 'm'},
            {'abbr': 'degm10l',
             'code': 20,
             'title': '-10 degrees C isothermal level',
             'units': 'm'},
            {'abbr': 'fdir',
             'code': 21,
             'title': 'FDIR Total sky direct solar radiation at surface',
             'units': 'J m**-2'},
            {'abbr': 'cdir',
             'code': 22,
             'title': 'CDIR Clear-sky direct solar radiation at surface',
             'units': 'J m**-2'},
            {'abbr': 'cbh', 'code': 23, 'title': 'CBH Cloud base height', 'units': 'm'},
            {'abbr': 'deg0l',
             'code': 24,
             'title': 'DEG0L Zero degree level',
             'units': 'm'},
            {'abbr': 'hvis',
             'code': 25,
             'title': 'HVIS Horizontal visibility',
             'units': 'm'},
            {'abbr': 'mx2t3',
             'code': 26,
             'title': 'MX2T3 Maximum temperature at 2 metres in the last 3 hours',
             'units': 'K'},
            {'abbr': 'mn2t3',
             'code': 27,
             'title': 'MN2T3 Minimum temperature at 2 metres in the last 3 hours',
             'units': 'K'},
            {'abbr': '10fg3',
             'code': 28,
             'title': '10FG3 10 metre wind gust in the last 3 hours',
             'units': 'm s**-1'},
            {'abbr': 'i10fg',
             'code': 29,
             'title': 'I10FG Instantaneous 10 metre wind gust',
             'units': 'm s**-1'},
            {'abbr': 'sm', 'code': 39, 'title': 'SM Soil Moisture', 'units': 'kg m**-3'},
            {'abbr': 'swi1',
             'code': 40,
             'title': 'SWI1 Soil wetness index in layer 1',
             'units': 'dimensionless'},
            {'abbr': 'swi2',
             'code': 41,
             'title': 'SWI2 Soil wetness index in layer 2',
             'units': 'dimensionless'},
            {'abbr': 'swi3',
             'code': 42,
             'title': 'SWI3 Soil wetness index in layer 3',
             'units': 'dimensionless'},
            {'abbr': 'swi4',
             'code': 43,
             'title': 'SWI4 Soil wetness index in layer 4',
             'units': 'dimensionless'},
            {'abbr': 'capes',
             'code': 44,
             'title': 'CAPES Convective available potential energy shear',
             'units': 'm**2 s**-2'},
            {'abbr': 'hcct',
             'code': 46,
             'title': 'HCCT Height of convective cloud top',
             'units': 'm'},
            {'abbr': 'hwbt0',
             'code': 47,
             'title': 'HWBT0 Height of zero-degree wet-bulb temperature',
             'units': 'm'},
            {'abbr': 'hwbt1',
             'code': 48,
             'title': 'HWBT1 Height of one-degree wet-bulb temperature',
             'units': 'm'},
            {'abbr': 'litoti',
             'code': 50,
             'title': 'LITOTI Instantaneous total lightning flash density',
             'units': 'km**-2 day**-1'},
            {'abbr': 'litota1',
             'code': 51,
             'title': 'LITOTA1 Averaged total lightning flash density in the last hour',
             'units': 'km**-2 day**-1'},
            {'abbr': 'licgi',
             'code': 52,
             'title': 'LICGI Instantaneous cloud-to-ground lightning flash density',
             'units': 'km**-2 day**-1'},
            {'abbr': 'licga1',
             'code': 53,
             'title': 'LICGA1 Averaged cloud-to-ground lightning flash density in the '
                      'last hour',
             'units': 'km**-2 day**-1'},
            {'abbr': 'smnnob',
             'code': 70,
             'title': 'SMNNOB SMOS observed soil moisture retrieved using neural network',
             'units': 'm**3 m**-3'},
            {'abbr': 'smnner',
             'code': 71,
             'title': 'SMNNER SMOS observed soil moisture uncertainty retrieved using '
                      'neural network',
             'units': 'm**3 m**-3'},
            {'abbr': 'smnnrfi',
             'code': 72,
             'title': 'SMNNRFI SMOS radio frequency interference probability',
             'units': '%'},
            {'abbr': 'smnnnb',
             'code': 73,
             'title': 'SMNNNB SMOS number of observations per grid point',
             'units': 'dimensionless'},
            {'abbr': 'smnntim',
             'code': 74,
             'title': 'SMNNTIM SMOS observation time for the satellite soil moisture data',
             'units': 'hour'},
            {'abbr': 'gppbfas',
             'code': 78,
             'title': 'GPPBFAS GPP coefficient from Biogenic Flux Adjustment System',
             'units': 'dimensionless'},
            {'abbr': 'recbfas',
             'code': 79,
             'title': 'RECBFAS Rec coefficient from Biogenic Flux Adjustment System',
             'units': 'dimensionless'},
            {'abbr': 'aco2nee',
             'code': 80,
             'title': 'ACO2NEE Accumulated Carbon Dioxide Net Ecosystem Exchange',
             'units': 'kg m**-2'},
            {'abbr': 'aco2gpp',
             'code': 81,
             'title': 'ACO2GPP Accumulated Carbon Dioxide Gross Primary Production',
             'units': 'kg m**-2'},
            {'abbr': 'aco2rec',
             'code': 82,
             'title': 'ACO2REC Accumulated Carbon Dioxide Ecosystem Respiration',
             'units': 'kg m**-2'},
            {'abbr': 'fco2nee',
             'code': 83,
             'title': 'FCO2NEE Flux of Carbon Dioxide Net Ecosystem Exchange',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'fco2gpp',
             'code': 84,
             'title': 'FCO2GPP Flux of Carbon Dioxide Gross Primary Production',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'fco2rec',
             'code': 85,
             'title': 'FCO2REC Flux of Carbon Dioxide Ecosystem Respiration',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'tcslw',
             'code': 88,
             'title': 'TCSLW Total column supercooled liquid water',
             'units': 'kg m**-2'},
            {'abbr': 'tcrw',
             'code': 89,
             'title': 'TCRW Total column rain water',
             'units': 'kg m**-2'},
            {'abbr': 'tcsw',
             'code': 90,
             'title': 'TCSW Total column snow water',
             'units': 'kg m**-2'},
            {'abbr': 'ccf',
             'code': 91,
             'title': 'CCF Canopy cover fraction',
             'units': '0 - 1'},
            {'abbr': 'stf',
             'code': 92,
             'title': 'STF Soil texture fraction',
             'units': '0 - 1'},
            {'abbr': 'swv',
             'code': 93,
             'title': 'SWV Volumetric soil moisture',
             'units': 'm**3 m**-3'},
            {'abbr': 'ist', 'code': 94, 'title': 'IST Ice temperature', 'units': 'K'},
            {'abbr': 'ceil', 'code': 109, 'title': 'CEIL Ceiling', 'units': 'm'},
            {'abbr': 'kx', 'code': 121, 'title': 'KX K index', 'units': 'K'},
            {'abbr': 'totalx',
             'code': 123,
             'title': 'TOTALX Total totals index',
             'units': 'K'},
            {'abbr': 'ssrdc',
             'code': 129,
             'title': 'SSRDC Surface solar radiation downward clear-sky',
             'units': 'J m**-2'},
            {'abbr': 'strdc',
             'code': 130,
             'title': 'STRDC Surface thermal radiation downward clear-sky',
             'units': 'J m**-2'},
            {'abbr': 'u10n',
             'code': 131,
             'title': 'U10N Neutral wind at 10 m u-component',
             'units': 'm s**-1'},
            {'abbr': 'v10n',
             'code': 132,
             'title': 'V10N Neutral wind at 10 m v-component',
             'units': 'm s**-1'},
            {'abbr': 'vtnowd',
             'code': 134,
             'title': 'VTNOWD V-tendency from non-orographic wave drag',
             'units': 'm s**-2'},
            {'abbr': 'utnowd',
             'code': 136,
             'title': 'UTNOWD U-tendency from non-orographic wave drag',
             'units': 'm s**-2'},
            {'abbr': 'st', 'code': 139, 'title': 'ST Soil Temperature', 'units': 'K'},
            {'abbr': 'sd',
             'code': 141,
             'title': 'SD Snow depth water equivalent',
             'units': 'kg m**-2'},
            {'abbr': 'sf',
             'code': 144,
             'title': 'SF Snow Fall water equivalent',
             'units': 'kg m**-2'},
            {'abbr': 'tcc', 'code': 164, 'title': 'TCC Total Cloud Cover', 'units': '%'},
            {'abbr': 'cap',
             'code': 170,
             'title': 'CAP Field capacity',
             'units': 'kg m**-3'},
            {'abbr': 'wilt',
             'code': 171,
             'title': 'WILT Wilting point',
             'units': 'kg m**-3'},
            {'abbr': 'fzra',
             'code': 216,
             'title': 'FZRA Accumulated freezing rain',
             'units': 'm'},
            {'abbr': 'ilspf',
             'code': 217,
             'title': 'ILSPF Instantaneous large-scale surface precipitation fraction',
             'units': '0 - 1'},
            {'abbr': 'crr',
             'code': 218,
             'title': 'CRR Convective rain rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'lsrr',
             'code': 219,
             'title': 'LSRR Large scale rain rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'csfr',
             'code': 220,
             'title': 'CSFR Convective snowfall rate water equivalent',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'lssfr',
             'code': 221,
             'title': 'LSSFR Large scale snowfall rate water equivalent',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'mxtpr3',
             'code': 222,
             'title': 'MXTPR3 Maximum total precipitation rate in the last 3 hours',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'mntpr3',
             'code': 223,
             'title': 'MNTPR3 Minimum total precipitation rate in the last 3 hours',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'mxtpr6',
             'code': 224,
             'title': 'MXTPR6 Maximum total precipitation rate in the last 6 hours',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'mntpr6',
             'code': 225,
             'title': 'MNTPR6 Minimum total precipitation rate in the last 6 hours',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'mxtpr',
             'code': 226,
             'title': 'MXTPR Maximum total precipitation rate since previous '
                      'post-processing',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'mntpr',
             'code': 227,
             'title': 'MNTPR Minimum total precipitation rate since previous '
                      'post-processing',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 'tp',
             'code': 228,
             'title': 'TP Total Precipitation',
             'units': 'kg m**-2'},
            {'abbr': 'smos_tb_cdfa',
             'code': 229,
             'title': 'SMOS_TB_CDFA SMOS first Brightness Temperature Bias Correction '
                      'parameter',
             'units': 'K'},
            {'abbr': 'smos_tb_cdfb',
             'code': 230,
             'title': 'SMOS_TB_CDFB SMOS second Brightness Temperature Bias Correction '
                      'parameter',
             'units': 'dimensionless'},
            {'abbr': '200U',
             'code': 239,
             'title': '200 metre U wind component',
             'units': 'm s**-1'},
            {'abbr': '200V',
             'code': 240,
             'title': '200 metre V wind component',
             'units': 'm s**-1'},
            {'abbr': '200SI',
             'code': 241,
             'title': '200 metre wind speed',
             'units': 'm s**-1'},
            {'abbr': 'fdif',
             'code': 242,
             'title': 'FDIF Surface solar radiation diffuse total sky',
             'units': 'J m**-2'},
            {'abbr': 'cdif',
             'code': 243,
             'title': 'CDIF Surface solar radiation diffuse clear-sky',
             'units': 'J m**-2'},
            {'abbr': 'aldr',
             'code': 244,
             'title': 'ALDR Surface albedo of direct radiation',
             'units': '0 - 1'},
            {'abbr': 'aldf',
             'code': 245,
             'title': 'ALDF Surface albedo of diffuse radiation',
             'units': '0 - 1'},
            {'abbr': '100u',
             'code': 246,
             'title': '100U 100 metre U wind component',
             'units': 'm s**-1'},
            {'abbr': '100v',
             'code': 247,
             'title': '100V 100 metre V wind component',
             'units': 'm s**-1'},
            {'abbr': '100si',
             'code': 249,
             'title': '100SI 100 metre wind speed',
             'units': 'm s**-1'},
            {'abbr': 'irrfr',
             'code': 250,
             'title': 'IRRFR Irrigation fraction',
             'units': 'Proportion'},
            {'abbr': 'pev',
             'code': 251,
             'title': 'PEV Potential evaporation',
             'units': 'm'},
            {'abbr': 'irr', 'code': 252, 'title': 'IRR Irrigation', 'units': 'm'},
            {'abbr': 'ascat_sm_cdfa',
             'code': 253,
             'title': 'ASCAT_SM_CDFA ASCAT first soil moisture CDF matching parameter',
             'units': 'm**3 m**-3'},
            {'abbr': 'ascat_sm_cdfb',
             'code': 254,
             'title': 'ASCAT_SM_CDFB ASCAT second soil moisture CDF matching parameter',
             'units': 'dimensionless'})

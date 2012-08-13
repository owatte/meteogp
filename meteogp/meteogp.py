#!/usr/bin/env python
# -*- coding: UTF8 -*-

URL_FEED_VIGILANCE = "http://www.meteo.gp/rss/rss_vigi.xml"

USAGE = '''retrieves weather alert level for French West Indies and French Guyane from meteo.gp website
 
USAGE :
vigilance.py <area_alias>
where area_alias in :
****************************************
*  area        * aliases               *
****************************************
* Iles du Nord * idn, ilesdunord, nord *
* Guadeloupe   * gp, guadeloupe, 971   *
* Martinique   * mq, martinique, 972   *
* Guyane       * gf, guyane, 974       *
****************************************

exemple for the Guadeloupe:
vigilance.py 971
vigilance.py gp
'''

COUNTRY_ALIASES = [ 
    ['IlesduNord', ['idn', 'ilesdunord', 'nord']],
    ['Guadeloupe', ['gp', 'guadeloupe', '971']], 
    ['Martinique',['mq', 'martinique', '972' ]],
    ['Guyane', ['gf', 'guyane', '974']]
]    

import feedparser

def get_vigilance_levels(url_feed_vigilance):
    d = feedparser.parse(url_feed_vigilance)
    vigilance = d['entries'][0].summary
    bruit = [u'\xa0', u'\n', ' ']
    for b in bruit :
        vigilance = vigilance.replace(b, '')
    vigilances = vigilance.split('.')

    vigilance = {}
    # alert level
    for dataz in vigilances:
        if (":" in dataz): 
            data = dataz.split(":")
            area = data[0]
            level = data[1]
            vigilance[area] = level
    # feed date
    vigilance['updated'] = d['entries'][0].updated        
    return vigilance

def run():
    import sys
    if len(sys.argv)==1 or sys.argv[1] in ['-h', '--help']:
        print USAGE
    else:
        url_feed_vigilance = URL_FEED_VIGILANCE
        wanted = sys.argv[1].lower()
        vigilance = get_vigilance_levels(url_feed_vigilance)              
        area = [ alias[0] for alias in COUNTRY_ALIASES if wanted in alias[1] ]

        if len(area) > 0 and vigilance.has_key(area[0]):
            result = ''.join([
                vigilance[area[0]], 
                ' (',
                vigilance['updated'],
                ')'
            ])
        else :
            result = ''.join([
                'ERREUR : no data for ', 
                sys.argv[1],
                '\n',
                USAGE
            ])
        print result

if __name__ == '__main__':
    run()

    


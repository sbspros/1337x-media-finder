from common.BaseClass import BaseClass
from models.PlexSection import PlexSection
from models.MediaFinder import MediaFinder
from views.DisplayTorrentLinks import DisplayTorrnetLinks

import os
import inspect

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" A ulitity to find and update plex media"""

if __name__ == '__main__':
    bc=BaseClass('config.ini')
    plex_sections={
    "Bonnie's Tv",
    "Richard's Tv",
    "Common - TV",    }

    plex_shows={
        "Bonnie's Tv":["Blue Bloods",'1883','Bridgerton','Becoming Elizabeth',
            'Chicago Fire','Chicago Med','The Crown','The Curse of Oak Island',
            'Fire Country','For Life','The Gilded Age','Godfather of Harlem',
            'The Good Doctor','Good Sam','House of Dragon',
            'The Last Days of Ptolemy Grey','Law & Order: Organized Crime',
            'Law & Order: Special Victims Unit','Mare of Easttown',
            'Mayor of Kingstown','A Million Little Things','NCIS',
            'New Amsterdam','Nine Perfect Strangers','The Resident','Shantaram',
            'The White Queen','Devil in Suburbia'],
        "Common - TV":["Tulsa King","Alone",'Australian Survivor',"Bering Sea Gold",'Clarice',
            'The Equalizer','Gold Rush','Good Bones: Risky Business',"Hell's Kitchen",
            'MasterChef (US)','MasterChef Australia','Next Level Chef','Reacher','Survivor',
            'Yellowstone'],
        "Richard's Tv":["The Peripheral","American Gods","American Horror Stories","American Horror Story",
            "Archive 81",'The Boys','Cypher','Debris','Evil','The Last Kingdom','Loki',
            "Andor",'The Mandalorian','Servant','The Lord of the Rings: The Rings of Power',
            "Obi-Wan Kenobi",'The Old Man','Outer Range','Peaky Blinder','Power Book III: Raising Kanan',
            'Prodigal Son','Raised by Wolves','Reservation Dogs','Resident Alien',
            'She-Hulk: Attorney at Law','Star Trek: Discovery','Star Trek: Picard',
            'The Terminal List','Vigil','Vikings: Valhalla','WandaVision','Yellowjackets'],

    }
    plex_url=bc.ini_file.config['Plex']['server']     
    plex_token=os.getenv("PLEX_TOKEN")
    plex_connect=PlexSection(bc,plex_token,plex_url)
    media_connection=MediaFinder(bc)
    display_torrents=DisplayTorrnetLinks(bc)


    for section in plex_sections:
        for show in plex_shows[section]:
            section_shows=plex_connect.section_shows(section,show)

            ## Current Season
            section_shows['episode']=str(int(section_shows['episode']+1))
            search_str=media_connection.show_to_search(section_shows)
            display_torrents.display_links( media_connection.query('tv',search_str),search_str)

            ## Next Season
            section_shows['episode']='02'
            section_shows['season']=str(int(section_shows['season']+1))
            search_str=media_connection.show_to_search(section_shows)
            display_torrents.display_links( media_connection.query('tv',search_str),search_str)

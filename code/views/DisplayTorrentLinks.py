from common.BaseClass import BaseClass
from exceptions.GetRequestException import GetRequestException
import requests

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"


class DisplayTorrnetLinks(BaseClass):
    """   """

    def __init__(self,bc:BaseClass)->None:
        self._bc=bc
        self._bc.log.info("\tStarting class "+self.__class__.__name__) 

    def display_mag_link(self,links):
        """A function to display a list of torrent and the magnetLink for them"""

        print( "{0}\t{1}\t{2}".format('    Sizes','Seeds','Link'))
        print( "{0}\t{1}\t{2}".format('---------','-----','----------------------------------------------------------------------------------------------'))
        for show in links:
            if int(show['seeders'])>0:
                torrent=requests.get(show['link'])
                if int(torrent.status_code) >= 200 and int(torrent.status_code) <= 299:
                    "find the magnet link to use as a download"
                    starting_point=torrent.text.find("magnet")
                    mag_link_start=torrent.text[starting_point:starting_point+200]
                    end_point=mag_link_start.find('"')
                    mag_link=mag_link_start[:end_point]

                    print( "{0}\t{1}\t{2:101s} **{3}".format(show['size'].rjust(9),\
                        show['seeders'].rjust(5),show['name'],mag_link))
                else:
                    self._bc.log.error("\tCould not open link:{link}".format(link=show['link']))
                    raise GetRequestException

    def display_links(self,links,title):
        """A function to display a list of torrent and the magnetLink for them"""
        if len(links)>0:
            print(len(links))
            print(title)
            print( "{0}\t{1}\t{2}".format('    Sizes','Seeds','Link'))
            print( "{0}\t{1}\t{2}".format('---------','-----','----------------------------------------------------------------------------------------------'))
            #print(links)
            try:
                for show in links:
                #    print(show)
                    if int(show['seeders'])>0:
                        print( "{0}\t{1}\t{2}".format(show['size'].rjust(9),\
                            show['seeders'].rjust(5),show['link']))
            except:
                pass
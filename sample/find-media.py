from common.BaseClass import BaseClass
from models.MediaFinder import MediaFinderFailed
from views.DisplayTorrentLinks import DisplayTorrnetLinks
import argparse
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"
""" This is the commandline controller to search for torrent media on 1337x"""

if __name__ == '__main__':
    bc=BaseClass('config.ini')     
    parser = argparse.ArgumentParser(description = 'This program search 1337x for media torrents')

    parser.add_argument('-q',
        '--query', 
        type=str,
        help='What are you looking for')
    
    parser.add_argument('-m', 
        '--media_type',
        type=str, 
        help='media type {tv,movies,other}')

    parser.add_argument('-s', 
        '--search_type',
        type=str, 
        help='media type {tv,movies,other}')

    parser.add_argument('-l', 
        '--link_style',
        type=str, 
        default='link',
        help='what type of link to return {link,magnet}')        

    arg = parser.parse_args()
    try:
        ## use indirection to call search
        imp=__import__('models.MediaFinder',\
                        globals=None,\
                        locals=None,\
                        fromlist='MediaFinder'\
                        ,level=0)
        
        ## creat instance of class
        cls=getattr(imp,'MediaFinder',None)
        media_finder=cls(bc)

        if arg.query == None:
            ## this will run MediaFinder.query()
            method=getattr(media_finder,arg.search_type)
            links=method(arg.media_type)            
        else:
            ## this will run MediaFinder.{top(),trending(),popular()}
            method=getattr(media_finder,'query')
            links=method(arg.media_type,arg.query)
        dl=DisplayTorrnetLinks(bc)
        if arg.link_style=='link':
            dl.display_links(links)
        else:
            dl.display_mag_link(links)    

    except  MediaFinderFailed:
        exit()
    except:
        bc.log.error("\t"+":"+traceback.format_exc()) 
        exit()

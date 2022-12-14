from tables.TvShowTorrent import TvShowTorrent, TvTorrentParsingError
from common.BaseClass import BaseClass
from models.MediaFinder import MediaFinder
import pytest
bc = BaseClass('./config.ini')

def test_add_show()->None:
    torrent={
        'name':'Test torrent',
        'torrentId':'12345',
        'link':'test.link',
        'seeders':'23',
        'leechers':'34',
        'size':'2.1 GB',
        'time':'date string',
        'uploader':'up name',
        'uploaderLink':'up link',
        }
    show_torrent=TvShowTorrent()
    show_torrent.parse_data(torrent)
    assert show_torrent._torrent_id == '12345'

def test_filter_results()->None:
    show_list=[]
    bc = BaseClass('./config.ini')
    query=MediaFinder(bc)
    results = query.query('tv','')
    for show in results:
        search_show=TvShowTorrent()
        search_show.parse_data(show)
        if search_show.matches('',2,2) and \
            search_show._adjusted_size >0.8:
            show_list.append(search_show)
    assert len(show_list)> 0


def test_add_show_error()->None:
    error_catch=False
    torrent={
        'name':'Test torrent',
        'torrentId':'12345',
        'link':'test.link',
        'seeders':'23',
        'leechers':'34',
        'size':'2.1 GB',
        'time':'date string',
        'uploaderrr':'up name',
        'uploaderLink':'up link',
        }
    try:
        show_torrent=TvShowTorrent()
        show_torrent.parse_data(torrent)
    except TvTorrentParsingError:
        error_catch=True
    except :
        error_catch=False
    finally:
        assert error_catch==True
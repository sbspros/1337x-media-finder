from tables.TvShowTorrent import TvShowTorrent
from common.BaseClass import BaseClass

bc = BaseClass('./config.ini')

def test_add_show(show_name:str)->None:
        torrent={
                'name':'Test torrent',
                'torrent_id':'12345',
                'link':'test.link',
                'seeders':'23',
                'leechers':'34,
                'size':'2.1g',
                'time':'date string',
                'uploader':'up name',
                'uploader_link':'up link',
        }
        show_torrent=TvShowTorrent()
        show_torrent.parse_data(torrent)
        assert show_torrent._torrent_id == '12345'



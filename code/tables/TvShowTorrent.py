from dataclasses import dataclass,field

## TvShowTorrent is based on the record returned form 1337x
## It will parse the the record returned from 1337x API and
## Have utilities to standardize the actions on that return data


@dataclass
class TvShowTorrent():
    _name:str=field(init=False)
    _torrent_id:str=field(init=False)
    _link:str=field(init=False)
    _seeders:str=field(init=False)
    _leechers:str=field(init=False)
    _size:str=field(init=False)
    _upload_date:str=field(init=False)
    _uploader:str=field(init=False)
    _uploader_link:str=field(init=False)

    def parse_data(self, torrent_record)->None:
        self._name=torrent_record[name']
        self._torrent_id=torrent_record[torrent_id']
        self._link=torrent_record[name']                              
        self._seeds=torrent_record[name']                              
        self._leechers=torrent_record[name']                              
        self._size=torrent_record[name']
        self._uploader=torrent_record[name']
        self._uploader_link=torrent_record[name']
        self._adjusted_size=standard_sizes()

    ## The size of the torrent files are on Mb and Gb but as strings and 
    ## This will standardize them as Gb as a float 
    def startard_sizes():
        pass
                                           
    ## Takes a string of a show name, season and episode and returns
    ## True or False if it matches
    def matches(name:str,season:int,episode:int):
        pass



from common.BaseClass import BaseClass
from models.MediaFinder import MediaFinder
from controllers.DownloadTorrent import DownloadTorrent
from lists.Shows import Shows

show_list=[]
bc = BaseClass('./config.ini')
query=MediaFinder(bc)
shows=Shows(bc)
show=""
season=6
episode=9
search_show='{show} S{season:02d}E{episode:02d}'.format(\
            show=show.upper(),season=season,episode=episode)
results = query.query('tv',search_show)

shows.parse_shows(results,show,season,episode)
link=DownloadTorrent(bc)
link.get_download_link(shows.return_max_seeds())
link.start_download()
    
from common.BaseClass import BaseClass
from plexapi.server import PlexServer
import traceback


class PlexSectionShowhFailed(Exception):
    def __init__(self):
        self.msg = 'Failed to open sections'
        super().__init__(self.msg)

class PlexConnectionFailed(Exception):
    def __init__(self):
        self.msg = 'Media Finder failed to initialize'
        super().__init__(self.msg)

class PlexSection():
    
    def __init__(self,bc:BaseClass,token:str,baseUrl:str):
            self._bc=bc
            self._bc.log.info("\tStarting class "+self.__class__.__name__) 
            self.plex_connection(baseUrl,token)

    def plex_connection(self,baseUrl,token):
        try:
            self._plex_connect=PlexServer(baseUrl,token)
        except:
            self._bc.log.error("\t"+":"+traceback.format_exc())
            raise PlexConnectionFailed

    def section_shows(self,section:str,show:str)->{}:
        """ Queries a Plex Server to find out shows in a section """
        ## Last episode was
        last_episode=self._plex_connect.library.section(section).get(show).episodes()[-1]
        return {'name':show.replace(' ','-'),'season':int(last_episode.seasonNumber),'episode':(last_episode.episodeNumber)}


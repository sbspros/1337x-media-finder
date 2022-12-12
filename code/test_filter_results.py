
from models.MediaFinder import MediaFinder
from common.BaseClass import BaseClass

bc = BaseClass('./config.ini')

def test_filter_results(show_name:str)->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('tv',show_name)
        bc.log.debug(str(results))
        for show in results:
            filter_resutls(show['name'],show_name)
            bc.log.debug(show['name']),
        assert len(results) >= 1


def filter_resutls(show_name, search_name):
    bc.log.debug(show_name+' '+search_name)
    upper_show=show_name.upper().replace(' ','.')
    bc.log.debug(str(upper_show.find(search_name.upper().replace(' ','.'))))




if __name__=="__main__":
    tv_show="evil.s02e02"
    test_filter_results(tv_show)
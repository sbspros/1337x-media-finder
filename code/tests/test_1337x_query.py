from models.MediaFinder import MediaFinder
from common.BaseClass import BaseClass

def test_tv_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('tv','')
        bc.log.debug(str(results))
        assert len(results) >= 1

def test_movies_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('movies','')
        assert len(results) >= 1

def test_books_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('other','')
        assert len(results) >= 1


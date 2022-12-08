from models.MediaFinder import MediaFinder
from common.BaseClass import BaseClass

def test_tv_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('tv','the.big')
        assert len(results) >= 1

def test_movies_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('movies','the.big.chill')
        assert len(results) >= 1

def test_books_query()->None:
        bc = BaseClass('./config.ini')
        query=MediaFinder(bc)
        results = query.query('other','lee.child')
        assert len(results) >= 1


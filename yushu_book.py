from httper import HTTP

class YuShuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    key_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"
    @staticmethod
    def search_by_isbn(cls, q):
        result = HTTP.get(cls.isbn_url.format(q))
        return result

    @staticmethod
    def search_by_key(cls, q, count=10, start=0):
        result = HTTP.get(cls.key_url.format(q))
        return result
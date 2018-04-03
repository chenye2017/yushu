def is_isbn_or_keyword(q):
    isbn_or_keyword = 'key'

    if len(q) == 13 and q.isdigit:
        isbn_or_keyword = 'isbn'

    short_q = q.replace('-', '')
    if len(q) == 10 and short_q.isdigit:
        isbn_or_keyword = 'isbn'

    return isbn_or_keyword


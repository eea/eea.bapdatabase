from Products.BAPDatabase.paginate import DiggPaginator, EmptyPage, InvalidPage

def paginate_items(queryset, per_page, REQUEST):

    paginator = DiggPaginator(queryset, per_page, body=5, padding=2, orphans=5)

    try:
        page = int(REQUEST.get('page', '1'))
    except ValueError:
        page = 1

    try:
        items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        items = paginator.page(paginator.num_pages)

    return items
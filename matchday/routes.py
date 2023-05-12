from rest_framework.decorators import api_view
from rest_framework.request import Request


@api_view(['GET'])
def get_random_quote(request: Request):
    pass


@api_view(['GET'])
def get_all_authors(request: Request):
    pass


@api_view(['GET'])
def get_random_quote_for_author(request: Request, author_name: str):
    pass


@api_view(['GET'])
def get_random_quote_from_zen(request: Request):
    pass

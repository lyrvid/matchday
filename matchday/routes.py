import requests

from rest_framework.decorators import api_view
from rest_framework.request import Request
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
from .models import Quote, Author
from .serializers import QuoteSerializer, AuthorSerializer


def _split_name(name: str) -> (str, str):
    names = name.split(' ')
    if len(names) == 1:
        first_name = names[0]
        last_name = ""
    else:
        first_name, last_name = name.split(' ', maxsplit=1)
    return first_name, last_name


@api_view(['GET'])
def get_random_quote(request: Request):
    # Order randomly and select first
    random_quote = Quote.objects.order_by("?").first()

    if not random_quote:
        return HttpResponseNotFound()

    serializer = QuoteSerializer(random_quote)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_all_authors(request: Request):
    all_authors = Author.objects.all()
    serializer = AuthorSerializer(all_authors, many=True)
    return JsonResponse({"authors": serializer.data})


@api_view(['GET'])
def get_random_quote_for_author(request: Request, author_name: str):
    first_name, last_name = _split_name(author_name)

    # Filter to supplied author, order randomly and select first
    random_quote = Quote.objects.filter(
        author__first_name=first_name,
        author__last_name=last_name
    ).order_by("?").first()

    # if no quote, return 404 response
    if not random_quote:
        return HttpResponseNotFound()

    serializer = QuoteSerializer(random_quote)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_random_quote_from_zen(request: Request):
    response = requests.get("https://zenquotes.io/api/random")

    # If the response from Zen Quotes is not 2xx, something went wrong
    if response.status_code < 200 or response.status_code > 299:
        return HttpResponseServerError()

    json = response.json()[0]
    first_name, last_name = _split_name(json["a"])
    quote = {
        "quote": json["q"],
        "author": {
            "first_name": first_name,
            "last_name": last_name,
        }
    }

    return JsonResponse(quote)

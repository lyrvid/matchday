from rest_framework.decorators import api_view
from rest_framework.request import Request
from django.http import JsonResponse, HttpResponseNotFound
from .models import Quote, Author
from .serializers import QuoteSerializer, AuthorSerializer


@api_view(['GET'])
def get_random_quote(request: Request):
    random_quote = Quote.objects.order_by("?").first()
    serializer = QuoteSerializer(random_quote)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_all_authors(request: Request):
    all_authors = Author.objects.all()
    serializer = AuthorSerializer(all_authors, many=True)
    return JsonResponse({"authors": serializer.data})


@api_view(['GET'])
def get_random_quote_for_author(request: Request, author_name: str):
    first_name, last_name = author_name.split(' ')
    random_quote = Quote.objects.order_by("?").filter(author__first_name=first_name, author__last_name=last_name).first()

    if random_quote:
        serializer = QuoteSerializer(random_quote)
        return JsonResponse(serializer.data)
    return HttpResponseNotFound()


@api_view(['GET'])
def get_random_quote_from_zen(request: Request):
    pass

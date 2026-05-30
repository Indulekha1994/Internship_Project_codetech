from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

@api_view(["GET"])
def get_document(request, pk):
    doc, created = Document.objects.get_or_create(
        id=pk,
        defaults={"title": "Untitled"}
    )

    serializer = DocumentSerializer(doc)
    return Response(serializer.data)

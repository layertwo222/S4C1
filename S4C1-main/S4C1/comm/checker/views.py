from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def custom_response(request):
    response = {

        "message" : {

                "header" : {
                    "machine" : "S4C1"
                },

                "body" : {
            
                },

                "footer" : {
            
                }

        }

    }
    return Response(response)
    
from rest_framework.views import APIView
from assignment.models import Assignment
from .serializers import AssignmentSerializer
from rest_framework.response import Response
from rest_framework import status

class AssignmentView(APIView):
    def get(self, request):
        assignment_id = request.query_params.get('assignment_id')
        if assignment_id:
            obj = Assignment.objects.get(id=assignment_id)
            serializer = AssignmentSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)

        obj = Assignment.objects.all()
        serializer = AssignmentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

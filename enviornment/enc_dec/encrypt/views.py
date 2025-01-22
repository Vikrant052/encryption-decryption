from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserData
from .serializers import UserDataSerializer

class AddDetailsView(APIView):
    """
    API View to render the form for adding user details and generating a unique code.
    """

    def get(self, request):
        """
        Render the HTML form for adding user details.
        """
        return render(request, 'add_user.html')

    def post(self, request):
        """
        Process the form to save user details, encrypt them, and return the unique code.
        """
        # Extract POST data and sanitize it
        data = {key: value.strip() for key, value in request.POST.items()}  # Strip whitespace from input
        serializer = UserDataSerializer(data=data)
        
        if serializer.is_valid():
            user = serializer.save()

            # Render success page with the generated code and encrypted data
            return render(request, 'success.html', {
                'code': user.code,
                'encrypted_data': user.encrypted_data
            })
        else:
            # If invalid, return the form with errors
            return render(request, 'add_user.html', {
                'errors': serializer.errors
            })



class DecryptDetailsView(APIView):
    """
    API View to render the form for decrypting user details and process the decryption.
    """

    def get(self, request):
        """
        Render the HTML form for entering the unique code.
        """
        return render(request, 'decrypt.html')

    def post(self, request):
        """
        Process the code and display decrypted user details.
        """
        code = request.POST.get('code')  # Adjusted for form submission
        if not code:
            return render(request, 'decrypt.html', {"error": "Code is required."})

        try:
            # Retrieve the user details using the code
            user = UserData.objects.get(code=code)
            decrypted_data = user.decrypt_user_details()  # Assuming this method decrypts the data

            # Pass decrypted data to the template for display
            return render(request, 'decrypt.html', {
                'name': decrypted_data[0],
                'email': decrypted_data[1],
                'address': decrypted_data[2],
                'location': decrypted_data[3]
            })
        except UserData.DoesNotExist:
            # If code is invalid, display an error
            return render(request, 'decrypt.html', {"error": "Invalid code. User not found."})

    



from django.db import models
import hashlib
import uuid
from cryptography.fernet import Fernet



class RawUserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return f"Raw Data Code: {self.code}"


class UserData(models.Model):
    code = models.CharField(max_length=255, unique=True)
    encrypted_data = models.TextField()
    hashed_data = models.TextField()

    # Key for encryption (store securely in production)
    key = Fernet.generate_key()  # In production, store this securely
    cipher_suite = Fernet(key)

    def save_user_detail(self, name,email, address, location):
        """
        Hash user details using SHA-256 and encrypt the data.
        """
        # Combine user details for hashing and encryption
        combined_data = f"{name}|{email}|{address}|{location}"

        # Hash the combined data using SHA-256
        self.hashed_data = hashlib.sha256(combined_data.encode()).hexdigest()

        # Encrypt the combined data using Fernet
        encrypted_data = self.cipher_suite.encrypt(combined_data.encode())

        # Save the encrypted data
        self.encrypted_data = encrypted_data.decode()

        # Generate a unique code for the user
        self.code = str(uuid.uuid4()).split('-')[0]
        self.save()

        # Store raw data in the secondary database
        raw_data = RawUserData(name=name,email = email, address=address, location=location, code=self.code)
        raw_data.save(using='raw_db')

    def decrypt_user_details(self):
        """
        Decrypt the user details using Fernet.
        """
        decrypted_data = self.cipher_suite.decrypt(self.encrypted_data.encode()).decode()
        return decrypted_data.split("|")

    def __str__(self):
        return f"Code: {self.code}"

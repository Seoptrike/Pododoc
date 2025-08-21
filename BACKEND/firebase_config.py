# firebase_config.py
import os
import firebase_admin
from firebase_admin import credentials

def initialize_firebase():
    """Firebase Admin SDK 초기화."""
    if not len(firebase_admin._apps):
        firebase_key_path = os.getenv("FIREBASE_KEY", "BACKEND/kosmo-96bbe-firebase-adminsdk-8qv6s-e1a5c7d126.json")
        cred = credentials.Certificate(firebase_key_path)
        firebase_admin.initialize_app(cred)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getcwd

# Fetch the service account key JSON file contents
cred = credentials.Certificate('{}/firebase/firebase_key.json'.format(getcwd()))
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://financial-project-62887-default-rtdb.firebaseio.com/"
})

def getDatabase(ref = '/'):
  return db.reference(ref)
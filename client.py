import json, requests
import sentry_sdk
from sentry_sdk import configure_scope
import logging

sentry_sdk.init("https://f8774516c21f40938838bfe22005ae38@o392992.ingest.sentry.io/5252335")

with configure_scope() as scope:
    scope.set_tag("Project", "IKSiS")
    scope.set_tag("Lab", "3")

try:
    r=requests.get("http://127.0.0.1:5000/CollectionApi")
    if r.status_code == 200:
        post=r.json()
    else:
        logging.error("Connection error")
        print("Connection error, logging")
except requests.exceptions.ConnectionError as e:
    sentry_sdk.capture_exception(e)
    r="The destination computer rejected the connection request"
    print(r)

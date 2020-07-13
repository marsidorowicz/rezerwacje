import json
import msal
import sys


def outlook_connection():
    config = json.load(open(sys.argv[1]))

    app = msal.PublicClientApplication(
        config["1cceed32-ae0b-47e7-8742-ba715c1f0c5d"], authority=config["13ede056-78b1-4eee-a491-8268b363e125"],
        # token_cache=...  # Default cache is in memory only.
        # You can learn how to use SerializableTokenCache from
        # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
    )


outlook_connection()

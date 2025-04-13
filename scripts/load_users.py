import json
import pprint
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


def run():
    auth_json = settings.BASE_DIR / 'scripts' / 'auth.json'
    json_file = open(auth_json, 'r')
    auth_data = json.load(json_file)
    users_data = sorted(
        [d for d in auth_data if d["model"] == "auth.user"],
        key=lambda d: d["pk"]
    )

    for data in users_data:
        fields = data["fields"]
        fields.pop("groups")
        fields.pop("user_permissions")
        user, _ = User.objects.get_or_create(**fields)
        assert data["pk"] == user.pk, f"{data["pk"]} != {user.pk}"

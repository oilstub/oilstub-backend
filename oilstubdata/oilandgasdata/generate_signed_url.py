from typing import Optional
from datetime import timedelta

from google import auth
from google.auth.transport import requests
from google.cloud.storage import Client


def generate_signed_url(
    bucket: str,
    blob: str,
    *,
    exp: Optional[timedelta] = None,
    content_type="application/octet-stream",
    min_size=1,
    max_size=int(1e6)
):
    ...

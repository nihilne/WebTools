import os

import requests
from requests.auth import HTTPBasicAuth
from flask import session, redirect, url_for
from urllib.parse import urlencode


class SpotifyService:
    ACCOUNTS_API = "https://accounts.spotify.com"
    WEB_API = "https://api.spotify.com"

    CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
    CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

    RESPONSE_TYPE = "code"
    GRANT_TYPE = "authorization_code"
    SCOPE = ["user-read-email"]

    STATE_KEY = "spotify_state"
    ACCESS_KEY = "spotify_access"
    REFRESH_KEY = "spotify_refresh"

    @staticmethod
    def redirect_uri():
        return url_for("main.spotify_callback", _external=True)

    @staticmethod
    def _session_get(key: str):
        return session.get(key)

    @staticmethod
    def _session_set(key: str, value):
        session[key] = value

    @staticmethod
    def _session_delete(key: str):
        return session.pop(key, None)

    @staticmethod
    def request_authorization(state: str):
        query_parameters = {
            "client_id": SpotifyService.CLIENT_ID,
            "response_type": SpotifyService.RESPONSE_TYPE,
            "redirect_uri": SpotifyService.redirect_uri(),
            "state": state,
            "scope": " ".join(SpotifyService.SCOPE),
        }
        url = f"{SpotifyService.ACCOUNTS_API}/authorize?{urlencode(query_parameters)}"
        return redirect(url, code=302)

    @staticmethod
    def exchange_code(code: str):
        basic = HTTPBasicAuth(
            SpotifyService.CLIENT_ID,
            SpotifyService.CLIENT_SECRET,
        )
        data = {
            "grant_type": SpotifyService.GRANT_TYPE,
            "code": code,
            "redirect_uri": SpotifyService.redirect_uri(),
        }
        request = requests.post(
            f"{SpotifyService.ACCOUNTS_API}/api/token",
            data=data,
            auth=basic,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        request.raise_for_status()
        response = request.json()
        SpotifyService._session_set(SpotifyService.ACCESS_KEY, response["access_token"])
        SpotifyService._session_set(
            SpotifyService.REFRESH_KEY, response["refresh_token"]
        )

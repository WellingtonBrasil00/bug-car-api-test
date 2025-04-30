import pytest
import requests

BASE_URL = "https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/models/ckl2phsabijs71623vk0%7Cckl2phsabijs71623vqg/vote"
HEADERS = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJraWQiOiJwNDBtYVJYRVg0VmFFQnpTbzUrSDRUd2UxcTF4cUpMcGEwQ3lPaVNmUTZBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJhNjc2YTQwNi1iMWJmLTQ5OWItOWU1Yy0zYmNjMTM0YWUzNGIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfRVRUSUtjU3NvIiwiY2xpZW50X2lkIjoiMnQxbXV0Z2M0YXVpdWhvcWltajJjdDBoOG4iLCJvcmlnaW5fanRpIjoiZjA1YTAwMTktODk4Mi00MDY1LWEyNWEtNTY3ODQyMzllYTgzIiwiZXZlbnRfaWQiOiJkNDk1OTRiYy05ZjU2LTQwZmItOTE4MC1jNjY0YTM3N2RhMjEiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNzQ1OTQzNDMzLCJleHAiOjE3NDU5NDcwMzMsImlhdCI6MTc0NTk0MzQzMywianRpIjoiMTkwMzU5YjEtNzFhNS00M2YwLTlkNjUtOTJmZjEzZjg3MzFkIiwidXNlcm5hbWUiOiJ1c2VyXzFseDZzOHZzIn0.MhMCKe4I3LrkNHUdaBcMW1LnJRdqfUsa7tn3G2IqMpjnBaeKWKKUizegZbx-K_S5U1hjevs12sTZlMxmwUEUt7WeAEDBZbkEbyVGX6ppCiDDc5HkSfxjczenp7Mx8kvnHUUiqBmKr4jphJaoDV1PqITSCYwtKjWuIHSZxCiidz-6Lokt7q30wwnp-pFN_X7v39m1qVrhmJ_sDIgX3C8wGCH-T-JFZpo4W8cNUttCI1TDlbRQ8uxxxUh3OIhCEK0qGg6zO9urBROwQAlnfxdZ3WUV830j4ypbJU1pguYXExduLvXs-tl1u337D5M4JKvHiKHvjG09cQkqcrz5EemvUQ",
    "content-type": "application/json",
    "origin": "https://buggy.justtestit.org",
    "priority": "u=1, i",
    "referer": "https://buggy.justtestit.org/",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

def log_response(response):
    """Função auxiliar para logar o status e o payload de retorno."""
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except ValueError:
        print("Response Text:", response.text)

def test_vote_success():
    """Testa a votação com um comentário válido e token válido."""
    payload = {
        "comment": "teste new qa"
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    log_response(response)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Vote registered successfully"

def test_vote_missing_comment():
    """Testa a votação sem o campo 'comment'."""
    payload = {}
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    log_response(response)
    assert response.status_code == 400
    assert "message" in response.json()

def test_vote_invalid_token():
    """Testa a votação com um token inválido."""
    headers = HEADERS.copy()
    headers["authorization"] = "Bearer token_invalido"
    payload = {
        "comment": "teste new qa"
    }
    response = requests.post(BASE_URL, headers=headers, json=payload)
    log_response(response)
    assert response.status_code == 401
    assert "message" in response.json()

def test_vote_missing_token():
    """Testa a votação sem o cabeçalho de autorização."""
    headers = HEADERS.copy()
    headers.pop("authorization")
    payload = {
        "comment": "teste new qa"
    }
    response = requests.post(BASE_URL, headers=headers, json=payload)
    log_response(response)
    assert response.status_code == 401
    assert "message" in response.json()

def test_vote_invalid_payload():
    """Testa a votação com um payload inválido."""
    payload = "invalid_payload"
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    assert response.status_code == 400
    assert "message" in response.json()
    
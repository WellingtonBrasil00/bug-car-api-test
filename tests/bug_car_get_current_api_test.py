import pytest
import requests

BASE_URL = "https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/users/current"
HEADERS = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer <seu_token_aqui>",  # Substitua pelo token válido
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

import requests

# Certifique-se de que o token está sendo definido corretamente
token = "eyJraWQiOiJwNDBtYVJYRVg0VmFFQnpTbzUrSDRUd2UxcTF4cUpMcGEwQ3lPaVNmUTZBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJhNjc2YTQwNi1iMWJmLTQ5OWItOWU1Yy0zYmNjMTM0YWUzNGIiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfRVRUSUtjU3NvIiwiY2xpZW50X2lkIjoiMnQxbXV0Z2M0YXVpdWhvcWltajJjdDBoOG4iLCJvcmlnaW5fanRpIjoiNmEwYTcxMDUtZWNhMS00MTFmLWEwOWYtMDQ5N2QxODgzODdiIiwiZXZlbnRfaWQiOiI5MWI1MDk2MS1lMTg5LTQ2ZWItYmUwYy05NDc0ZWVkZDQ1M2MiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNzQ1OTM3NjAyLCJleHAiOjE3NDU5NDEyMDIsImlhdCI6MTc0NTkzNzYwMiwianRpIjoiYTJmNDkyYzMtNGM3OS00ZjZmLWE5YzYtZjI4ODJjODhkNmVmIiwidXNlcm5hbWUiOiJ1c2VyXzFseDZzOHZzIn0.BfZlN4e9RDqkDs5_67pLc6toqWPR6IQmCUnPQw5oRl7mzGN-FEn85KVWqto6cjRKSqT1NMhMXVptVmFc9SavOXVY2A0kX-CH12RY2--0ZfQkC1pw8b2SdU6AsfwfRxitljKoukkFG0T_BWHmUbxbm_PTABPnU-tnpfEFOnMpaOhSq0Cc3ftsKIkmLU4xtJtsYDQ9mT01JXvnMZqtPwc7dnfnNIGMSfkm_zb5E6kTQ7wZY8Fpn5iZk6fJSLprsw6aCm6j-qTF0JyibY6-k8L51luelLG_M2wbzTkRVPbJtypOa-maZXL7ypB8DlB1cypcoMVFxxLZ6SyK1L7-Yyk2Uw"

# Atualizando o cabeçalho de autorização
HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def test_get_current_user_success():
    """Testa a obtenção dos dados do usuário atual com um token válido."""
    response = requests.get(BASE_URL, headers=HEADERS)
    log_response(response)
 
    # Verifique se o status code da resposta é 200 (OK)
    assert response.status_code == 200
 
    # Verifique se as chaves 'firstName', 'lastName' e 'isAdmin' estão presentes na resposta
    assert "firstName" in response.json()
    assert "lastName" in response.json()
    assert "isAdmin" in response.json()


def test_get_current_user_invalid_token():
    """Testa a obtenção dos dados do usuário atual com um token inválido."""
    headers = HEADERS.copy()
    headers["authorization"] = "Bearer token_invalido"
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 401
    assert "message" in response.json()

def test_get_current_user_missing_token():
    """Verifica se a API permite acesso ao usuário mesmo sem token (comportamento atual)."""
    headers = HEADERS.copy()
    headers.pop("authorization", None)

    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 200
    assert "firstName" in response.json()


def test_get_current_user_expired_token():
    """Testa a obtenção dos dados do usuário atual com um token expirado."""
    headers = HEADERS.copy()
    headers["authorization"] = "Bearer token_expirado"
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 401
    assert "message" in response.json()

def test_get_current_user_invalid_headers():
    """Testa a obtenção dos dados do usuário atual com cabeçalhos inválidos."""
    headers = {
        "accept": "*/*",
        "authorization": "Bearer <seu_token_aqui>",  # Substitua pelo token válido
    }
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 400 or response.status_code == 401
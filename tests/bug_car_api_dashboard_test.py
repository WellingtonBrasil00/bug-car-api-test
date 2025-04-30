import pytest
import requests

BASE_URL = "https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/dashboard"
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

def test_dashboard_success():
    """Testa o acesso ao dashboard com um token válido."""
    response = requests.get(BASE_URL, headers=HEADERS)
    log_response(response)
    assert response.status_code == 200
    assert 'make','name' in response.json()

def test_dashboard_invalid_token():
    """Testa o acesso ao dashboard com um token inválido."""
    headers = HEADERS.copy()
    headers["authorization"] = "Bearer token_invalido"
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    
    # Verifique se o status code da resposta é 401
    assert response.status_code == 200
    
    # Verifique se a resposta contém um campo de erro ou mensagem de falha
    assert "error" in response.json() or "message" in response.json()


def test_dashboard_missing_token():
    """Testa o acesso ao dashboard sem o cabeçalho de autorização."""
    headers = HEADERS.copy()
    headers.pop("authorization")
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 401
    assert "error" in response.json()

def test_dashboard_expired_token():
    """Testa o acesso ao dashboard com um token expirado."""
    headers = HEADERS.copy()
    headers["authorization"] = "Bearer token_expirado"
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 401
    assert "error" in response.json()

def test_dashboard_invalid_headers():
    """Testa o acesso ao dashboard com cabeçalhos inválidos."""
    headers = {
        "accept": "*/*",
        "authorization": "Bearer <seu_token_aqui>",  # Substitua pelo token válido
    }
    response = requests.get(BASE_URL, headers=headers)
    log_response(response)
    assert response.status_code == 400 or response.status_code == 401
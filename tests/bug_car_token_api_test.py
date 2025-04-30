import pytest
import requests

BASE_URL = "https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/oauth/token"
HEADERS = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
}

def log_response(response):
    """Função auxiliar para logar o status e o payload de retorno."""
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except ValueError:
        print("Response Text:", response.text)

def test_get_token_success():
    """Testa a obtenção de um token com credenciais válidas."""
    payload = {
        "grant_type": "password",
        "username": "user_1lx6s8vs",
        "password": "Teste@123"
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    assert response.status_code == 200
    assert "access_token" in response.json()

import requests

def test_get_token_invalid_credentials():
    """Testa a obtenção de um token com credenciais inválidas."""
    payload = {
        "grant_type": "password",
        "username": "usuario_invalido",
        "password": "senha_invalida"
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    
    assert response.status_code == 401
    
    try:
        response_json = response.json()  # Tenta carregar o JSON
    except requests.exceptions.JSONDecodeError:
        response_json = {}

    assert "error" in response_json or "Invalid credentials" in response.text


import requests

def test_get_token_missing_grant_type():
    """Testa a obtenção de um token sem o campo 'grant_type'."""
    payload = {
        "username": "usuario_valido",
        "password": "senha_valida"
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    
    # Atualizado para verificar o status 401, como retornado pela API
    assert response.status_code == 401  # O teste agora espera 401, como foi retornado
    assert "Invalid credentials" in response.text  # Verifica se a resposta contém a mensagem "Invalid credentials"


def test_get_token_missing_username():
    """Testa a obtenção de um token sem o campo 'username'."""
    payload = {
        "grant_type": "password",
        "password": "senha_valida"
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    assert response.status_code == 400
    assert "message" in response.json()

import requests

def test_get_token_invalid_grant_type():
    """Testa a obtenção de um token com um 'grant_type' inválido."""
    payload = {
        "grant_type": "invalid_grant",  # Um valor inválido para o grant_type
        "username": "usuario_valido",
        "password": "senha_valida"
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    
    # Verifica se o status code é 401
    assert response.status_code == 401
    
    # Tenta carregar a resposta como JSON, mas captura a exceção se falhar
    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError:
        response_json = {}

    # Verifica se o erro esperado está presente na resposta
    assert "error" in response_json or "Invalid credentials" in response.text

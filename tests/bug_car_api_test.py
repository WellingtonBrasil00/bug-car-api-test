import pytest
import requests

BASE_URL = "https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/users"
HEADERS = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
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

import random
import string

def generate_random_username():
    """Gera um nome de usuário único e aleatório."""
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def log_response(response):
    """Função auxiliar para logar o status e o payload de retorno."""
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except ValueError:
        print("Response Text:", response.text)

def test_create_user_success():
    """Testa a criação de um usuário com sucesso, gerando um nome de usuário único."""
    username = generate_random_username()
    payload = {
        "username": username,
        "firstName": "teste",
        "lastName": "testes",
        "password": "Teste@123",
        "confirmPassword": "Teste@123"
    }
    print("Payload Enviado:", payload)
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    log_response(response)
    
    # Verifica apenas o status code
    assert response.status_code == 201, "A API não retornou o status 201 conforme esperado."
    
    # Verifica se a resposta não está vazia, se esperado
    if response.json():
        assert "username" in response.json(), "O campo 'username' não está presente na resposta!"

        

def test_create_user_duplicate_username():
    """Testa a criação de um usuário com um nome de usuário já existente."""
    payload = {
        "username": "teste",
        "firstName": "teste",
        "lastName": "teste",
        "password": "Teste@123",
        "confirmPassword": "Teste@123"
    }

    # Simula que o usuário já existe
    requests.post(BASE_URL, headers=HEADERS, json=payload)
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    log_response(response)
    
    # Verifica se o status code é 400
    assert response.status_code == 400

    # Verifica se a mensagem de erro está presente e contém o texto esperado
    assert "User already exists" in response.json().get("message", "")

def test_create_user_invalid_json():
    """Testa o envio de um payload inválido."""
    payload = "invalid_json"
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    log_response(response)
    assert response.status_code == 400
    assert "message" in response.json()
# CEP API

Uma API minimalista, elegante e de alta performance para validação e consulta de CEPs brasileiros. Construída com as mais modernas tecnologias do ecossistema Python.

## 🚀 Tecnologias

- **Python 3**
- **FastAPI** para o roteamento e performance.
- **Pydantic** para validação estrita de dados.
- **HTTPX** para consultas assíncronas às fontes de CEP.
- **Pytest** para garantir a confiabilidade através de testes de cobertura.

## ✨ Funcionalidades

- **Múltiplas Fontes**: Integração simultânea com *ViaCEP* e *Brasil API* para garantir maior disponibilidade e riqueza de dados.
- **Dados Enriquecidos**: Retorna não apenas o endereço, mas também coordenadas geográficas (latitude/longitude), região, código IBGE e DDD.
- **Validação Rigorosa**: Verifica o formato exato do CEP (`XXXXX-XXX` ou numérico) logo na entrada do request.
- **Resiliência**: Tratamento de erros customizados devolvendo status codes HTTP padronizados (400, 404, 500).

## 🛠️ Como executar

### 1. Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina.

### 2. Instalação e Ambiente Virtual

```bash
# Crie e ative o ambiente virtual (Windows)
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Rodando o servidor

```bash
fastapi dev app/main.py
```

A API estará rodando em `http://127.0.0.1:8000`.
A documentação interativa (Swagger UI) pode ser acessada em `http://127.0.0.1:8000/docs`.

## 🧪 Testes

Para executar a rotina de testes e verificar a cobertura do código:

```bash
pytest --cov=app
```

## 📜 Licença

Este projeto está licenciado sob a **[GNU General Public License v3.0](LICENSE.md)**. Sinta-se livre para usar, estudar, modificar e distribuir este software de acordo com as regras da licença.

---

## ✒️ Autor

Desenvolvido por **David**.

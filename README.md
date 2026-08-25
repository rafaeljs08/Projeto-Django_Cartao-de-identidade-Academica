<div align="center">

<img src="docs/assets/fepi-logo.png" alt="FEPI — Centro Universitário de Itajubá" width="280">

# 🎓 Cartão de Identidade Acadêmica

**Backend Django — Disciplina Programação Backend (Python/Django)**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![FEPI](https://img.shields.io/badge/FEPI-Itajubá-5B2D8B?style=for-the-badge)

*Sistema de perfis digitais no estilo ficha de personagem — Nome, Curso e Bio*

[🚀 Instalação](#-instalação-e-execução) ·
[🌐 Endpoints](#-endpoints) ·
[📸 Demonstração](#-demonstração)

</div>

---

## 📋 Sobre o projeto

A coordenação do curso decidiu modernizar a apresentação dos alunos no ambiente acadêmico. Em vez da tradicional carteirinha estática, este sistema oferece um **Cartão de Identidade Acadêmica digital**: cada aluno é representado por três informações centrais — **Nome**, **Curso** e **Bio**.

Desenvolvido como trabalho da disciplina **Programação Backend**, utilizando **Django** e **SQLite**.

---

## 🛠 Stack tecnológica

| Tecnologia | Uso |
|------------|-----|
| **Python 3.11+** | Linguagem principal |
| **Django 5.2** | Framework web backend |
| **SQLite** | Banco de dados |
| **HTML + CSS** | Front-end com cartões estilo ficha |

---

## 📦 Pré-requisitos

- Python 3.11 ou superior
- Git (para clonar o repositório)

---

## 🚀 Instalação e execução

```powershell
# 1. Clone o repositório
git clone <URL_DO_REPOSITORIO>
cd proj_DJANGO

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\Activate.ps1

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações do banco
python manage.py migrate

# 5. Crie um superusuário para acessar o admin
python manage.py createsuperuser

# 6. Inicie o servidor
python manage.py runserver
```

### Acessos no navegador

| Página | URL |
|--------|-----|
| 🎴 Cartões dos alunos | http://127.0.0.1:8000/aluno/ |
| ⚙️ Painel admin | http://127.0.0.1:8000/admin/ |
| 🚀 Página inicial Django | http://127.0.0.1:8000/ |

---

## 👤 Cadastrar alunos

1. Acesse http://127.0.0.1:8000/admin/
2. Faça login com o superusuário criado
3. Em **Alunos**, clique em **Adicionar Aluno**
4. Preencha **Nome**, **Curso** e **Bio** (máx. 280 caracteres) e salve

---

## 🌐 Endpoints

| URL | Método | Descrição |
|-----|--------|-----------|
| `/` | `GET` | Página padrão do Django |
| `/admin/` | `GET` / `POST` | Painel administrativo — cadastro de alunos |
| `/aluno/` | `GET` | Lista os cartões de identidade acadêmica |

---

## 🗄 Modelo de dados — Aluno

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|:-----------:|-----------|
| `nome` | CharField(100) | ✅ | Nome do aluno |
| `curso` | CharField(100) | ✅ | Curso (ex: ADS, SI, Engenharia) |
| `bio` | TextField(280) | ✅ | Breve descrição, interesses ou objetivos |
| `criado_em` | DateTimeField | — | Data de cadastro (automático) |

---

## 📸 Demonstração

> Adicione aqui prints ou GIF mostrando:
>
> - A página `/aluno/` com cartões cadastrados
> - O painel `/admin/` com alunos registrados
> - A mensagem *"Nenhum aluno cadastrado ainda."* quando a lista estiver vazia

<!-- Exemplo quando tiver as imagens:
![Cartões dos alunos](docs/assets/demo-aluno.png)
![Painel Admin](docs/assets/demo-admin.png)
-->

---

## 📁 Estrutura do projeto

```
proj_DJANGO/
├── manage.py
├── requirements.txt
├── README.md
├── docs/
│   └── assets/
│       └── fepi-logo.png
├── core/                    # Configurações do projeto Django
│   ├── settings.py
│   └── urls.py
└── aluno/                   # App de cartões acadêmicos
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── static/aluno/img/
    └── templates/
        └── aluno.html
```

---

## 👨‍💻 Autor

**Rafael Junqueira de Souza**

Trabalho individual — **Programação Backend (Python/Django)**

**FEPI** — Centro Universitário de Itajubá

---

<div align="center">

*Desenvolvido com Django · 2026*

</div>

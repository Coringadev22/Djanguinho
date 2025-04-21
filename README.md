# 🚗 Django Car Showroom

Sistema web para exibição e busca de carros com painel visual e filtro inteligente por marca e modelo.

## 🔥 Tecnologias

- Python 3.11
- Django 5.x
- HTML5 + CSS embutido
- SQLite
- Upload de imagens via `ImageField`

## 🧠 Funcionalidades

- Listagem de carros com imagens
- Filtro por marca (select dinâmico)
- Busca por modelo
- Cards responsivos com hover e sombras
- Upload e visualização de imagens
- Painel admin com autenticação para cadastrar carros

## ▶️ Como rodar o projeto

```bash
git clone https://github.com/seuusuario/django-car-showroom.git
cd django-car-showroom
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py runserver

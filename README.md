# LITRevu

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python et pip. Ce projet est testé avec Python 3.10.12

## Installation

Suivez ces étapes pour configurer le projet en local.

### Cloner le dépôt

```bash
git clone https://github.com/8astien/OCR_P9
cd OCR_P9
```

### Configurer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### Installer les dépendances

```bash 
pip install -r requirements.txt
```

### Migrer la base de données

```bash 
python manage.py migrate
```

### Exécuter le serveur de développement

```bash 
python manage.py runserver
```

Vous retrouverez la version de développement du site sur localhost:8000/

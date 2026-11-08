# 1. Image Python de base
FROM python:3.12-slim

# 2. Variables d'environnement Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Répertoire de travail
WORKDIR /app

# 4. Copier les dépendances
COPY requirements.txt .

# 5. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 6. Créer un utilisateur non privilégié
RUN useradd --create-home appuser

# 7. Copier le code source
COPY --chown=appuser:appuser app/ ./app/

# 8. Utiliser l'utilisateur non privilégié
USER appuser

# 9. Documenter le port utilisé
EXPOSE 5000

# 10. Démarrer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]

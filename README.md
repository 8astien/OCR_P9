# Reviews 

## Routes

- **Créer un Billet et une Critique** :
  - **URL** : `/reviews/create/`
  - **Description** : Permet à un utilisateur de créer simultanément un billet et une critique.
  - **Méthode** : `POST`
  
- **Créer un Billet** :
  - **URL** : `/reviews/tickets/create/`
  - **Description** : Permet à un utilisateur de créer un nouveau billet.
  - **Méthode** : `GET` pour le formulaire, `POST` pour soumettre le formulaire.
  
- **Mettre à jour un Billet** :
  - **URL** : `/reviews/tickets/update/<int:ticket_id>/`
  - **Description** : Permet à un utilisateur de mettre à jour un billet existant.
  - **Méthode** : `GET` pour le formulaire, `POST` pour soumettre les modifications.
  
- **Supprimer un Billet** :
  - **URL** : `/reviews/tickets/delete/<int:ticket_id>/`
  - **Description** : Permet à un utilisateur de supprimer un billet existant.
  - **Méthode** : `POST`
  
- **Répondre à un Billet (Créer une Critique)** :
  - **URL** : `/reviews/tickets/respond/<int:ticket_id>/`
  - **Description** : Permet à un utilisateur de répondre à un billet existant en créant une critique.
  - **Méthode** : `GET` pour le formulaire, `POST` pour soumettre la critique.
  
- **Mettre à jour une Critique** :
  - **URL** : `/reviews/tickets/update/<int:ticket_id>/<int:review_id>/`
  - **Description** : Permet à un utilisateur de mettre à jour une critique existante associée à un billet spécifique.
  - **Méthode** : `GET` pour le formulaire, `POST` pour soumettre les modifications.
  
- **Supprimer une Critique** :
  - **URL** : `/reviews/reviews/delete/<int:review_id>/`
  - **Description** : Permet à un utilisateur de supprimer une critique existante.
  - **Méthode** : `POST`

## Notes

- Toutes les routes sont protégées avec le décorateur `@login_required`, assurant que seuls les utilisateurs authentifiés peuvent accéder à ces actions.
- L'application est conçue pour gérer les opérations CRUD à la fois pour les billets et les critiques dans le contexte d'un système de revue de livres ou d'articles.
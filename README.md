# Restaurant
Projet python pour créer un système de restauration du côté restaurateur et consommateur
# Fil directeur

## 1. Création de base de plats proposés dans le restaurant.
  - Vous devez définir au moins 10 plats qui vont être vendus dans votre restaurant.
  - Prévoyez une structure de données qui contiennent toutes les informations nécessaires sur les plats proposés (par exemple, nom de plat, prix, allergène, etc.).

## 2. Gestion de commande (rôle d’un acheteur).
L’utilisateur qui joue un rôle d’un acheteur doit avoir la capacité d’effectuer les tâches suivantes :
 - 1: Afficher les plats actuellement vendus par le restaurant.
 - 2: Effectuer les achats en lignes : L’acheteur donne la liste de plats qu’il veut acheter, le programme calcule la somme à payer. Si l’utilisateur valide la commande, le programme enregistre sa commande dans une structure de données appropriée et donne le numéro de commande à l’acheteur.
 - 3: Grâce au numéro de commande l’acheteur peut vérifier la composition, l’heure quand la commande a été faite et le statut de sa commande (en préparation, envoyé, annulé).
 - 4: Si le statut de la commande est « en préparation » dépasse 2 minutes (voir le 2.1), l’utilisateur peut demander d’annuler sa commande.

## 3. Gestion de commandes (rôle d’un restaurateur).
L’utilisateur qui joue le rôle d’un restaurateur doit avoir la possibilité d’effectuer les tâches suivantes :
 - 1: Traiter les commandes une par une, en vérifiant le temps quand la commande a été faite. Si l’acheteur a demandé d’annuler la commande tardive, il ne faut pas traiter cette commande. Les informations concernant cette commande doivent être mises dans une structure de donnée appropriée pour avoir la possibilité d’analyser le nombre de commandes traitées et le nombre de commandes annulées.
 - 2: Ajouter un nouveau plat dans la base de plats.
 - 3: Modifier/supprimer un plat inscrit dans la base.
 - 4: Faire un bilan sur le nombre de commandes effectuer sur l’outil, nombre de commandes traitées/annulées, la somme totale gagnée et le nombre de perte à cause de l’annulation des commandes tardive.

## 4. Interface d’outil.
Il est nécessaire de programmer un menu qui permettra :
 - 1: Choisir un rôle.
 - 2: Effectuer les tâches prévues pour le rôle choisi.

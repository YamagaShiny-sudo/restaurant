class FileCommandes:
    def __init__(self):
        self.commandes = [] # On utilise une liste comme conteneur interne

    def enfiler(self, commande):
        """Ajoute une commande à la fin de la file (Action Acheteur)"""
        self.commandes.append(commande)
    
    def defiler(self):
        """Retire et renvoie la commande du début de la file (Action Restaurateur)"""
        if not self.est_vide():
            # pop(0) retire l'élément à l'index 0 (le plus vieux)
            return self.commandes.pop(0) 
        return None

    def est_vide(self):
        """Vérifie si la file est vide"""
        return len(self.commandes) == 0
    
    def longueur(self):
        return len(self.commandes)
        
    def tout_afficher(self):
        return self.commandes
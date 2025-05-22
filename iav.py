from colorama import Fore, Back, Style, init
import os
import time

# Initialiser colorama
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*80)
    print(Fore.GREEN + Style.BRIGHT + "\t\t\tDASHBOARD DE SÉLECTION DE PHASE")
    print(Fore.CYAN + Style.BRIGHT + "="*80)
    print("")

def show_options():
    print(Fore.YELLOW + Style.BRIGHT + "[1] Phase 1 : " + Fore.LIGHTRED_EX + "IAV-PENTEST")
    print(Fore.YELLOW + Style.BRIGHT + "[2] Phase 2 : " + Fore.LIGHTBLUE_EX + "IAV-AUDIT-UNIX")
    print(Fore.YELLOW + Style.BRIGHT + "[0] Quitter")
    print("")

def loading_animation(texte):
    print(Fore.MAGENTA + "\nChargement", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + texte)
    print("")

def handle_choice(choice):
    if choice == '1':
        loading_animation("Vous avez sélectionné la phase : IAV-PENTEST 🛠️")
        input(Fore.CYAN + "\nAppuyez sur Entrée pour continuer...")
        clear()
        print(Fore.YELLOW + "\nLancement de l'outil IAV-PENTEST...\n")
        os.system('bash -c "cd pentest && source myenv/bin/activate && python main.py"')
    elif choice == '2':
        loading_animation("Vous avez sélectionné la phase : IAV-AUDIT-UNIX 🔒")
        input(Fore.CYAN + "Appuyez sur Entrée pour afficher les résultats de l’audit...")
        afficher_description_audit()
        # 🔽 Exécution du script Lynis après la description
        input(Fore.CYAN + "\nAppuyez sur Entrée pour continuer...")
        clear()
        print(Fore.YELLOW + "\nLancement de l'outil Lynis pour l'audit du système...\n")
        os.system('cd lynis && ./lynis audit system')
    elif choice == '0':
        print(Fore.RED + "\nFermeture du programme... À bientôt ! 👋")
        exit()
    else:
        print(Fore.RED + "Choix invalide, veuillez réessayer.\n")
def afficher_description_audit():
    clear()
    print(Fore.CYAN + Style.BRIGHT + "\n=== PHASE IAV-AUDIT : DESCRIPTION DES FONCTIONNALITÉS ===\n")

    print(Fore.GREEN + Style.BRIGHT + "🔧 Initialisation du programme")
    print("- Configuration des chemins d'accès aux fichiers nécessaires")
    print("- Vérification des permissions et propriétaires des fichiers\n")

    print(Fore.GREEN + Style.BRIGHT + "🖥️ Détection du système")
    print(Fore.WHITE + "- Identification du système d'exploitation et sa version")
    print("- Détection de l'environnement (physique, VM, conteneur)")
    print("- Vérification des composants système (systemd, gestionnaire de paquets)\n")

    print(Fore.GREEN + Style.BRIGHT + "🔐 Vérification de sécurité")
    print(Fore.WHITE + "- Exécution de tests de sécurité regroupés par catégories :")
    print("  * Authentification")
    print("  * Configuration réseau")
    print("  * Système de fichiers")
    print("  * Logiciels installés")
    print("  * Politiques de mot de passe")
    print("  * Et bien d'autres...\n")

    print(Fore.GREEN + Style.BRIGHT + "🧩 Gestion des plugins")
    print(Fore.WHITE + "- Chargement et exécution de plugins personnalisés")
    print("- Extensibilité en deux phases : Pré-analyse (avant les tests principaux) et Post-analyse (après les résultats)\n")

    print(Fore.GREEN + Style.BRIGHT + "📄 Génération de rapports")
    print(Fore.WHITE + "- Rapport détaillé avec résultats, recommandations et niveaux de risque\n")

    #wqinput(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")
def main():
    while True:
        clear()
        show_header()
        show_options()
        choice = input(Fore.WHITE + Style.BRIGHT + "Entrez votre choix [1/2/0] : ")
        handle_choice(choice)
        input(Fore.CYAN + "\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()

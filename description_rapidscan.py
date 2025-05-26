# description_rapidscan.py

from colorama import Fore, Style
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def afficher_description_rapidscan():
    clear()
    print(Fore.CYAN + Style.BRIGHT + "\n=== PHASE RAPIDSCAN : DESCRIPTION DES FONCTIONNALITÉS ===\n")

    print(Fore.GREEN + Style.BRIGHT + "🧰 Multi-outils intégrés")
    print(Fore.WHITE + "- Utilise une multitude d'outils de sécurité Linux :")
    print("  * nmap, wafw00f, theHarvester, nikto, dirb, etc.\n")

    print(Fore.GREEN + Style.BRIGHT + "🛡️ Détection de vulnérabilités")
    print(Fore.WHITE + "- Vérifie plusieurs types de vulnérabilités :")
    print("  * Failles Web (XSS, SQLi, LFI/RFI, CSRF)")
    print("  * Problèmes DNS (transferts de zone, fuites de sous-domaines)")
    print("  * Vulnérabilités SSL/TLS (Heartbleed, POODLE, FREAK)")
    print("  * Services exposés (FTP, Telnet, SMB, RDP)")
    print("  * CMS vulnérables (WordPress, Drupal, Joomla)")
    print("  * Failles réseau (Slowloris, Stuxnet)\n")

    print(Fore.GREEN + Style.BRIGHT + "📄 Génération de rapports")
    print(Fore.WHITE + "- Rapport vulnérabilités : rs.vul.<domaine>.<date>")
    print("- Fichier de débogage complet : rs.dbg.<domaine>.<date>\n")

    #input(Fore.CYAN + "Appuyez sur Entrée pour revenir au menu principal...")

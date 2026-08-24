# Foire Aux Questions

## 1. Aucune boîte de dialogue n'apparaît
Ce mod nécessite un programme backend supplémentaire pour fonctionner. Téléchargez le programme backend localisé ici : [https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest). Le fichier .exe téléchargé s'installera automatiquement à l'ouverture.

## 2. Problèmes de configuration de l'API
Il est recommandé d'utiliser l'API officielle DeepSeek. Dans le menu déroulant pour la connexion du modèle de dialogue, sélectionnez la page `custom(openai-compatible)` pour configurer :
- URL du serveur : `https://api.deepseek.com/beta`
- Clé API : Entrez votre propre clé API, qui peut être demandée sur [https://platform.deepseek.com](https://platform.deepseek.com).

OpenAI et OpenRouter devraient également être compatibles.

## 3. Aucune boîte de dialogue n'apparaît même lorsque le programme backend est en cours d'exécution après l'installation
**Solution** : Vous devez utiliser le mod de localisation.

Méthodes d'installation (choisissez une seule) :
1. Après avoir extrait les fichiers du mod de localisation téléchargé, écrasez directement les fichiers du mod original dans le répertoire Steam Workshop.
2. Placez le dossier du mod extrait `voices_of_the_court_mod-1.2.1-beta` dans le dossier mod du jeu. Ensuite, utilisez le Bloc-notes pour créer un nouveau fichier nommé `voices_of_the_court_mod-1.2.1-beta.mod` dans le dossier `Documents\Paradox Interactive\Crusader Kings III\mod` avec le contenu suivant :
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [Votre nom d'utilisateur PC ici] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

Si la boîte de dialogue n'apparaît toujours pas après avoir installé et activé le mod de localisation, le chemin du dossier utilisateur CK3 peut être incorrect, ou le jeu peut être en mode Ironman. Ce mod ne fonctionne pas en mode Ironman.

## 4. Erreur "TypeError: Cannot read properties of undefined (reading 'playerID')" avec du texte rouge lors de l'ouverture de la fenêtre de chat
**Solution** : Créez un dossier nommé `run` dans `Documents\Paradox Interactive\Crusader Kings III`. Entrez dans ce dossier et créez un fichier texte nommé `votc.txt`.

## 5. Les souvenirs récents ne sont pas lus lors des conversations avec les personnages
**Solution** :
1. Il s'agit d'un petit bug dans le programme backend de l'auteur original ; télécharger le backend localisé résout ce problème.
2. Cela peut également être dû à des limites de tokens de mémoire. Ajustez la taille `max memory tokens` dans la page des paramètres du programme backend. Après avoir ajusté les tokens de mémoire, vous devriez également augmenter `max new tokens` ; il est préférable que `max new tokens` soit supérieur à `max memory tokens`.

## 6. Le script de génération de prompt revient après le redémarrage du programme backend
**Solution** :
Enregistrez-le en tant que fichier séparé dans le dossier `custom`.

## Licence et Attribution

### Informations sur le Mod
- **Nom du Mod** : Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **Licence** : GNU General Public License v3.0 (GPLv3)
- **Version CK3 supportée** : 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### Notice GPLv3
Ce programme est un logiciel libre ; vous pouvez le redistribuer et/ou le modifier selon les termes de la GNU General Public License telle que publiée par la Free Software Foundation, soit la version 3 de la Licence, soit (à votre choix) toute version ultérieure.

Ce programme est distribué dans l'espoir qu'il sera utile, mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de QUALITÉ MARCHANDE ou d'ADÉQUATION À UN USAGE PARTICULIER. Consultez la GNU General Public License pour plus de détails.

Vous devriez avoir reçu une copie de la GNU General Public License avec ce programme. Si ce n'est pas le cas, consultez <https://www.gnu.org/licenses/>.

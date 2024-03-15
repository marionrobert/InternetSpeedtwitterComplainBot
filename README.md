# Bot Twitter pour Vérifier la Vitesse Internet

## Introduction
Ce projet automatise le processus de vérification de la vitesse Internet et envoie un tweet à un fournisseur de services Internet pour signaler les résultats. Il utilise Selenium pour effectuer un test de vitesse sur [speedtest.net](https://www.speedtest.net/) et envoie ensuite un tweet à un fournisseur de services Internet pour signaler toute disparité entre les vitesses promises et les vitesses réelles.

## Fonctionnalités
- Effectue un test de vitesse Internet sur [speedtest.net](https://www.speedtest.net/).
- Envoie un tweet à un fournisseur de services Internet pour signaler les vitesses réelles de téléchargement et de téléversement par rapport aux vitesses promises.

## Exigences
- Python 3.x
- Selenium
- Chrome WebDriver

## Installation et Configuration
1. Assurez-vous d'avoir Python installé sur votre système.
2. Installez la bibliothèque Selenium à l'aide de pip : `pip install selenium`.
3. Téléchargez le Chrome WebDriver compatible avec la version de votre navigateur Chrome.
4. Configurez les variables d'environnement `EMAIL`, `USERNAME`, `PASSWORD` pour votre compte Twitter.
5. Exécutez le script et surveillez vos tweets pour voir s'ils ont été envoyés avec succès.

## Exécution
Pour exécuter le bot :
1. Assurez-vous d'avoir Google Chrome installé sur votre système.
2. Exécutez le script Python ("main.py"). Le bot ouvrira un navigateur Chrome, effectuera un test de vitesse Internet sur [speedtest.net](https://www.speedtest.net/), se connectera à Twitter, et enverra un tweet à votre fournisseur de services Internet en signalant les vitesses réelles.

## Remarque
- Assurez-vous que la version de Chrome WebDriver utilisée est compatible avec la version de Chrome installée sur votre système.
- Soyez conscient des conditions d'utilisation de Twitter lors de l'envoi de tweets automatisés.
- Assurez-vous d'avoir les autorisations appropriées pour envoyer des tweets au fournisseur de services Internet.
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) d'Angela Yu sur la plateforme Udemy.

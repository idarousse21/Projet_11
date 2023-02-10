<h1 align ="center">Explication et lancement du code</h1>

------------------------------
<h2 align = "center"> Application et Bibliothèque</h2>

<p>
    Pour employer le code, tout d'abord, installez l'application python.
<ul>
    <li>
        <a href = "https://www.python.org/downloads/">Python </a>
    </li>
</ul>
</p>
<p>
    Nous utiliserons aussi les bibliothèques python:
<ul>
    <li>
        <a href = "https://flask.palletsprojects.com/en/2.2.x/">Flask </a>
    </li>
    <li>
        <a href = "https://docs.pytest.org/en/7.1.x/contents.html">Pytest</a>
    </li>
    <li>
        <a href = "https://docs.locust.io/en/stable/">Locust</a>
    </li>
</ul>
</p>
<h2 align = "center"> Lancement du code </h2>
<p>Pour commencer, vous devez lancer l'invite de commande et employer les commandes suivantes:
    <ol>
        <li>Clonez le projet:</li>
                <ul><li>git clone https://github.com/idarousse21/Projet_11 </li></ul>
            <li>Dirigez-vous sur le dossier cloné:</li>
                <ul><li>cd Projet_11 </li></ul>
            <li>Créez un environnement virtuel:</li>
                <ul><li>python -m venv env</li></ul>
            <li>Puis activation de l'environnement virtuel:</li>
                <ul><li>Sur Windows:</li></ul>
                env\Scripts\activate
                <ul><li>Sous Mac/Linus:</li></ul>
                source/env/Scripts/activate
            <li>Télécharger les bibliothèque nécessaire :</li>
                <ul><li>pip install -r requirements.txt</li></ul>
            <li>Executer le serveur Flask à partir de la racine du projet:</li>
                <ul><li>set FLASK_APP=server.py</li></ul>
            <li>Démarrer le serveur Flask:</li>
                <ul><li>flask run</li></ul>
            <li>Entrez l'url ci-dessous dans votre navigateur pour acceder au site: </li>
                <ul><li>http://127.0.0.1:5000/</li></ul>
    </ol>
</p>
<h2 align = "center"> Lancement des tests </h2>
<p>Pour lancer les test employer les commandes suivantes sur l'invite de commande :</p>
    <ul>
        <li>Tout les tests:</li>
            <ul><li>pytest</li></ul>
        <li>Test unit:</li>
            <ul><li>pytest pytest tests\test_unit</li></ul>
        <li>Test integration:</li>
            <ul><li>pytest "tests\test integration"</li></ul>
        <li>Test functional:</li>
            <ul><li>pytest tests\test_functional</li></ul>   
    </ul>
<h2 align = "center"> Lancement du test de perfomance</h2>
    <p>Sur une invite de commande</p>
    <ol>
        <li>Executer le serveur Flask à partir de la racine du projet:</li>
            <ul><li>set FLASK_APP=server.py</li></ul>
        <li>Démarrer le serveur Flask:</li>
            <ul><li>flask run</li></ul>
        <li>Démarrer le serveur Flask:</li>
            <ul><li>flask run</li></ul>
    <p>Ouvré une nouvelle invite de commande</p>
        <li>Acceder au dossier du test de performance:</li>
            <ul><li>cd Projet_11\tests\test_performance</li></ul>
        <li>Executer locust:</li>
            <ul><li>locust</li></ul>
        <li>Entrez l'url ci-dessous dans votre navigateur:</li>
            <ul><li>http://localhost:8089</li></ul>
        <li>Completer les informations demander:</li>
            <ul><li>Number of users: 6</li></ul>
            <ul><li>Spawn rate: 1</li></ul>
            <ul><li>Host: http://127.0.0.1:5000/</li></ul> 
    </ol>
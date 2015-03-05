# Collaboration sur le projet

Le but initial du TM était d'intégrer toutes les applications pour réaliser une
plateforme commune. Pour ce faire, et pour bénéficier de l'application d'authentification
utiliseurs définie dans l'application `common`, il faut procéder comme suit :

1.  Faire un fork de ce dépôt dans votre propre compte GitHub
2.  Cloner votre fork sur votre machine locale (ou sur Cloud9) en remplaçant `<username>` par votre nom d'utilisateur GitHub.
    ```{bash}
    $ git clone https://github.com/<username>/webmath2.git
    ```
3.  Intégrer votre application Django dans l'application globale. Un moyen de procéder est de copier votre dossier 
4.  Ajouter le dépôt Upstream (https://github.com/tmwebmath/webmath2.git)
    ```{bash}
    $ git remote add upstream https://github.com/tmwebmath/webmath2.git
    ```
4.  travailler dans la branche `develop` 
5.  Faire des *Pull Requests* de origin:develop ==> upstream:develop

# Question 

Comment intégrer le travail des étudiants (leur application) alors qu'ils ont
dans leur projet tout un dépôt ...

*   Comme je l'ai expliqué à quelques-uns : copier leur travail dans le fork de
    mon projet ...
*   Ajouter l'application common comme un sous-module de leur dépôt, mais cela
    limite les possibilités d'intégration.
*   Dans quelle branche faut-il travailler ?

# Suppression des double points dans les formulaires
Pour supprimer les doubles points : https://github.com/torchbox/wagtail/issues/130

# Créer des utilisateurs
Via l'administration -> user:admin password:12345
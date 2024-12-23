# Shop Service 

Ce projet propose une API sécurisée permettant de gérer des utilisateurs et d'interagir avec une base de données SQL via une infrastructure déployée sur Azure.

---

## 📄 **Documentation**

### 🔧 **Protocole d'utilisation du projet**

#### **1ère étape : Création d'un dépôt GitHub**
1. Créez un dépôt public dans votre propre compte GitHub.

#### **2ème étape : Cloner le dépôt**
1. Clonez ce dépôt dans votre environnement local avec :
   ```bash
   git clone https://github.com/<votre-username>/<nom-du-repo>.git
   ```

#### 3ème étape : Configuration des accès Azure ####
   1. Obtenez les informations nécessaires  à la configuration Azure en éxecutant la commande suivante:
      ```bash
    az ad sp create-for-rbac --name "shop-service-plan" --role Contributor --scopes /subscriptions/<subscriptionId>
     ```
   Remplacez ```<subscriptionId>``` par l'ID de votre abonnement Azure, que vous pouvez récupérer sur le portail Azure.

   2. Cette commande générera un JSON semblable à ceci :
  ```json
   {
    "appId": "votre-appId",
    "displayName": "shop-service-plan",
    "password": "votre-password",
    "tenant": "votre-tenant"
    }
   ```

   3. AJoutez ces informations comme secret dans votre dépôt GitHub sous la clé ```AZURE_CREDENTIALS```:
   ```json
    {
      "clientSecret": "votre-password",
      "subscriptionId": "votre-subscriptionId",
      "tenantId": "votre-tenant",
      "clientId": "votre-appId"
    }
   ```

#### 4ème étape : Push and Deploy
  1. Poussez ce projet dans votre dépôt en suivant ces étapes:
   ```bash
    git remote remove origin
    git remote add origin https://github.com/<votre-username>/<nom-du-repo>.git
    git push -u origin main
   ```
  En poussant le projet sur votre branche main, la ci-cd de déploiement se lancera et votre projet sera prêt à être utilisé !

#### 4ème étape : Ajout de la clé secrète.####
   1. Générez une clé secrète pour signer les tokens en utilisant un générateur de token.
   2. Ajoutez cette clé comme secret dans votre dépôt Github sous la clé ```SECRET_KEY```.


### 🔧 **Utilisation de l'API**

### 🌐 **Infrastructure du projet**



### ⚖️ **Licence**
Ce projet est sous licence MIT.
Cela couvre les étapes d'installation, du'tilisation, l'infrastructure et les tests.
Vous pouvez l'adapter selon vos besoins spécifiques.

   

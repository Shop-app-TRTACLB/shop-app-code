  # Création du serveur SQL
  resource "azurerm_mssql_server" "server" {
    name                        = "${var.database_name}-${var.suffix}"
    resource_group_name         = var.resource_group_name
    location                    = var.location
    version                     = "12.0"  # Exemple de version (à ajuster selon vos besoins)
    administrator_login         = var.admin_user
    administrator_login_password = var.admin_password
  }

 

  # Création de la base de données
  resource "azurerm_mssql_database" "db" {
    name      = "${var.database_name}-${var.suffix}"
    server_id = azurerm_mssql_server.server.id
  }

  # Création du Private Endpoint
  resource "azurerm_private_endpoint" "db_private_endpoint" {
    name                = "db-private-endpoint"
    location            = var.location
    resource_group_name = var.resource_group_name
    subnet_id           = var.subnet_id  # Utilisation de la variable pour le subnet ID

    private_service_connection {
      name                           = "sql-private-connection"
      private_connection_resource_id = azurerm_mssql_server.server.id
      subresource_names              = ["sqlServer"]
      is_manual_connection           = false  # Connexion automatique
    }
  }

 

 


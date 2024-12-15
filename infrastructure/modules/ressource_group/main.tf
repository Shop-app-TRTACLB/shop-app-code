resource "azurerm_resource_group" "rg" {
  name     = "${var.resource_group_name}-${var.suffix}"  # Utilisation du suffixe aléatoire
  location = var.location
}



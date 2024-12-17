output "sql_connection_string" {
  value =azurerm_mssql_server.server.fully_qualified_domain_name
}
  
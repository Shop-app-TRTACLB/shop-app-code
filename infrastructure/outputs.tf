output "app_name"{
    value = module.backend_app.app_name
}

output "sql_connection_string"{
    value = module.database.sql_connection_string
}

output "sql_connection_string_without" {
  value = module.database.sql_connection_string_without
}


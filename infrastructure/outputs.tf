output "app_name"{
    value = module.backend_app.app_name
}



output "rg_name"{
    value = module.resource_group.name
}


output "app_service_ips" {
  value = module.database.app_service_ips
}
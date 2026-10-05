package model

type RoutePath struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	RouteID int64 `json:"route_id"`
	RoutePathName string `json:"route_path_name"`
	RouteBackendService string `json:"route_backend_service"`
	RouteBackendServicePort int32 `json:"route_backend_service_port"`
}

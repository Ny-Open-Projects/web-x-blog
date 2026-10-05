package model

type Route struct{
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	RouteName string `json:"route_name"`
	RouteNamespace string `json:"route_namespace"`
	RouteHost string `json:"route_host"`
	RoutePath []RoutePath `gorm:"ForeignKey:RouteID" json:"route_path"`
}


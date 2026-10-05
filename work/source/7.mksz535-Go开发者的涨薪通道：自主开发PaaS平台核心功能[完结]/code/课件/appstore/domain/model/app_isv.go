package model

//服务商
type AppIsv struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppIsvName string `json:"app_isv_name"`
	AppIsvDetail string `json:"app_isv_detail"`
}

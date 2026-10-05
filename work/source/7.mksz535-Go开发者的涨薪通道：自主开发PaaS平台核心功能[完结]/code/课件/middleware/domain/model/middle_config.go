package model

//中间件配置的结构体
type MiddleConfig struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	//关联的中间件ID
	MiddleID int64 `json:"middle_id"`
	//可能存在的root 用户
	MiddleConfigRootUser string `json:"middle_config_root_user"`
	//可能存在的root 密码
	MiddleConfigRootPwd string `json:"middle_config_root_pwd"`
	//可能存在的普通用户
	MiddleConfigUser string `json:"middle_config_user"`
	//普通用户的密码
	MiddleConfigPwd string `json:"middle_config_pwd"`
	//预置数据库名称
	MiddleConfigDataBase string `json:"middle_config_data_base"`
	//其它设置
}

package common

import "github.com/asim/go-micro/v3/config"

//创建结构体
type MysqlConfig struct {
	Host string `json:"host"`
	User string `json:"user"`
	Pwd string `json:"pwd"`
	Database string `json:"database"`
	Port string `json:"port"`
}

func GetMysqlFromConsul(config config.Config,path ...string) *MysqlConfig  {
	mysqlConfig := &MysqlConfig{}
	config.Get(path...).Scan(mysqlConfig)
	return mysqlConfig
}

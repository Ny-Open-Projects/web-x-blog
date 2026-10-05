package model

type MiddlePort struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	//主要用来关联中间件的ID
	MiddleID int64 `json:"middle_id"`
	//中间件开放的端口
	MiddlePort int32 `json:"middle_port"`
	//中间件开放的端口协议
	MiddleProtocol string `json:"middle_protocol"`
}

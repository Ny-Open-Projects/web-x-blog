package model

//中间件的存储盘
type MiddleStorage struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	//关联的中间件ID
	MiddleID int64 `json:"middle_id"`
	//存储名称
	MiddleStorageName string `json:"middle_storage_name"`
	//存储的大小
	MiddleStorageSize float32 `json:"middle_storage_size"`
	//存储需要挂载的目录
	MiddleStoragePath string `json:"middle_storage_path"`
	//存储创建的类型
	MiddleStorageClass string `json:"middle_storage_class"`
	//存储的权限
	MiddleStorageAccessMode string `json:"middle_storage_access_mode"`
}

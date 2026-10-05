package model

type Volume struct{
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	//存储的名称
	VolumeName string `json:"volume_name"`
	//存储的所属的命名空间
	VolumeNamespace string `json:"volume_namespace"`
	//存储的访问模式，RWO,ROX,RWX
	VolumeAccessMode string `json:"volume_access_mode"`
	//sc 的 class name
	VolumeStorageClassName string `json:"volume_storage_class_name"`
	//请求资源的大小
	VolumeRequest float32 `json:"volume_request"`
	//存储类型 Block，filesystem
	VolumePersistentVolumeMode string `json:"volume_persistent_volume_mode"`
}


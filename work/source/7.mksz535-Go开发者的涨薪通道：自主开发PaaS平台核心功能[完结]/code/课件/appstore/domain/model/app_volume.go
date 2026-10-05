package model

//云应用存储模板
type AppVolume struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	AppVolumeID int64 `json:"app_volume_id"`
}

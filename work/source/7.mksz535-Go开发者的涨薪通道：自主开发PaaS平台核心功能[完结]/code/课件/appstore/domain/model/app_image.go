package model

//云引用图片
type AppImage struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	AppID int64 `json:"app_id"`
	//图片地址
	AppImageSrc string `json:"app_image_src"`
}

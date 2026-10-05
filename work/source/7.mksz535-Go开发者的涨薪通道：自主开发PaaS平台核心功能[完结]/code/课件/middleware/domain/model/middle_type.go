package model

//中间件类型
type MiddleType struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	//中间件类型名称
	MiddleTypeName string `json:"middle_type_name"`
	//中间件图片地址
	MiddleTypeImageSrc string `json:"middle_type_image_src"`
	//中间件的版本
	MiddleVersion[] MiddleVersion `gorm:"ForeignKey:MiddleTypeID" json:"middle_version"`
}

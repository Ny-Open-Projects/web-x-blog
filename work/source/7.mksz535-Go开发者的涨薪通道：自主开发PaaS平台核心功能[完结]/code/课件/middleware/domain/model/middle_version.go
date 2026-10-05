package model

type MiddleVersion struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	MiddleTypeID int64 `json:"middle_type_id"`
	//镜像地址
	MiddleDockerImage string `json:"middle_docker_image"`
	//镜像版本
	MiddleVS string `json:"middle_vs"`
	//MiddleDockerImage:MiddleVS
	//其它
}

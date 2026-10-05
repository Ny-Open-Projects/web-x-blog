package model

type PodEnv struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	PodID int64 `json:"pod_id"`
	EnvKey string `json:"env_key"`
	EnvValue string `json:"env_value"`
}

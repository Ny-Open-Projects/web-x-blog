package model

type Svc struct{
	ID int64 `gorm:"primary_key;not_null;auto_increment"`
	//服务名称
	SvcName string `gorm:"unique_index;not_null" json:"svc_name"`
	//服务名称命名空间
	SvcNamespace string `gorm:"not_null" json:"svc_namespace"`
	//绑定的POD名称
	SvcPodName string `gorm:"not_null" json:"svc_pod_name"`
	//ClusterIP，NodePort，LoadBalancer,ExternalName
	SvcType string `json:"svc_type"`
	//type类型为：ExternalName 时候启用该字段
	SvcExternalName string `json:"svc_external_name"`
	//业务侧的团队ID
	SvcTeamId string `json:"svc_team_id"`
	//服务上的端口设置
	SvcPort[] SvcPort `gorm:"ForeignKey:SvcID" json:"svc_port"`


}


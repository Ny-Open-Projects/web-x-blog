package controllers

import (
	"imooc.com/lottery/models"
	"imooc.com/lottery/comm"
	"imooc.com/lottery/services"
)

func (api *LuckyApi) prizeLarge(ip string,
	uid int, username string,
	userinfo *models.LtUser,
	blackipInfo *models.LtBlackip) {
	userService := services.NewUserService()
	blackipService := services.NewBlackipService()
	nowTime := comm.NowUnix()
	blackTime := 30 * 86400
	// 更新用户的黑名单信息
	if userinfo == nil || userinfo.Id <= 0 || userinfo.Username == "" {
		userinfo = &models.LtUser{
			Id:			uid,
			Username:   username,
			Blacktime:  nowTime+blackTime,
			SysCreated: nowTime,
			SysIp:      ip,
		}
		userService.Create(userinfo)
	} else {
		userinfo = &models.LtUser{
			Id: uid,
			Blacktime:nowTime+blackTime,
			SysUpdated:nowTime,
		}
		userService.Update(userinfo, nil)
	}
	// 更新要IP的黑名单信息
	if blackipInfo == nil || blackipInfo.Id <= 0 {
		blackipInfo = &models.LtBlackip{
			Ip:         ip,
			Blacktime:  nowTime+blackTime,
			SysCreated: nowTime,
		}
		blackipService.Create(blackipInfo)
	} else {
		blackipInfo.Blacktime = nowTime + blackTime
		blackipInfo.SysUpdated = nowTime
		blackipService.Update(blackipInfo, nil)
	}
}
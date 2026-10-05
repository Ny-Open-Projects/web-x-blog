package controllers

import (
	"imooc.com/lottery/web/utils"
	"imooc.com/lottery/conf"
)

// 作废，验证用户的IP，今天的抽奖次数是否超过每天最大允许的参与次数
func (c *IndexController) _checkLimitIpday(ip string) bool {
	num := utils.IncrIpLucyNum(ip)
	if num > conf.IpLimitMax {
		return false
	} else if num > conf.IpPrizeMax {
		return false
	}
	return true
}

// 作废，验证用户的IP，今天的抽奖次数是否超过每天最大抽奖次数
func (c *IndexController) _checkIpday(ip string) bool {
	num := utils.IncrIpLucyNum(ip)
	if num > conf.IpPrizeMax {
		return false
	}
	return true
}

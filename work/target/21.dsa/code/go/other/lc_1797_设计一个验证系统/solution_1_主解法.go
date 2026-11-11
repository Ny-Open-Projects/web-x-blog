// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354494
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type AuthenticationManager struct { // 定义类型
	expiresAt map[string]int // expiresAt 映射表[string]int
	ttl       int            // ttl int
}

func NewAuthenticationManager(ttl int) *AuthenticationManager { // 定义函数/方法 NewAuthenticationManager
	return &AuthenticationManager{expiresAt: make(map[string]int), ttl: ttl}
}

func (a *AuthenticationManager) generate(token string, currentTime int) { // 定义函数/方法 generate
	a.expiresAt[token] = currentTime + a.ttl // 把 currentTime 加 数组.ttl 写入 a.expiresAt[token]
}

func (a *AuthenticationManager) renew(token string, currentTime int) int { // 定义函数/方法 renew
	if exp, ok := a.expiresAt[token]; ok && exp > currentTime { // 若 exp, ok : 赋值为 数组.expiresAt[token]; ok 且 exp 超过 currentTime
		a.expiresAt[token] = currentTime + a.ttl // 把 currentTime 加 数组.ttl 写入 a.expiresAt[token]
		return 1                                 // 返回 1
	}
	return 0 // 返回 0
}

func (a *AuthenticationManager) countValidTokens(currentTime int) int { // 定义函数/方法 countValidTokens
	count := 0                        // 把 0 写入 count :
	for _, exp := range a.expiresAt { // 同时取 _ 与 exp 遍历
		if exp > currentTime { // 若 exp 超过 currentTime
			count++ // 计数 加一
		}
	}
	return count // 返回 计数
}

func main() { // 程序入口：跑内嵌自测用例
	a := NewAuthenticationManager(5)        // 把 NewAuthenticationManager(5) 写入 a :
	a.generate("aaa", 1)                    // 数组.generate(「aaa」, 1)
	ok := true                              // 把 true 写入 ok :
	if v := a.countValidTokens(3); v != 1 { // 若 值 : 赋值为 数组.countValidTokens(3); 值 不等于 1
		ok = false                          // 把 false 写入 ok
		fmt.Printf("FAIL count(3)=%d\n", v) // 打印输出
	}
	if v := a.renew("aaa", 4); v != 1 { // 若 值 : 赋值为 数组.renew(「aaa」, 4); 值 不等于 1
		ok = false                          // 把 false 写入 ok
		fmt.Printf("FAIL renew(4)=%d\n", v) // 打印输出
	}
	if v := a.countValidTokens(6); v != 1 { // 若 值 : 赋值为 数组.countValidTokens(6); 值 不等于 1
		ok = false                          // 把 false 写入 ok
		fmt.Printf("FAIL count(6)=%d\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

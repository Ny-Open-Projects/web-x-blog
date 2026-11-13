// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354313
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type BrowserHistory struct { // 定义类型
	history []string // history []string
	current int      // current int
}

func Constructor(homepage string) BrowserHistory { // 定义函数/方法 Constructor
	return BrowserHistory{history: []string{homepage}, current: 0} // 返回 BrowserHistory{history: []string{homepage}, current: 0}
}

func (this *BrowserHistory) Visit(url string) { // 定义函数/方法 Visit
	this.history = this.history[:this.current+1] // 把 this.history[:this.current 加 1] 写入 this.history
	this.history = append(this.history, url)     // 把 append(this.history, url) 写入 this.history
	this.current = len(this.history) - 1         // 把 长度(this.history) 减 1 写入 this.current
}

func (this *BrowserHistory) Back(steps int) string { // 定义函数/方法 Back
	this.current = max(0, this.current-steps) // 把 取较大值 0, this.current 减 steps) 写入 this.current
	return this.history[this.current]         // 返回 this.history[this.current]
}

func (this *BrowserHistory) Forward(steps int) string { // 定义函数/方法 Forward
	this.current = min(len(this.history)-1, this.current+steps)
	return this.history[this.current] // 返回 this.history[this.current]
}

func max(a, b int) int { // 定义函数/方法 max
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func min(a, b int) int { // 定义函数/方法 min
	if a < b { // 若 数组 小于 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	browser := Constructor("leetcode.com") // 把 Constructor(「leetcode.com」) 写入 browser :
	browser.Visit("google.com")            // browser.Visit(「google.com」)
	browser.Visit("facebook.com")          // browser.Visit(「facebook.com」)
	browser.Visit("youtube.com")           // browser.Visit(「youtube.com」)
	out1 := browser.Back(1)                // 把 browser.Back(1) 写入 out1 :
	out2 := browser.Forward(2)             // 把 browser.Forward(2) 写入 out2 :
	if !reflect.DeepEqual([]string{out1, out2}, []string{"facebook.com", "youtube.com"}) {
		fmt.Println("FAIL", out1, out2) // 打印输出
		return                          // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

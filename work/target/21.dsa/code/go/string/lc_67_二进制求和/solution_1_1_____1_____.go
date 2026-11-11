package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 二进制求和：从低位逐位相加（忠实于 bin(int(a,2)+int(b,2)) 的结果）
func addBinary(a, b string) string { // 定义函数/方法 addBinary
	i, j := len(a)-1, len(b)-1          // 把 长度(数组) 减 1, 长度(b) 减 1 写入 i, j :
	carry := 0                          // 把 0 写入 carry :
	var sb []byte                       // var sb []byte
	for i >= 0 || j >= 0 || carry > 0 { // 把 0 或 下标 j 不低于 0 或 carry 超过 0 { 写入 for i >
		sum := carry // 把 carry 写入 sum :
		if i >= 0 {  // 若 下标 i 不低于 0
			sum += int(a[i] - '0') // 累计和累加 int(数组[下标 i] 减 '0')
			i--                    // 下标 i 减一
		}
		if j >= 0 { // 若 下标 j 不低于 0
			sum += int(b[j] - '0') // 累计和累加 int(b[下标 j] 减 '0')
			j--                    // 下标 j 减一
		}
		sb = append([]byte{byte('0' + sum%2)}, sb...) // 把 append([]byte{byte('0' 加 累计和 对…取模 2)}, sb...) 写入 sb
		carry = sum / 2                               // 把 累计和 除以 2 写入 carry
	}
	return string(sb) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		a, b, want string // 数组, b, want string
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{"11", "1", "100"},
		{"1010", "1011", "10101"},
		{"0", "0", "0"},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := addBinary(c.a, c.b) // 把 addBinary(字符.数组, 字符.b) 写入 got :
		if got != c.want {         // 若 got 不等于 字符.want
			fmt.Printf("FAIL: addBinary(%s,%s)=%s want %s\n", c.a, c.b, got, c.want) // 打印输出
			ok = false                                                               // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

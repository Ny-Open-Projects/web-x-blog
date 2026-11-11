// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"strings" // 「strings」
)

// Rule 规则类：规则串中的不同字符表示不同的前进命令，循环使用（方案 11）。
type Rule struct { // 定义类型
	data   []byte // data []byte
	idx    int    // idx int
	length int    // 长度 int
}

func NewRule(r string) *Rule { // 定义函数/方法 NewRule
	return &Rule{data: []byte(r), idx: 0, length: len(r)} // 返回 按位与 Rule{data: []byte(右指针), idx: 0, 长度: 长度(右指针)}
}

// next 返回当前命令并推进（对应 python __next__）
func (r *Rule) next() byte { // 定义函数/方法 next
	ch := r.data[r.idx]            // 把 右指针.data[右指针.idx] 写入 ch :
	r.idx = (r.idx + 1) % r.length // 把 (右指针.idx 加 1) 对…取模 右指针.长度 写入 r.idx
	return ch                      // 返回 字符
}

// peek 返回当前命令但不推进
func (r *Rule) peek() byte { // 定义函数/方法 peek
	return r.data[r.idx] // 返回 右指针.data[右指针.idx]
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :

	// 正常用例：ESVM 循环 10 次
	r := NewRule("ESVM")      // 把 NewRule(「ESVM」) 写入 r :
	var sb strings.Builder    // var sb strings.Builder
	for i := 0; i < 10; i++ { // 让 下标 i 从 0 开始计数
		sb.WriteByte(r.next()) // sb.WriteByte(右指针.下一个())
	}
	if sb.String() != "ESVMESVMES" { // 若 sb.String() 不等于 「ESVMESVMES」
		ok = false                                                                      // 把 false 写入 ok
		fmt.Printf("FAIL Rule(ESVM) next 10 = %q want %q\n", sb.String(), "ESVMESVMES") // 打印输出
	}
	if r.peek() != 'V' { // 若 右指针.peek() 不等于 'V'
		ok = false                                                    // 把 false 写入 ok
		fmt.Printf("FAIL peek = %q want %q\n", string(r.peek()), "V") // 打印输出
	}

	// 正常用例：semv 循环 6 次
	r2 := NewRule("semv")    // 把 NewRule(「semv」) 写入 r2 :
	var sb2 strings.Builder  // var sb2 strings.Builder
	for i := 0; i < 6; i++ { // 让 下标 i 从 0 开始计数
		sb2.WriteByte(r2.next()) // sb2.WriteByte(r2.下一个())
	}
	if sb2.String() != "semvse" { // 若 sb2.String() 不等于 「semvse」
		ok = false                                                                  // 把 false 写入 ok
		fmt.Printf("FAIL Rule(semv) next 6 = %q want %q\n", sb2.String(), "semvse") // 打印输出
	}
	if r2.peek() != 'm' { // 若 r2.peek() 不等于 '映射表'
		ok = false                                                     // 把 false 写入 ok
		fmt.Printf("FAIL peek = %q want %q\n", string(r2.peek()), "m") // 打印输出
	}

	// 边界用例：单字符规则
	r3 := NewRule("A")       // 把 NewRule(「A」) 写入 r3 :
	var sb3 strings.Builder  // var sb3 strings.Builder
	for i := 0; i < 3; i++ { // 让 下标 i 从 0 开始计数
		sb3.WriteByte(r3.next()) // sb3.WriteByte(r3.下一个())
	}
	if sb3.String() != "AAA" { // 若 sb3.String() 不等于 「AAA」
		ok = false                                                            // 把 false 写入 ok
		fmt.Printf("FAIL Rule(A) next 3 = %q want %q\n", sb3.String(), "AAA") // 打印输出
	}

	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

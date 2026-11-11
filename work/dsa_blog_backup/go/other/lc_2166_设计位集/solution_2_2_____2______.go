// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145370422
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Bitset stores bits one-per-int; Flip uses a lazy inverted flag.
type Bitset struct { // 定义类型
	arr      []int // 数组 []int
	cnt      int   // 计数 int
	reversed int   // reversed int
}

func Constructor(size int) *Bitset { // 定义函数/方法 Constructor
	return &Bitset{arr: make([]int, size)} // 返回 按位与 Bitset{数组: make([]int, 大小)}
}

func (b *Bitset) Fix(idx int) { // 定义函数/方法 Fix
	if (b.arr[idx] ^ b.reversed) == 0 { // 若 b.数组[idx] 按位异或 b.reversed) 等于 0
		b.arr[idx] ^= 1 // 把 1 写入 b.arr[idx] ^
		b.cnt++         // b.计数 加一
	}
}

func (b *Bitset) Unfix(idx int) { // 定义函数/方法 Unfix
	if (b.arr[idx] ^ b.reversed) == 1 { // 若 b.数组[idx] 按位异或 b.reversed) 等于 1
		b.arr[idx] ^= 1 // 把 1 写入 b.arr[idx] ^
		b.cnt--         // b.计数 减一
	}
}

func (b *Bitset) Flip() { // 定义函数/方法 Flip
	b.reversed ^= 1            // 把 1 写入 b.reversed ^
	b.cnt = len(b.arr) - b.cnt // 把 长度(b.数组) 减 b.计数 写入 计数
}

func (b *Bitset) All() bool  { return b.cnt == len(b.arr) } // 定义函数/方法 All
func (b *Bitset) One() bool  { return b.cnt > 0 }           // 定义函数/方法 One
func (b *Bitset) Count() int { return b.cnt }               // 定义函数/方法 Count

func (b *Bitset) ToString() string { // 定义函数/方法 ToString
	res := make([]byte, len(b.arr)) // 把 make([]byte, 长度(b.数组)) 写入 res :
	for i, bit := range b.arr {     // 同时取 下标 i 与 bit 遍历
		res[i] = byte('0' + (bit ^ b.reversed)) // 把 byte('0' 加 (bit 按位异或 b.reversed)) 写入 res[i]
	}
	return string(res) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	b := Constructor(5)                  // 把 Constructor(5) 写入 b :
	b.Fix(0)                             // b.Fix(0)
	b.Fix(3)                             // b.Fix(3)
	ok := true                           // 把 true 写入 ok :
	if s := b.ToString(); s != "10010" { // 若 字符串 : 赋值为 b.ToString(); 字符串 不等于 「10010」
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL toString1=%q\n", s) // 打印输出
	}
	if c := b.Count(); c != 2 { // 若 字符 : 赋值为 b.Count(); 字符 不等于 2
		ok = false                        // 把 false 写入 ok
		fmt.Printf("FAIL count1=%d\n", c) // 打印输出
	}
	b.Flip()                             // b.Flip()
	if s := b.ToString(); s != "01101" { // 若 字符串 : 赋值为 b.ToString(); 字符串 不等于 「01101」
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL toString2=%q\n", s) // 打印输出
	}
	if c := b.Count(); c != 3 { // 若 字符 : 赋值为 b.Count(); 字符 不等于 3
		ok = false                        // 把 false 写入 ok
		fmt.Printf("FAIL count2=%d\n", c) // 打印输出
	}
	b.Unfix(0)                           // b.Unfix(0)
	if s := b.ToString(); s != "01101" { // 若 字符串 : 赋值为 b.ToString(); 字符串 不等于 「01101」
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL toString3=%q\n", s) // 打印输出
	}
	if a := b.All(); a != false { // 若 数组 : 赋值为 b.All(); 数组 不等于 false
		ok = false              // 把 false 写入 ok
		fmt.Println("FAIL all") // 打印输出
	}
	if o := b.One(); o != true { // 若 o : 赋值为 b.One(); o 不等于 true
		ok = false              // 把 false 写入 ok
		fmt.Println("FAIL one") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

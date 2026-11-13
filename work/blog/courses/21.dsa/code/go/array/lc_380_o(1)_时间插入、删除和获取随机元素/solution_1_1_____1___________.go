// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345735
package main // 引入依赖

import (
	"fmt"       // 「fmt」
	"math/rand" // 「math 除以 rand」
	"os"        // 「os」
)

type RandomizedSet struct { // 定义类型
	nums    []int       // 数组 []int
	indices map[int]int // indices 映射表[int]int
}

func NewRandomizedSet() *RandomizedSet { // 定义函数/方法 NewRandomizedSet
	return &RandomizedSet{indices: map[int]int{}} // 返回 按位与 RandomizedSet{indices: 映射表[int]int{}}
}

func (r *RandomizedSet) insert(val int) bool { // 定义函数/方法 insert
	if _, ok := r.indices[val]; ok { // 若 _, ok : 赋值为 右指针.indices[值]; ok
		return false // 返回 false
	}
	r.indices[val] = len(r.nums) // 把 长度(右指针.数组) 写入 r.indices[val]
	r.nums = append(r.nums, val) // 把 append(右指针.数组, 值) 写入 数组
	return true                  // 返回 true
}

func (r *RandomizedSet) remove(val int) bool { // 定义函数/方法 remove
	if _, ok := r.indices[val]; !ok { // 若 _, ok : 赋值为 右指针.indices[值]; 取反 ok
		return false // 返回 false
	}
	idx := r.indices[val]           // 把 右指针.indices[值] 写入 idx :
	last := r.nums[len(r.nums)-1]   // 把 右指针.数组[长度(右指针.数组) 减 1] 写入 last :
	r.nums[idx] = last              // 把 last 写入 r.nums[idx]
	r.indices[last] = idx           // 把 idx 写入 r.indices[last]
	r.nums = r.nums[:len(r.nums)-1] // 把 右指针.数组[:长度(右指针.数组) 减 1] 写入 数组
	delete(r.indices, val)          // delete(右指针.indices, 值)
	return true                     // 返回 true
}

func (r *RandomizedSet) getRandom() int { // 定义函数/方法 getRandom
	return r.nums[rand.Intn(len(r.nums))] // 返回 右指针.数组[rand.Intn(长度(右指针.数组))]
}

func main() { // 程序入口：跑内嵌自测用例
	rs := NewRandomizedSet() // 把 NewRandomizedSet() 写入 rs :
	ok := true               // 把 true 写入 ok :
	if !rs.insert(1) {       // 若 取反 rs 插入 1
		ok = false                                  // 把 false 写入 ok
		fmt.Println("FAIL insert(1) expected true") // 打印输出
	}
	if rs.remove(2) { // 若 rs 弹出 2
		ok = false                                   // 把 false 写入 ok
		fmt.Println("FAIL remove(2) expected false") // 打印输出
	}
	if !rs.insert(2) { // 若 取反 rs 插入 2
		ok = false                                  // 把 false 写入 ok
		fmt.Println("FAIL insert(2) expected true") // 打印输出
	}
	g := rs.getRandom()   // 把 rs.getRandom() 写入 g :
	if g != 1 && g != 2 { // 若 g 不等于 1 且 g 不等于 2
		ok = false                                             // 把 false 写入 ok
		fmt.Printf("FAIL getRandom()=%v expected 1 or 2\n", g) // 打印输出
	}
	if !rs.remove(1) { // 若 取反 rs 弹出 1
		ok = false                                  // 把 false 写入 ok
		fmt.Println("FAIL remove(1) expected true") // 打印输出
	}
	if rs.insert(2) { // 若 rs 插入 2
		ok = false                                                     // 把 false 写入 ok
		fmt.Println("FAIL insert(2) expected false (already present)") // 打印输出
	}
	if rs.getRandom() != 2 { // 若 rs.getRandom() 不等于 2
		ok = false                                                 // 把 false 写入 ok
		fmt.Printf("FAIL getRandom() expected 2 (only element)\n") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

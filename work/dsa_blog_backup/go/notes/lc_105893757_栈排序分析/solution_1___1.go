// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

// SortedStack 有序栈：push 时通过辅助栈把元素插入到正确位置，使栈底->栈顶保持升序（栈顶最小）。
type SortedStack struct { // 定义类型
	data []int // data []int
}

func (s *SortedStack) push(val int) { // 定义函数/方法 push
	temp := []int{}                                      // 把 []int{} 写入 temp :
	for len(s.data) > 0 && s.data[len(s.data)-1] < val { // for 长度(字符串.data) 超过 0 且 字符串.data[长度(字符串.data) 减 1] 小于 值 {
		temp = append(temp, s.data[len(s.data)-1]) // 把 append(临时变量, 字符串.data[长度(字符串.data) 减 1]) 写入 临时变量
		s.data = s.data[:len(s.data)-1]            // 把 字符串.data[:长度(字符串.data) 减 1] 写入 s.data
	}
	s.data = append(s.data, val) // 把 append(字符串.data, 值) 写入 s.data
	for len(temp) > 0 {          // for 长度(临时变量) 超过 0 {
		s.data = append(s.data, temp[len(temp)-1]) // 把 append(字符串.data, 临时变量[长度(临时变量) 减 1]) 写入 s.data
		temp = temp[:len(temp)-1]                  // 把 临时变量[:长度(临时变量) 减 1] 写入 临时变量
	}
}

func (s *SortedStack) pop() (int, bool) { // 定义函数/方法 pop
	if len(s.data) == 0 { // 若 长度(字符串.data) 等于 0
		return 0, false // 返回 0, false
	}
	v := s.data[len(s.data)-1]      // 把 字符串.data[长度(字符串.data) 减 1] 写入 v :
	s.data = s.data[:len(s.data)-1] // 把 字符串.data[:长度(字符串.data) 减 1] 写入 s.data
	return v, true                  // 返回 值, true
}

func (s *SortedStack) peek() (int, bool) { // 定义函数/方法 peek
	if len(s.data) == 0 { // 若 长度(字符串.data) 等于 0
		return 0, false // 返回 0, false
	}
	return s.data[len(s.data)-1], true // 返回 字符串.data[长度(字符串.data) 减 1], true
}

func (s *SortedStack) isEmpty() bool { // 定义判定函数 isEmpty
	return len(s.data) == 0 // 返回 长度(字符串.data) 等于 0
}

func (s *SortedStack) sortVals() []int { // 定义函数/方法 sortVals
	cp := make([]int, len(s.data)) // 把 make([]int, 长度(字符串.data)) 写入 cp :
	copy(cp, s.data)               // copy(cp, 字符串.data)
	sort.Ints(cp)                  // sort.Ints(cp)
	return cp                      // 返回 cp
}

func eqIntSlice(a, b []int) bool { // 定义函数/方法 eqIntSlice
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :

	// 正常用例：push [1,3,2,4]，栈内保持升序，pop 依次输出最小值
	st := &SortedStack{}                  // 把 按位与 SortedStack{} 写入 st :
	for _, v := range []int{1, 3, 2, 4} { // 同时取 _ 与 值 遍历
		st.push(v) // 把 值 压入栈/数组尾部
	}
	if got := st.sortVals(); !eqIntSlice(got, []int{1, 2, 3, 4}) {
		ok = false                                           // 把 false 写入 ok
		fmt.Printf("FAIL sortVals=%v want [1 2 3 4]\n", got) // 打印输出
	}
	if v, exist := st.peek(); !exist || v != 1 { // 若 值, exist : 赋值为 st.peek(); 取反 exist 或 值 不等于 1
		ok = false                                                  // 把 false 写入 ok
		fmt.Printf("FAIL peek=%v exist=%v want 1 true\n", v, exist) // 打印输出
	}
	out := []int{}      // 把 []int{} 写入 out :
	for !st.isEmpty() { // for 取反 st.isEmpty() {
		v, _ := st.pop()     // 弹出栈顶元素
		out = append(out, v) // 把 append(out, 值) 写入 out
	}
	if !eqIntSlice(out, []int{1, 2, 3, 4}) { // 若 取反 eqIntSlice(out, []int{1, 2, 3, 4}
		ok = false                                               // 把 false 写入 ok
		fmt.Printf("FAIL pop sequence=%v want [1 2 3 4]\n", out) // 打印输出
	}

	// 边界用例：空栈 pop/peek 返回不存在，isEmpty 为 true
	empty := &SortedStack{} // 把 按位与 SortedStack{} 写入 empty :
	if !empty.isEmpty() {   // 若 取反 empty.isEmpty(
		ok = false                                 // 把 false 写入 ok
		fmt.Println("FAIL isEmpty on empty stack") // 打印输出
	}
	if _, exist := empty.pop(); exist { // 若 _, exist : 赋值为 empty 弹出 ); exist
		ok = false                                              // 把 false 写入 ok
		fmt.Println("FAIL pop on empty stack should not exist") // 打印输出
	}
	if _, exist := empty.peek(); exist { // 若 _, exist : 赋值为 empty.peek(); exist
		ok = false                                               // 把 false 写入 ok
		fmt.Println("FAIL peek on empty stack should not exist") // 打印输出
	}

	// 边界用例：单个元素
	single := &SortedStack{}                                   // 把 按位与 SortedStack{} 写入 single :
	single.push(42)                                            // 把 42 压入栈/数组尾部
	if got := single.sortVals(); !eqIntSlice(got, []int{42}) { // 若 got : 赋值为 single.sortVals(); 取反 eqIntSlice(got, []int{42}
		ok = false                                             // 把 false 写入 ok
		fmt.Printf("FAIL single sortVals=%v want [42]\n", got) // 打印输出
	}

	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

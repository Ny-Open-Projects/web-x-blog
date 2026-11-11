// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Matrix 面向对象版：矩阵类，封装填充与打印（方案 3）。
type Matrix struct { // 定义类型
	N int     // N int
	M [][]int // M [][]int
}

func NewMatrix(size int) *Matrix { // 定义函数/方法 NewMatrix
	m := make([][]int, size) // 把 make([][]int, 大小) 写入 m :
	for i := range m {       // 把 range 映射表 { 写入 for i :
		m[i] = make([]int, size) // 把 make([]int, 大小) 写入 m[i]
	}
	return &Matrix{N: size, M: m} // 返回 按位与 Matrix{N: 大小, M: 映射表}
}

func (mx *Matrix) fill(num, begin, size int) int { // 定义函数/方法 fill
	if size == 0 { // 若 大小 等于 0
		return num // 返回 num
	}
	if size == 1 { // 若 大小 等于 1
		mx.M[begin][begin] = num // 把 num 写入 mx.M[begin][begin]
		return num + 1           // 返回 num 加 1
	}
	for j := 0; j < size-1; j++ { // 让 下标 j 从 0 开始计数
		mx.M[begin+j][begin] = num // 把 num 写入 mx.M[begin+j][begin]
		num++                      // num 加一
	}
	for j := 0; j < size-1; j++ { // 让 下标 j 从 0 开始计数
		mx.M[begin+size-1][begin+j] = num // 把 num 写入 mx.M[begin+size-1][begin+j]
		num++                             // num 加一
	}
	for j := size - 1; j > 0; j-- { // 把 大小 减 1; 下标 j 超过 0; 下标 j 减一 { 写入 for j :
		mx.M[begin+j][begin+size-1] = num // 把 num 写入 mx.M[begin+j][begin+size-1]
		num++                             // num 加一
	}
	for j := size - 1; j > 0; j-- { // 把 大小 减 1; 下标 j 超过 0; 下标 j 减一 { 写入 for j :
		mx.M[begin][begin+j] = num // 把 num 写入 mx.M[begin][begin+j]
		num++                      // num 加一
	}
	return mx.fill(num, begin+1, size-2) // 返回 mx.fill(num, begin 加 1, 大小 减 2)
}

func (mx *Matrix) clear() { // 定义函数/方法 clear
	mx.M = make([][]int, mx.N) // 把 make([][]int, mx.N) 写入 mx.M
	for i := range mx.M {      // 把 range mx.M { 写入 for i :
		mx.M[i] = make([]int, mx.N) // 把 make([]int, mx.N) 写入 mx.M[i]
	}
}

func eqMat(a, b [][]int) bool { // 定义函数/方法 eqMat
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if len(a[i]) != len(b[i]) { // 定义函数/方法 len
			return false // 返回 false
		}
		for j := range a[i] { // 把 range 数组[下标 i] { 写入 for j :
			if a[i][j] != b[i][j] { // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]
				return false // 返回 false
			}
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	want6 := [][]int{ // 把 [][]int{ 写入 want6 :
		{1, 20, 19, 18, 17, 16},
		{2, 21, 32, 31, 30, 15},
		{3, 22, 33, 36, 29, 14},
		{4, 23, 34, 35, 28, 13},
		{5, 24, 25, 26, 27, 12},
		{6, 7, 8, 9, 10, 11},
	}
	ok := true // 把 true 写入 ok :

	// 正常用例：6x6 逆时针螺旋填充
	obj := NewMatrix(6)       // 把 NewMatrix(6) 写入 obj :
	obj.fill(1, 0, 6)         // obj.fill(1, 0, 6)
	if !eqMat(obj.M, want6) { // 若 取反 eqMat(obj.M, want6
		ok = false                                                // 把 false 写入 ok
		fmt.Printf("FAIL Matrix.fill=%v want %v\n", obj.M, want6) // 打印输出
	}

	// clear 后全部归零
	obj.clear()                 // obj.clear()
	for _, row := range obj.M { // 同时取 _ 与 row 遍历
		for _, v := range row { // 同时取 _ 与 值 遍历
			if v != 0 { // 若 值 不等于 0
				ok = false                                             // 把 false 写入 ok
				fmt.Println("FAIL Matrix.clear did not reset to zero") // 打印输出
			}
		}
	}

	// 边界用例：1x1
	one := NewMatrix(1)              // 把 NewMatrix(1) 写入 one :
	one.fill(1, 0, 1)                // one.fill(1, 0, 1)
	if !eqMat(one.M, [][]int{{1}}) { // 若 取反 eqMat(one.M, [][]int{{1}}
		ok = false                                               // 把 false 写入 ok
		fmt.Printf("FAIL Matrix(1).fill=%v want [[1]]\n", one.M) // 打印输出
	}

	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

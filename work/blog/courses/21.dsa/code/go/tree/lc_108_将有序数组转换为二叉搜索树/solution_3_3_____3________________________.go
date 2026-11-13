// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144993168
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode { // 定义函数/方法 sortedArrayToBST
	var helper func(left, right int) *TreeNode // var helper func(左边界, 右边界 int) 乘 TreeNode
	helper = func(left, right int) *TreeNode { // 把 func(左边界, 右边界 int) 乘 TreeNode { 写入 helper
		if left > right { // 若 左边界 超过 右边界
			return nil // 返回 nil
		}
		mid := (left + right) / 2         // 把 (左边界 加 右边界) 除以 2 写入 mid :
		root := &TreeNode{Val: nums[mid]} // 把 按位与 TreeNode{Val: 数组[中点]} 写入 root :
		root.Left = helper(left, mid-1)   // 把 helper(左边界, 中点 减 1) 写入 root.Left
		root.Right = helper(mid+1, right) // 把 helper(中点 加 1, 右边界) 写入 root.Right
		return root                       // 返回 根节点
	}
	return helper(0, len(nums)-1) // 定义函数/方法 helper
}

func inorder(root *TreeNode) []int { // 定义函数/方法 inorder
	if root == nil { // 若 根节点 等于 nil
		return []int{} // 返回 []int{}
	}
	res := []int{}                            // 把 []int{} 写入 res :
	res = append(res, inorder(root.Left)...)  // 把 append(结果, inorder(根节点.Left)...) 写入 结果
	res = append(res, root.Val)               // 把 append(结果, 根节点.Val) 写入 结果
	res = append(res, inorder(root.Right)...) // 把 append(结果, inorder(根节点.Right)...) 写入 结果
	return res                                // 返回 结果
}

type tc struct { // 定义类型
	nums []int // 数组 []int
	want []int // want []int
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{}, []int{}},
		{[]int{1}, []int{1}},
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{1, 2, 3, 4, 5}, []int{1, 2, 3, 4, 5}},
	}
	for idx, c := range cases { // 同时取 idx 与 字符 遍历
		got := inorder(sortedArrayToBST(c.nums)) // 把 inorder(sortedArrayToBST(字符.数组)) 写入 got :
		if !reflect.DeepEqual(got, c.want) {     // 若 取反 reflect.DeepEqual(got, 字符.want
			fmt.Printf("case %d failed: got %v want %v\n", idx, got, c.want) // 打印输出
			os.Exit(1)                                                       // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

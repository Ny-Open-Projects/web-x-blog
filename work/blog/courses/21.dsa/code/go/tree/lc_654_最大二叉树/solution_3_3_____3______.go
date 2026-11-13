// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode { // 定义函数/方法 constructMaximumBinaryTree
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return nil // 返回 nil
	}
	tree := make([]*TreeNode, n) // 把 make([] 乘 TreeNode, 元素个数) 写入 tree :
	for i := 0; i < n; i++ {     // 让 下标 i 从 0 开始计数
		tree[i] = &TreeNode{Val: nums[i]} // 把 按位与 TreeNode{Val: 数组[下标 i]} 写入 tree[i]
	}
	stack := []int{}         // 把 []int{} 写入 stack :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for len(stack) > 0 && nums[i] > nums[stack[len(stack)-1]] { // for 长度(栈) 超过 0 且 数组[下标 i] 超过 数组[栈[长度(栈) 减 1]] {
			tree[i].Left = tree[stack[len(stack)-1]] // 把 tree[栈[长度(栈) 减 1]] 写入 tree[i].Left
			stack = stack[:len(stack)-1]             // 把 栈[:长度(栈) 减 1] 写入 栈
		}
		if len(stack) > 0 { // 若 长度(栈) 超过 0
			tree[stack[len(stack)-1]].Right = tree[i] // 把 tree[下标 i] 写入 tree[stack[len(stack)-1]].Right
		}
		stack = append(stack, i) // 把 append(栈, 下标 i) 写入 栈
	}
	return tree[stack[0]] // 返回 tree[栈[0]]
}

func main() { // 程序入口：跑内嵌自测用例
	root := constructMaximumBinaryTree([]int{3, 2, 1, 6, 0, 5})
	if root == nil || root.Val != 6 { // 若 根节点 等于 nil 或 根节点.Val 不等于 6
		fmt.Printf("FAIL root.Val=%v want=6\n", root) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

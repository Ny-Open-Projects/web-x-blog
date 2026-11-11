// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347892
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type dllNode struct { // 定义类型
	val  int      // 值 int
	prev *dllNode // 前一个 乘 dllNode
	next *dllNode // 下一个 乘 dllNode
}

type MyLinkedList struct { // 定义类型
	head *dllNode // 头节点 乘 dllNode
	tail *dllNode // 尾节点 乘 dllNode
	size int      // 大小 int
}

func NewMyLinkedList() *MyLinkedList { // 定义函数/方法 NewMyLinkedList
	return &MyLinkedList{} // 返回 按位与 MyLinkedList{}
}

func (l *MyLinkedList) get(index int) int { // 定义函数/方法 get
	if index < 0 || index >= l.size { // 若 index 小于 0 或 index 不低于 左指针.大小
		return -1 // 返回 减 1
	}
	curr := l.head               // 把 左指针.头节点 写入 curr :
	for i := 0; i < index; i++ { // 让 下标 i 从 0 开始计数
		curr = curr.next // 把 当前值.下一个 写入 当前值
	}
	return curr.val // 返回 当前值.值
}

func (l *MyLinkedList) addAtHead(val int) { // 定义函数/方法 addAtHead
	newNode := &dllNode{val: val} // 把 按位与 dllNode{值: 值} 写入 newNode :
	newNode.next = l.head         // 把 左指针.头节点 写入 下一个
	if l.head != nil {            // 若 左指针.头节点 不等于 nil
		l.head.prev = newNode // 把 newNode 写入 前一个
	} else { // 否则
		l.tail = newNode // 把 newNode 写入 尾节点
	}
	l.head = newNode // 把 newNode 写入 头节点
	l.size++         // 左指针.大小 加一
}

func (l *MyLinkedList) addAtTail(val int) { // 定义函数/方法 addAtTail
	newNode := &dllNode{val: val} // 把 按位与 dllNode{值: 值} 写入 newNode :
	if l.tail != nil {            // 若 左指针.尾节点 不等于 nil
		l.tail.next = newNode // 把 newNode 写入 下一个
		newNode.prev = l.tail // 把 左指针.尾节点 写入 前一个
	} else { // 否则
		l.head = newNode // 把 newNode 写入 头节点
	}
	l.tail = newNode // 把 newNode 写入 尾节点
	l.size++         // 左指针.大小 加一
}

func (l *MyLinkedList) addAtIndex(index, val int) { // 定义函数/方法 addAtIndex
	if index < 0 || index > l.size { // 若 index 小于 0 或 index 超过 左指针.大小
		return // return
	}
	if index == 0 { // 若 index 等于 0
		l.addAtHead(val) // 左指针.addAtHead(值)
	} else if index == l.size { // 否则，若 index 等于 左指针.大小
		l.addAtTail(val) // 左指针.addAtTail(值)
	} else { // 否则
		curr := l.head               // 把 左指针.头节点 写入 curr :
		for i := 0; i < index; i++ { // 让 下标 i 从 0 开始计数
			curr = curr.next // 把 当前值.下一个 写入 当前值
		}
		newNode := &dllNode{val: val} // 把 按位与 dllNode{值: 值} 写入 newNode :
		newNode.prev = curr.prev      // 把 当前值.前一个 写入 前一个
		newNode.next = curr           // 把 当前值 写入 下一个
		curr.prev.next = newNode      // 把 newNode 写入 下一个
		curr.prev = newNode           // 把 newNode 写入 前一个
		l.size++                      // 左指针.大小 加一
	}
}

func (l *MyLinkedList) deleteAtIndex(index int) { // 定义函数/方法 deleteAtIndex
	if index < 0 || index >= l.size { // 若 index 小于 0 或 index 不低于 左指针.大小
		return // return
	}
	var curr *dllNode // var 当前值 乘 dllNode
	if index == 0 {   // 若 index 等于 0
		curr = l.head        // 把 左指针.头节点 写入 当前值
		l.head = l.head.next // 把 左指针.头节点.下一个 写入 头节点
		if l.head != nil {   // 若 左指针.头节点 不等于 nil
			l.head.prev = nil // 把 nil 写入 前一个
		} else { // 否则
			l.tail = nil // 把 nil 写入 尾节点
		}
	} else if index == l.size-1 { // 否则，若 index 等于 左指针.大小 减 1
		curr = l.tail        // 把 左指针.尾节点 写入 当前值
		l.tail = l.tail.prev // 把 左指针.尾节点.前一个 写入 尾节点
		if l.tail != nil {   // 若 左指针.尾节点 不等于 nil
			l.tail.next = nil // 把 nil 写入 下一个
		} else { // 否则
			l.head = nil // 把 nil 写入 头节点
		}
	} else { // 否则
		curr = l.head                // 把 左指针.头节点 写入 当前值
		for i := 0; i < index; i++ { // 让 下标 i 从 0 开始计数
			curr = curr.next // 把 当前值.下一个 写入 当前值
		}
		curr.prev.next = curr.next // 把 当前值.下一个 写入 下一个
		curr.next.prev = curr.prev // 把 当前值.前一个 写入 前一个
	}
	l.size-- // 左指针.大小 减一
}

func main() { // 程序入口：跑内嵌自测用例
	obj := NewMyLinkedList()                         // 把 NewMyLinkedList() 写入 obj :
	obj.addAtHead(1)                                 // obj.addAtHead(1)
	obj.addAtTail(3)                                 // obj.addAtTail(3)
	obj.addAtIndex(1, 2)                             // obj.addAtIndex(1, 2)
	got := []int{obj.get(1), obj.get(0), obj.get(2)} // 把 []int{obj 查找 1), obj 查找 0), obj 查找 2)} 写入 got :
	obj.deleteAtIndex(1)                             // obj.deleteAtIndex(1)
	got = append(got, obj.get(1))                    // 把 append(got, obj 查找 1)) 写入 got
	want := []int{2, 1, 3, 3}                        // 把 []int{2, 1, 3, 3} 写入 want :
	if !reflect.DeepEqual(got, want) {               // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL MyLinkedList %v want %v\n", got, want) // 打印输出
		os.Exit(1)                                              // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}

-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145361774
-- LeetCode 641. 设计循环双端队列 — Lua 版（方案1）
local MyCircularDeque = {} -- 把 {} 写入 local MyCircularDeque
MyCircularDeque.__index = MyCircularDeque -- 把 MyCircularDeque 写入 MyCircularDeque.__index
function MyCircularDeque.new(k) -- function MyCircularDeque.new(下标 k)
	return setmetatable({ data = {}, head = 1, tail = 1, cap = k, size = 0 }, MyCircularDeque)
end -- 终点
function MyCircularDeque:insertFront(v) -- function MyCircularDeque:insertFront(值)
	if self.size == self.cap then
		return false
	end -- 若 self.大小 等于 self.cap then return false 终点
	self.head = (self.head - 2) % self.cap + 1 -- 把 (self.头节点 减 2) 对…取模 self.cap 加 1 写入 头节点
	self.data[self.head] = v -- 把 值 写入 self.data[self.head]
	self.size = self.size + 1 -- 把 self.大小 加 1 写入 大小
	return true -- 返回 true
end -- 终点
function MyCircularDeque:insertLast(v) -- function MyCircularDeque:insertLast(值)
	if self.size == self.cap then
		return false
	end -- 若 self.大小 等于 self.cap then return false 终点
	self.data[self.tail] = v -- 把 值 写入 self.data[self.tail]
	self.tail = self.tail % self.cap + 1 -- 把 self.尾节点 对…取模 self.cap 加 1 写入 尾节点
	self.size = self.size + 1 -- 把 self.大小 加 1 写入 大小
	return true -- 返回 true
end -- 终点
function MyCircularDeque:deleteFront() -- function MyCircularDeque:deleteFront()
	if self.size == 0 then
		return false
	end -- 若 self.大小 等于 0 then return false 终点
	self.head = self.head % self.cap + 1 -- 把 self.头节点 对…取模 self.cap 加 1 写入 头节点
	self.size = self.size - 1 -- 把 self.大小 减 1 写入 大小
	return true -- 返回 true
end -- 终点
function MyCircularDeque:deleteLast() -- function MyCircularDeque:deleteLast()
	if self.size == 0 then
		return false
	end -- 若 self.大小 等于 0 then return false 终点
	self.tail = (self.tail - 2) % self.cap + 1 -- 把 (self.尾节点 减 2) 对…取模 self.cap 加 1 写入 尾节点
	self.size = self.size - 1 -- 把 self.大小 减 1 写入 大小
	return true -- 返回 true
end -- 终点
function MyCircularDeque:getFront()
	if self.size == 0 then
		return -1
	end
	return self.data[self.head]
end
function MyCircularDeque:getRear()
	if self.size == 0 then
		return -1
	end
	return self.data[(self.tail - 2) % self.cap + 1]
end
function MyCircularDeque:isEmpty()
	return self.size == 0
end -- 把 赋值为 0 终点 写入 大小
function MyCircularDeque:isFull()
	return self.size == self.cap
end -- 把 赋值为 self.cap 终点 写入 大小
local d = MyCircularDeque.new(3) -- 把 MyCircularDeque.new(3) 写入 local d
assert(d:insertLast(1) == true) -- 断言校验
assert(d:insertLast(2) == true) -- 断言校验
assert(d:insertFront(3) == true) -- 断言校验
assert(d:insertFront(4) == false) -- 断言校验
assert(d:getRear() == 2) -- 断言校验
assert(d:isFull() == true) -- 断言校验
assert(d:deleteLast() == true) -- 断言校验
assert(d:insertFront(4) == true) -- 断言校验
assert(d:getFront() == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

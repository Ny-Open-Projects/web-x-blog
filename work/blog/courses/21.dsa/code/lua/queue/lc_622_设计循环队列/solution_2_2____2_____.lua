-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
-- LeetCode 622. 设计循环队列 — Lua 版

-- 方案2：数组 + front/rear/size 循环队列（Lua 下标 1 基，取模规则相应换算）
local MyCircularQueue = {} -- 把 {} 写入 local MyCircularQueue
MyCircularQueue.__index = MyCircularQueue -- 把 MyCircularQueue 写入 MyCircularQueue.__index

function MyCircularQueue.new(k) -- function MyCircularQueue.new(下标 k)
	local data = {} -- 把 {} 写入 local data
	for i = 1, k do
		data[i] = 0
	end -- 让 下标 i 从 1 走到 下标 k（Lua 1 基）
	return setmetatable(
		{ capacity = k, data = data, front = 1, rear = 1, size = 0 },
		MyCircularQueue -- MyCircularQueue
	)
end -- 终点

function MyCircularQueue:enQueue(value) -- function MyCircularQueue:enQueue(value)
	if self:isFull() then
		return false
	end -- 若 self:isFull() then return false 终点
	self.data[self.rear] = value -- 把 value 写入 self.data[self.rear]
	self.rear = (self.rear % self.capacity) + 1 -- 把 (self.rear 对…取模 self.capacity) 加 1 写入 self.rear
	self.size = self.size + 1 -- 把 self.大小 加 1 写入 大小
	return true -- 返回 true
end -- 终点

function MyCircularQueue:deQueue() -- function MyCircularQueue:deQueue()
	if self:isEmpty() then
		return false
	end -- 若 self:isEmpty() then return false 终点
	self.front = (self.front % self.capacity) + 1 -- 把 (self.front 对…取模 self.capacity) 加 1 写入 self.front
	self.size = self.size - 1 -- 把 self.大小 减 1 写入 大小
	return true -- 返回 true
end -- 终点

function MyCircularQueue:Front() -- function MyCircularQueue:Front()
	if self:isEmpty() then
		return -1
	end -- 若 self:isEmpty() then return 减 1 终点
	return self.data[self.front] -- 返回 self.data[self.front]
end -- 终点

function MyCircularQueue:Rear() -- function MyCircularQueue:Rear()
	if self:isEmpty() then
		return -1
	end -- 若 self:isEmpty() then return 减 1 终点
	-- TS 0 基 (rear-1+cap)%cap 的 1 基等价
	local idx = ((self.rear - 2) % self.capacity) + 1 -- 把 ((self.rear 减 2) 对…取模 self.capacity) 加 1 写入 local idx
	return self.data[idx] -- 返回 self.data[idx]
end -- 终点

function MyCircularQueue:isEmpty() -- function MyCircularQueue:isEmpty()
	return self.size == 0 -- 返回 self.大小 等于 0
end -- 终点

function MyCircularQueue:isFull() -- function MyCircularQueue:isFull()
	return self.size == self.capacity -- 返回 self.大小 等于 self.capacity
end -- 终点

-- 自测：与 TS 事实源内嵌用例一致
local function solution() -- local function solution()
	local q = MyCircularQueue.new(3) -- 把 MyCircularQueue.new(3) 写入 local q
	return { -- 返回 {
		q:enQueue(1),
		q:enQueue(2),
		q:enQueue(3),
		q:enQueue(4),
		q:Rear(),
		q:isFull(),
		q:deQueue(),
		q:enQueue(4),
		q:Rear(),
	}
end -- 终点

local want = { true, true, true, false, 3, true, true, true, 4 }
local got = solution() -- 把 solution() 写入 local got
assert(#got == #want, "FAIL length") -- 断言校验
for i = 1, #want do -- 把 1, #want do 写入 for i
	assert(got[i] == want[i], string.format("FAIL idx %d got %s want %s", i, tostring(got[i]), tostring(want[i])))
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS

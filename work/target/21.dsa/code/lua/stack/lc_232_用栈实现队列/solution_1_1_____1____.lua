-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
-- LeetCode 232. 用栈实现队列 — Lua 版（方案1）
local MyQueue = {} -- 把 {} 写入 local MyQueue
MyQueue.__index = MyQueue -- 把 MyQueue 写入 MyQueue.__index
function MyQueue.new()
	return setmetatable({ in_ = {}, out_ = {} }, MyQueue)
end
function MyQueue:in2out() -- function MyQueue:in2out()
	while #self.in_ > 0 do -- while #self.in_ 超过 0 do
		self.out_[#self.out_ + 1] = table.remove(self.in_) -- 把 table 弹出 self.in_) 写入 self.out_[#self.out_ + 1]
	end -- 终点
end -- 终点
function MyQueue:push(x)
	self.in_[#self.in_ + 1] = x
end -- 把 x 终点 写入 function MyQueue:push(x) self.in_[#self.in_ + 1]
function MyQueue:pop() -- function MyQueue:pop()
	if #self.out_ == 0 then
		self:in2out()
	end -- 若 #self.out_ 等于 0 then self:in2out() 终点
	return table.remove(self.out_) -- 返回 table 弹出 self.out_)
end -- 终点
function MyQueue:peek() -- function MyQueue:peek()
	if #self.out_ == 0 then
		self:in2out()
	end -- 若 #self.out_ 等于 0 then self:in2out() 终点
	return self.out_[#self.out_] -- 返回 self.out_[#self.out_]
end -- 终点
function MyQueue:empty()
	return #self.in_ == 0 and #self.out_ == 0
end
local mq = MyQueue.new() -- 把 MyQueue.new() 写入 local mq
mq:push(1)
mq:push(2) -- mq:push(1); mq:push(2)
assert(mq:peek() == 1) -- 断言校验
assert(mq:pop() == 1) -- 断言校验
assert(mq:empty() == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

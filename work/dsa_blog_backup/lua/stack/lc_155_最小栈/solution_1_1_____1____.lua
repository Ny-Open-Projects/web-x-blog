-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
-- LeetCode 155. 最小栈 — Lua 版（方案1）
local MinStack = {} -- 把 {} 写入 local MinStack
MinStack.__index = MinStack -- 把 MinStack 写入 MinStack.__index
function MinStack.new()
	return setmetatable({ vals = {}, mins = {} }, MinStack)
end
function MinStack:push(v) -- function MinStack:push(值)
	self.vals[#self.vals + 1] = v -- 把 值 写入 self.vals[#self.vals + 1]
	local m = #self.mins > 0 and math.min(self.mins[#self.mins], v) or v
	self.mins[#self.mins + 1] = m -- 把 映射表 写入 self.mins[#self.mins + 1]
end -- 终点
function MinStack:pop()
	self.vals[#self.vals] = nil
	self.mins[#self.mins] = nil
end
function MinStack:top()
	return self.vals[#self.vals]
end -- function MinStack:top() return self.vals[#self.vals] 终点
function MinStack:getMin()
	return self.mins[#self.mins]
end -- function MinStack:getMin() return self.mins[#self.mins] 终点
local ms = MinStack.new() -- 把 MinStack.new() 写入 local ms
ms:push(-2)
ms:push(0)
ms:push(-3) -- ms:push( 减 2); ms:push(0); ms:push( 减 3)
assert(ms:getMin() == -3) -- 断言校验
ms:pop() -- ms:pop()
assert(ms:top() == 0) -- 断言校验
assert(ms:getMin() == -2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

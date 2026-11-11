-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145198996
-- LeetCode 225. 用队列实现栈 — Lua 版（方案1）
local MyStack = {} -- 把 {} 写入 local MyStack
MyStack.__index = MyStack -- 把 MyStack 写入 MyStack.__index
function MyStack.new()
	return setmetatable({ q = {} }, MyStack)
end
function MyStack:push(x)
	table.insert(self.q, 1, x)
end -- function MyStack:push(x) table 插入 self.节点, 1, x) 终点
function MyStack:pop()
	return table.remove(self.q, 1)
end -- function MyStack:pop() return table 弹出 self.节点, 1) 终点
function MyStack:top()
	return self.q[1]
end -- function MyStack:top() return self.节点[1] 终点
function MyStack:empty()
	return #self.q == 0
end -- 把 赋值为 0 终点 写入 节点
local ms = MyStack.new() -- 把 MyStack.new() 写入 local ms
ms:push(1)
ms:push(2) -- ms:push(1); ms:push(2)
assert(ms:top() == 2) -- 断言校验
assert(ms:pop() == 2) -- 断言校验
assert(ms:empty() == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

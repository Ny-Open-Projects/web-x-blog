-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案11：Rule 循环游标）
local Rule = {} -- 把 {} 写入 local Rule
Rule.__index = Rule -- 把 Rule 写入 Rule.__index
function Rule.new(r) -- function Rule.new(右指针)
	return setmetatable({ data = r, idx = 1, len = #r }, Rule)
end -- 终点
function Rule:next() -- function Rule:下一个()
	local ch = self.data:sub(self.idx, self.idx) -- 把 self.data:sub(self.idx, self.idx) 写入 local ch
	self.idx = (self.idx - 1 + 1) % self.len + 1 -- 把 (self.idx 减 1 加 1) 对…取模 self.长度 加 1 写入 self.idx
	return ch -- 返回 字符
end -- 终点
function Rule:peek() -- function Rule:peek()
	return self.data:sub(self.idx, self.idx) -- 返回 self.data:sub(self.idx, self.idx)
end -- 终点

local r = Rule.new("ESVM") -- 把 Rule.new(「ESVM」) 写入 local r
local s1 = {} -- 把 {} 写入 local s1
for _ = 1, 10 do
	s1[#s1 + 1] = r:next()
end -- 让 _ 从 1 走到 10（Lua 1 基）
local r2 = Rule.new("semv") -- 把 Rule.new(「semv」) 写入 local r2
local s2 = {} -- 把 {} 写入 local s2
for _ = 1, 6 do
	s2[#s2 + 1] = r2:next()
end -- 让 _ 从 1 走到 6（Lua 1 基）
assert(table.concat(s1) == "ESVMESVMES", "rule1") -- 打印输出
assert(table.concat(s2) == "semvse", "rule2") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS

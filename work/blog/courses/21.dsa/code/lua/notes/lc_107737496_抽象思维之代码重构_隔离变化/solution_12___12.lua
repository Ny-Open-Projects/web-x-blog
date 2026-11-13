-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案12：Location/Rule/Filler 组合）
local Rule = {} -- 把 {} 写入 local Rule
Rule.__index = Rule -- 把 Rule 写入 Rule.__index
function Rule.new(r) -- function Rule.new(右指针)
	return setmetatable({ data = r, idx = 1, len = #r }, Rule)
end -- 终点
function Rule:current()
	return self.data:sub(self.idx, self.idx)
end
function Rule:advance()
	self.idx = (self.idx - 1 + 1) % self.len + 1
end

local Filler = {} -- 把 {} 写入 local Filler
Filler.__index = Filler -- 把 Filler 写入 Filler.__index
function Filler.new(rn, cn, rule) -- function Filler.new(rn, cn, rule)
	local f = setmetatable({}, Filler) -- 把 setmetatable({}, Filler) 写入 local f
	f.pos = { 0, 0 } -- 把 { 0, 0 } 写入 f.pos
	f.rMin = 0 -- 把 0 写入 f.rMin
	f.cMin = 0 -- 把 0 写入 f.cMin
	f.rMax = rn - 1 -- 把 rn 减 1 写入 f.rMax
	f.cMax = cn - 1 -- 把 cn 减 1 写入 f.cMax
	f.cmd = Rule.new(rule) -- 把 Rule.new(rule) 写入 f.cmd
	return f -- 返回 f
end -- 终点
function Filler:next() -- function Filler:下一个()
	local res = { self.pos[1], self.pos[2] } -- 把 { self.pos[1], self.pos[2] } 写入 local res
	local ch = self.cmd:current() -- 把 self.cmd:current() 写入 local ch
	if ch == "E" then -- 若 字符 等于 「E」 then
		self.pos[1] = self.pos[1] + 1 -- 把 self.pos[1] 加 1 写入 self.pos[1]
		if self.pos[1] == self.rMax then
			self.cmd:advance()
			self.cMin = self.cMin + 1
		end
	elseif ch == "S" then -- 把 赋值为 「S」 then 写入 elseif ch
		self.pos[2] = self.pos[2] + 1 -- 把 self.pos[2] 加 1 写入 self.pos[2]
		if self.pos[2] == self.cMax then
			self.cmd:advance()
			self.rMax = self.rMax - 1
		end
	elseif ch == "V" then -- 把 赋值为 「V」 then 写入 elseif ch
		self.pos[1] = self.pos[1] - 1 -- 把 self.pos[1] 减 1 写入 self.pos[1]
		if self.pos[1] == self.rMin then
			self.cmd:advance()
			self.cMax = self.cMax - 1
		end
	elseif ch == "M" then -- 把 赋值为 「M」 then 写入 elseif ch
		self.pos[2] = self.pos[2] - 1 -- 把 self.pos[2] 减 1 写入 self.pos[2]
		if self.pos[2] == self.cMin then
			self.cmd:advance()
			self.rMin = self.rMin + 1
		end
	end -- 终点
	return res[1], res[2] -- 返回 结果[1], 结果[2]
end -- 终点

local function test_filler(rule, rn, cn) -- local function test_filler(rule, rn, cn)
	local obj = Filler.new(rn, cn, rule) -- 把 Filler.new(rn, cn, rule) 写入 local obj
	local seq = {} -- 把 {} 写入 local seq
	for _ = 1, rn * cn do -- 让 _ 从 1 走到 rn（Lua 1 基）
		local r, c = obj:next() -- 把 obj:下一个() 写入 local r, c
		seq[#seq + 1] = { r, c } -- 把 { 右指针, 字符 } 写入 seq[#seq + 1]
	end -- 终点
	return seq -- 返回 seq
end -- 终点

local got = test_filler("ESVM", 4, 4) -- 把 test_filler(「ESVM」, 4, 4) 写入 local got
local want = {
	{ 0, 0 },
	{ 1, 0 },
	{ 2, 0 },
	{ 3, 0 },
	{ 3, 1 },
	{ 3, 2 },
	{ 3, 3 },
	{ 2, 3 },
	{ 1, 3 },
	{ 0, 3 },
	{ 0, 2 },
	{
		0,
		1,
	},
	{
		1,
		1,
	},
	{
		2,
		1,
	},
	{
		2,
		2,
	},
	{
		1,
		2,
	},
}
for i = 1, 16 do -- 让 下标 i 从 1 走到 16（Lua 1 基）
	assert(got[i][1] == want[i][1] and got[i][2] == want[i][2], "filler4 at " .. i) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS

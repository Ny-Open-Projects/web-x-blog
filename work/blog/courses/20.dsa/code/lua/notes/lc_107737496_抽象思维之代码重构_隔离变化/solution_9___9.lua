-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案9：规则串状态机，8 方向字母）
local Filler = {} -- 把 {} 写入 local Filler
Filler.__index = Filler -- 把 Filler 写入 Filler.__index
function Filler.new(rn, cn) -- function Filler.new(rn, cn)
	local f = setmetatable({ rowNum = rn, colNum = cn, rule = "ESVM" }, Filler)
	f.pos = { 0, 0 } -- 把 { 0, 0 } 写入 f.pos
	f.idx = 0 -- 把 0 写入 f.idx
	f.rMin = 0 -- 把 0 写入 f.rMin
	f.cMin = 0 -- 把 0 写入 f.cMin
	f.rMax = rn - 1 -- 把 rn 减 1 写入 f.rMax
	f.cMax = cn - 1 -- 把 cn 减 1 写入 f.cMax
	return f -- 返回 f
end -- 终点
function Filler:setRule(rule)
	self.rule = rule
end -- 把 rule 终点 写入 function Filler:setRule(rule) self.rule
function Filler:next() -- function Filler:下一个()
	local res = { self.pos[1], self.pos[2] } -- 把 { self.pos[1], self.pos[2] } 写入 local res
	local ch = self.rule:sub(self.idx % #self.rule + 1, self.idx % #self.rule + 1)
	if ch == "E" then -- 若 字符 等于 「E」 then
		self.pos[1] = self.pos[1] + 1 -- 把 self.pos[1] 加 1 写入 self.pos[1]
		if self.pos[1] == self.rMax then
			self.idx = self.idx + 1
			self.cMin = self.cMin + 1
		end
	elseif ch == "S" then -- 把 赋值为 「S」 then 写入 elseif ch
		self.pos[2] = self.pos[2] + 1 -- 把 self.pos[2] 加 1 写入 self.pos[2]
		if self.pos[2] == self.cMax then
			self.idx = self.idx + 1
			self.rMax = self.rMax - 1
		end
	elseif ch == "V" then -- 把 赋值为 「V」 then 写入 elseif ch
		self.pos[1] = self.pos[1] - 1 -- 把 self.pos[1] 减 1 写入 self.pos[1]
		if self.pos[1] == self.rMin then
			self.idx = self.idx + 1
			self.cMax = self.cMax - 1
		end
	elseif ch == "M" then -- 把 赋值为 「M」 then 写入 elseif ch
		self.pos[2] = self.pos[2] - 1 -- 把 self.pos[2] 减 1 写入 self.pos[2]
		if self.pos[2] == self.cMin then
			self.idx = self.idx + 1
			self.rMin = self.rMin + 1
		end
	elseif ch == "e" then -- 把 赋值为 「e」 then 写入 elseif ch
		self.pos[1] = self.pos[1] + 1 -- 把 self.pos[1] 加 1 写入 self.pos[1]
		if self.pos[1] == self.rMax then
			self.idx = self.idx + 1
			self.cMax = self.cMax - 1
		end
	elseif ch == "s" then -- 把 赋值为 「字符串」 then 写入 elseif ch
		self.pos[2] = self.pos[2] + 1 -- 把 self.pos[2] 加 1 写入 self.pos[2]
		if self.pos[2] == self.cMax then
			self.idx = self.idx + 1
			self.rMin = self.rMin + 1
		end
	elseif ch == "v" then -- 把 赋值为 「值」 then 写入 elseif ch
		self.pos[1] = self.pos[1] - 1 -- 把 self.pos[1] 减 1 写入 self.pos[1]
		if self.pos[1] == self.rMin then
			self.idx = self.idx + 1
			self.cMin = self.cMin + 1
		end
	elseif ch == "m" then -- 把 赋值为 「映射表」 then 写入 elseif ch
		self.pos[2] = self.pos[2] - 1 -- 把 self.pos[2] 减 1 写入 self.pos[2]
		if self.pos[2] == self.cMin then
			self.idx = self.idx + 1
			self.rMax = self.rMax - 1
		end
	end -- 终点
	return res[1], res[2] -- 返回 结果[1], 结果[2]
end -- 终点

local function test_filler(rule, rn, cn) -- local function test_filler(rule, rn, cn)
	local obj = Filler.new(rn, cn) -- 把 Filler.new(rn, cn) 写入 local obj
	obj:setRule(rule) -- obj:setRule(rule)
	local seq = {} -- 把 {} 写入 local seq
	for _ = 1, rn * cn do -- 让 _ 从 1 走到 rn（Lua 1 基）
		local r, c = obj:next() -- 把 obj:下一个() 写入 local r, c
		seq[#seq + 1] = { r, c } -- 把 { 右指针, 字符 } 写入 seq[#seq + 1]
	end -- 终点
	return seq -- 返回 seq
end -- 终点

local function check_seq(got, want, tag) -- local function check_seq(got, want, tag)
	assert(#got == #want, tag .. " length") -- 断言校验
	for i = 1, #want do -- 把 1, #want do 写入 for i
		assert(got[i][1] == want[i][1] and got[i][2] == want[i][2], tag .. " at " .. i) -- 断言校验
	end -- 终点
end -- 终点

check_seq(test_filler("ESVM", 4, 4), {
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
}, "ESVM")
check_seq(test_filler("semv", 4, 4), {
	{ 0, 0 },
	{ 0, 1 },
	{ 0, 2 },
	{ 0, 3 },
	{ 1, 3 },
	{ 2, 3 },
	{ 3, 3 },
	{ 3, 2 },
	{ 3, 1 },
	{ 3, 0 },
	{ 2, 0 },
	{
		1,
		0,
	},
	{
		1,
		1,
	},
	{
		1,
		2,
	},
	{
		2,
		2,
	},
	{
		2,
		1,
	},
}, "semv")
print("PASS") -- 全部用例通过，输出 PASS

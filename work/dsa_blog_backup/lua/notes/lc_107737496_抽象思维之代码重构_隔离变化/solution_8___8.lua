-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案8：Filler 状态机 + hasNext 部分填充）
local Filler = {} -- 把 {} 写入 local Filler
Filler.__index = Filler -- 把 Filler 写入 Filler.__index
function Filler.new(rn, cn) -- function Filler.new(rn, cn)
	local f = setmetatable({ rowNum = rn, colNum = cn, rule = "ESVM" }, Filler)
	f:reset() -- f:reset()
	return f -- 返回 f
end -- 终点
function Filler:reset() -- function Filler:reset()
	self.pos = { 0, 0 } -- 0 基
	self.idx = 0 -- 把 0 写入 self.idx
	self.rMin = 0 -- 把 0 写入 self.rMin
	self.cMin = 0 -- 把 0 写入 self.cMin
	self.rMax = self.rowNum - 1 -- 把 self.rowNum 减 1 写入 self.rMax
	self.cMax = self.colNum - 1 -- 把 self.colNum 减 1 写入 self.cMax
end -- 终点
function Filler:setRule(r)
	self.rule = r
end -- 把 右指针 终点 写入 function Filler:setRule(r) self.rule
function Filler:hasNext() -- function Filler:hasNext()
	return self.rMin <= self.pos[1]
		and self.pos[1] <= self.rMax -- 返回 self.rMin 不超过 self.pos[1] and self.pos[1] 不超过 self.rMax
		and self.cMin <= self.pos[2]
		and self.pos[2] <= self.cMax
end -- 终点
function Filler:next() -- function Filler:下一个()
	local r, c = self.pos[1], self.pos[2] -- 把 self.pos[1], self.pos[2] 写入 local r, c
	self:_advance() -- self:_advance()
	return r, c -- 返回 右指针, 字符
end -- 终点
function Filler:_advance() -- function Filler:_advance()
	local cmd = self.rule:sub(self.idx % 4 + 1, self.idx % 4 + 1)
	if cmd == "E" then -- 若 cmd 等于 「E」 then
		self.pos[1] = self.pos[1] + 1 -- 把 self.pos[1] 加 1 写入 self.pos[1]
		if self.pos[1] == self.rMax then
			self.idx = self.idx + 1
			self.cMin = self.cMin + 1
		end
	elseif cmd == "S" then -- 把 赋值为 「S」 then 写入 elseif cmd
		self.pos[2] = self.pos[2] + 1 -- 把 self.pos[2] 加 1 写入 self.pos[2]
		if self.pos[2] == self.cMax then
			self.idx = self.idx + 1
			self.rMax = self.rMax - 1
		end
	elseif cmd == "V" then -- 把 赋值为 「V」 then 写入 elseif cmd
		self.pos[1] = self.pos[1] - 1 -- 把 self.pos[1] 减 1 写入 self.pos[1]
		if self.pos[1] == self.rMin then
			self.idx = self.idx + 1
			self.cMax = self.cMax - 1
		end
	elseif cmd == "M" then -- 把 赋值为 「M」 then 写入 elseif cmd
		self.pos[2] = self.pos[2] - 1 -- 把 self.pos[2] 减 1 写入 self.pos[2]
		if self.pos[2] == self.cMin then
			self.idx = self.idx + 1
			self.rMin = self.rMin + 1
		end
	end -- 终点
end -- 终点

local function fill_matrix(rn, cn, rule) -- local function fill_matrix(rn, cn, rule)
	local mat = {} -- 把 {} 写入 local mat
	for i = 1, rn do -- 让 下标 i 从 1 走到 rn（Lua 1 基）
		mat[i] = {} -- 把 {} 写入 mat[i]
		for j = 1, cn do
			mat[i][j] = 0
		end -- 让 下标 j 从 1 走到 cn（Lua 1 基）
	end -- 终点
	local f = Filler.new(rn, cn) -- 把 Filler.new(rn, cn) 写入 local f
	f:setRule(rule) -- f:setRule(rule)
	local i = 1 -- 把 1 写入 local i
	while f:hasNext() do -- while f:hasNext() do
		local r, c = f:next() -- 把 f:下一个() 写入 local r, c
		mat[r + 1][c + 1] = i -- 把 下标 i 写入 mat[r + 1][c + 1]
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
	end -- 终点
	return mat -- 返回 mat
end -- 终点

local got1 = fill_matrix(6, 6, "ESVM") -- 把 fill_matrix(6, 6, 「ESVM」) 写入 local got1
local want1 = { -- 把 { 写入 local want1
	{ 1, 0, 0, 0, 0, 0 },
	{ 2, 0, 0, 0, 0, 0 },
	{ 3, 0, 0, 0, 0, 0 },
	{ 4, 0, 0, 0, 0, 0 },
	{ 5, 0, 0, 0, 0, 0 },
	{ 0, 0, 0, 0, 0, 0 },
}
for i = 1, 6 do
	for j = 1, 6 do
		assert(got1[i][j] == want1[i][j], "case1")
	end
end -- 让 下标 i 从 1 走到 6（Lua 1 基）
local got2 = fill_matrix(3, 3, "ESVM") -- 把 fill_matrix(3, 3, 「ESVM」) 写入 local got2
local want2 = { { 1, 0, 0 }, { 2, 0, 0 }, { 0, 0, 0 } } -- 把 {{1, 0, 0}, {2, 0, 0}, {0, 0, 0}} 写入 local want2
for i = 1, 3 do
	for j = 1, 3 do
		assert(got2[i][j] == want2[i][j], "case2")
	end
end -- 让 下标 i 从 1 走到 3（Lua 1 基）
print("PASS") -- 全部用例通过，输出 PASS

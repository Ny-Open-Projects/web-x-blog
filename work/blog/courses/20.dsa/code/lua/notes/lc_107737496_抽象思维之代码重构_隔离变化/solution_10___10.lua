-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案10：Filler+Matrix 组合 9x9 全螺旋）
local Filler = {} -- 把 {} 写入 local Filler
Filler.__index = Filler -- 把 Filler 写入 Filler.__index
function Filler.new(rn, cn) -- function Filler.new(rn, cn)
	local f = setmetatable({}, Filler) -- 把 setmetatable({}, Filler) 写入 local f
	f.pos = { 0, 0 } -- 把 { 0, 0 } 写入 f.pos
	f.idx = 0 -- 把 0 写入 f.idx
	f.rMin = 0 -- 把 0 写入 f.rMin
	f.cMin = 0 -- 把 0 写入 f.cMin
	f.rMax = rn - 1 -- 把 rn 减 1 写入 f.rMax
	f.cMax = cn - 1 -- 把 cn 减 1 写入 f.cMax
	return f -- 返回 f
end -- 终点
local RULE = "ESVM" -- 把 「ESVM」 写入 local RULE

function Filler:next() -- function Filler:下一个()
	local r, c = self.pos[1], self.pos[2] -- 把 self.pos[1], self.pos[2] 写入 local r, c
	local cmd = RULE:sub(self.idx % 4 + 1, self.idx % 4 + 1)
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
	return r, c -- 返回 右指针, 字符
end -- 终点

local function fmt_row(row) -- local function fmt_row(row)
	local parts = {} -- 把 {} 写入 local parts
	for i, x in ipairs(row) do
		parts[i] = string.format("%2d", x)
	end -- 遍历取 x
	return table.concat(parts, " ") -- 返回 table.concat(parts, 「 」)
end -- 终点

local rn, cn = 9, 9 -- 把 9, 9 写入 local rn, cn
local obj = Filler.new(rn, cn) -- 把 Filler.new(rn, cn) 写入 local obj
local m = {} -- 把 {} 写入 local m
for i = 1, rn do -- 让 下标 i 从 1 走到 rn（Lua 1 基）
	m[i] = {} -- 把 {} 写入 m[i]
	for j = 1, cn do
		m[i][j] = 0
	end -- 让 下标 j 从 1 走到 cn（Lua 1 基）
end -- 终点
for i = 1, rn * cn do -- 让 下标 i 从 1 走到 rn（Lua 1 基）
	local r, c = obj:next() -- 把 obj:下一个() 写入 local r, c
	m[r + 1][c + 1] = i -- 把 下标 i 写入 m[r + 1][c + 1]
end -- 终点
local want = { -- 把 { 写入 local want
	" 1 32 31 30 29 28 27 26 25",
	" 2 33 56 55 54 53 52 51 24",
	" 3 34 57 72 71 70 69 50 23",
	" 4 35 58 73 80 79 68 49 22",
	" 5 36 59 74 81 78 67 48 21",
	" 6 37 60 75 76 77 66 47 20",
	" 7 38 61 62 63 64 65 46 19",
	" 8 39 40 41 42 43 44 45 18",
	" 9 10 11 12 13 14 15 16 17",
}
for i = 1, rn do -- 让 下标 i 从 1 走到 rn（Lua 1 基）
	local got = fmt_row(m[i]) -- 把 fmt_row(映射表[下标 i]) 写入 local got
	assert(got == want[i], "matrix9 row " .. i) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS

-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案6：合成滑块数据 buildSynthetic）
local function build_synthetic(bg_len, gap_start, puzzle_len)
	local bg = {} -- 把 {} 写入 local bg
	for i = 1, bg_len do
		bg[i] = 10
	end -- 让 下标 i 从 1 走到 bg_len（Lua 1 基）
	for i = gap_start + 1, math.min(gap_start + puzzle_len, bg_len) do
		bg[i] = 200 -- 把 200 写入 bg[i]
	end -- 终点
	local puzzle = {} -- 把 {} 写入 local puzzle
	for i = 1, puzzle_len do -- 让 下标 i 从 1 走到 puzzle_len（Lua 1 基）
		puzzle[i] = bg[gap_start + i] -- 把 bg[gap_start 加 下标 i] 写入 puzzle[i]
	end -- 终点
	return bg, puzzle -- 返回 bg, puzzle
end -- 终点

local bg, puzzle = build_synthetic(8, 3, 4) -- 把 build_synthetic(8, 3, 4) 写入 local bg, puzzle
local want_bg = { 10, 10, 10, 200, 200, 200, 200, 10 } -- 把 {10, 10, 10, 200, 200, 200, 200, 10} 写入 local want_bg
for i = 1, 8 do
	assert(bg[i] == want_bg[i], "bg")
end -- 让 下标 i 从 1 走到 8（Lua 1 基）
local want_pz = { 200, 200, 200, 200 } -- 把 {200, 200, 200, 200} 写入 local want_pz
for i = 1, 4 do
	assert(puzzle[i] == want_pz[i], "puzzle")
end -- 让 下标 i 从 1 走到 4（Lua 1 基）
assert(#puzzle == 4, "puzzle length") -- 断言校验
assert(#bg == 8, "bg length") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

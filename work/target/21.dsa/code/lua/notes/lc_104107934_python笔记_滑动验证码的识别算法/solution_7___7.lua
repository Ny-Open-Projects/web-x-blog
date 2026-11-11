-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案7：合成数据 + 识别全流程）
local function detect_edges(image) -- local function detect_edges(image)
	local edges = {} -- 把 {} 写入 local edges
	for i = 1, #image do
		edges[i] = false
	end -- 把 1, #image do 边集[下标 i] 赋值为 false 终点 写入 for i
	for i = 2, #image do -- 把 2, #image do 写入 for i
		edges[i] = math.abs(image[i] - image[i - 1]) > 50 -- 把 math.取绝对值 image[下标 i] 减 image[下标 i 减 1]) 超过 50 写入 edges[i]
	end -- 终点
	return edges -- 返回 边集
end -- 终点

local function recognize_captcha(bg, puzzle) -- local function recognize_captcha(bg, puzzle)
	local bg_edges = detect_edges(bg) -- 把 detect_edges(bg) 写入 local bg_edges
	local puzzle_edges = detect_edges(puzzle) -- 把 detect_edges(puzzle) 写入 local puzzle_edges
	local best_x, best_score = 1, -1 -- 把 1, 减 1 写入 local best_x, best_score
	for x = 1, #bg - #puzzle + 1 do -- 把 1, #bg 减 #puzzle 加 1 do 写入 for x
		local score = 0 -- 把 0 写入 local score
		for y = 1, #puzzle do -- 把 1, #puzzle do 写入 for y
			if bg_edges[x + y - 1] and puzzle_edges[y] then
				score = score + 1
			end
		end -- 终点
		if score > best_score then -- 若 score 超过 best_score then
			best_score = score -- 把 score 存入 best_score
			best_x = x -- 把 x 存入 best_x
		end -- 终点
	end -- 终点
	return best_x - 1 -- 返回 best_x 减 1
end -- 终点

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
-- 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
assert(recognize_captcha(bg, puzzle) == 0, "synthetic") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

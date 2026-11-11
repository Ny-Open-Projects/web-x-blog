-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案5：边缘匹配 findGap 响应曲线）
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

local function find_gap(bg, puzzle) -- local function find_gap(bg, puzzle)
	local bg_edges = detect_edges(bg) -- 把 detect_edges(bg) 写入 local bg_edges
	local puzzle_edges = detect_edges(puzzle) -- 把 detect_edges(puzzle) 写入 local puzzle_edges
	local responses = {} -- 把 {} 写入 local responses
	for x = 1, #bg - #puzzle + 1 do -- 把 1, #bg 减 #puzzle 加 1 do 写入 for x
		local score = 0 -- 把 0 写入 local score
		for y = 1, #puzzle do -- 把 1, #puzzle do 写入 for y
			if bg_edges[x + y - 1] and puzzle_edges[y] then
				score = score + 1
			end
		end -- 终点
		responses[#responses + 1] = score -- 把 score 写入 responses[#responses + 1]
	end -- 终点
	local best_x = 1 -- 把 1 写入 local best_x
	for i = 2, #responses do -- 把 2, #responses do 写入 for i
		if responses[i] > responses[best_x] then
			best_x = i
		end
	end -- 终点
	return best_x - 1, responses -- 返回 best_x 减 1, responses
end -- 终点

local bg = { 10, 10, 10, 10, 200, 200, 200, 200 } -- 把 {10, 10, 10, 10, 200, 200, 200, 200} 写入 local bg
local puzzle = { 10, 200, 200, 200 } -- 把 {10, 200, 200, 200} 写入 local puzzle
local bx, resp = find_gap(bg, puzzle) -- 把 find_gap(bg, puzzle) 写入 local bx, resp
assert(bx == 3, "gap") -- 断言校验
local want_resp = { 0, 0, 0, 1, 0 } -- 把 {0, 0, 0, 1, 0} 写入 local want_resp
for i = 1, 5 do
	assert(resp[i] == want_resp[i], "responses")
end -- 让 下标 i 从 1 走到 5（Lua 1 基）
print("PASS") -- 全部用例通过，输出 PASS

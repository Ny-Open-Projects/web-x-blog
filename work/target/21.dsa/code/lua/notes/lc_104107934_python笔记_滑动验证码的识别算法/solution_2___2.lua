-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案2：Sobel 中心差分边缘 + 匹配）
local function detect_edges_sobel(image) -- local function detect_edges_sobel(image)
	local n = #image -- 把 #image 写入 local n
	local edges = {} -- 把 {} 写入 local edges
	for i = 1, n do
		edges[i] = false
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	if n < 2 then
		return edges
	end -- 若 元素个数 小于 2 then return 边集 终点
	edges[1] = math.abs(image[2] - image[1]) > 50 -- 把 math.取绝对值 image[2] 减 image[1]) 超过 50 写入 edges[1]
	for i = 2, n - 1 do -- 让 下标 i 从 2 走到 元素个数（Lua 1 基）
		edges[i] = math.abs(image[i + 1] - image[i - 1]) > 50
	end -- 终点
	edges[n] = math.abs(image[n] - image[n - 1]) > 50 -- 把 math.取绝对值 image[元素个数] 减 image[元素个数 减 1]) 超过 50 写入 edges[n]
	return edges -- 返回 边集
end -- 终点

local function recognize_captcha(bg, puzzle) -- local function recognize_captcha(bg, puzzle)
	local bg_edges = detect_edges_sobel(bg) -- 把 detect_edges_sobel(bg) 写入 local bg_edges
	local puzzle_edges = detect_edges_sobel(puzzle) -- 把 detect_edges_sobel(puzzle) 写入 local puzzle_edges
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

local bg = { 10, 10, 10, 10, 200, 200, 200, 200 } -- 把 {10, 10, 10, 10, 200, 200, 200, 200} 写入 local bg
local puzzle = { 10, 200, 200, 200 } -- 把 {10, 200, 200, 200} 写入 local puzzle
assert(recognize_captcha(bg, puzzle) == 3, "gap") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

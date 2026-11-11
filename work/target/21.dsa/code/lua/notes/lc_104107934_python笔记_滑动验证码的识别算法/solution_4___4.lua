-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案4：SAD 绝对差和最佳窗口）
local function best_match_window(bg, puzzle) -- local function best_match_window(bg, puzzle)
	local best_x, best_score = 1, math.huge -- 把 1, math.huge 写入 local best_x, best_score
	local n = #puzzle -- 把 #puzzle 写入 local n
	for x = 1, #bg - n + 1 do -- 把 1, #bg 减 元素个数 加 1 do 写入 for x
		local score = 0 -- 把 0 写入 local score
		for y = 0, n - 1 do -- 让 y 从 0 走到 元素个数（Lua 1 基）
			score = score + math.abs(bg[x + y] - puzzle[y + 1]) -- 把 score 加 math.取绝对值 bg[x 加 y] 减 puzzle[y 加 1]) 存入 score
		end -- 终点
		if score < best_score then -- 若 score 小于 best_score then
			best_score = score -- 把 score 存入 best_score
			best_x = x -- 把 x 存入 best_x
		end -- 终点
	end -- 终点
	return best_x - 1, best_score -- 返回 best_x 减 1, best_score
end -- 终点

local bg = { 10, 10, 10, 10, 200, 200, 200, 200 } -- 把 {10, 10, 10, 10, 200, 200, 200, 200} 写入 local bg
local puzzle = { 10, 200, 200, 200 } -- 把 {10, 200, 200, 200} 写入 local puzzle
local bx, bs = best_match_window(bg, puzzle) -- 把 best_match_window(bg, puzzle) 写入 local bx, bs
assert(bx == 3 and bs == 0, "gap failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

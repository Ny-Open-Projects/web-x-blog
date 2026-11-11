-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
-- LeetCode 104107934. 滑动验证码识别 — Lua 版（方案3：NCC 归一化互相关）
local function ncc_match(bg, puzzle) -- local function ncc_match(bg, puzzle)
	local best_x, best_score = 1, -math.huge -- 把 1, 减 math.huge 写入 local best_x, best_score
	local n = #puzzle -- 把 #puzzle 写入 local n
	for x = 1, #bg - n + 1 do -- 把 1, #bg 减 元素个数 加 1 do 写入 for x
		local bw, pw = 0, 0 -- 把 0, 0 写入 local bw, pw
		for i = 0, n - 1 do -- 让 下标 i 从 0 走到 元素个数（Lua 1 基）
			bw = bw + bg[x + i] -- 把 bw 加 bg[x 加 下标 i] 存入 bw
			pw = pw + puzzle[i + 1] -- 把 pw 加 puzzle[下标 i 加 1] 存入 pw
		end -- 终点
		bw = bw / n -- 把 bw 除以 元素个数 存入 bw
		pw = pw / n -- 把 pw 除以 元素个数 存入 pw
		local num, db, dp = 0, 0, 0 -- 把 0, 0, 0 写入 local num, db, dp
		for i = 0, n - 1 do -- 让 下标 i 从 0 走到 元素个数（Lua 1 基）
			local a = bg[x + i] - bw -- 把 bg[x 加 下标 i] 减 bw 写入 local a
			local b = puzzle[i + 1] - pw -- 把 puzzle[下标 i 加 1] 减 pw 写入 local b
			num = num + a * b -- 把 num 加 数组 乘 b 存入 num
			db = db + a * a -- 把 db 加 数组 乘 数组 存入 db
			dp = dp + b * b -- 把 DP 表 加 b 乘 b 存入 DP 表
		end -- 终点
		local denom = math.sqrt(db) * math.sqrt(dp) -- 把 math.sqrt(db) 乘 math.sqrt(DP 表) 写入 local denom
		local score = (denom ~= 0) and (num / denom) or 0 -- 把 (denom ~ 赋值为 0) and (num 除以 denom) or 0 写入 local score
		if score > best_score then -- 若 score 超过 best_score then
			best_score = score -- 把 score 存入 best_score
			best_x = x -- 把 x 存入 best_x
		end -- 终点
	end -- 终点
	return best_x - 1 -- 返回 best_x 减 1
end -- 终点

local bg = { 10, 10, 10, 10, 200, 200, 200, 200 } -- 把 {10, 10, 10, 10, 200, 200, 200, 200} 写入 local bg
local puzzle = { 10, 200, 200, 200 } -- 把 {10, 200, 200, 200} 写入 local puzzle
assert(ncc_match(bg, puzzle) == 3, "gap") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

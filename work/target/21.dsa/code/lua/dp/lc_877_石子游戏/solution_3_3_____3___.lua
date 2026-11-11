-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323
-- LeetCode 877. 石子游戏 — Lua 版（方案3）
local function stone_game(piles)
	return true
end -- local function stone_game(piles) return true 终点
assert(stone_game({ 5, 3, 4, 5 }) == true) -- 断言校验
assert(stone_game({ 3, 7, 2, 3 }) == true) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

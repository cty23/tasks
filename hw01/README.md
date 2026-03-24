1. 实现思路
本项目使用回溯算法求解 N 皇后问题。

算法通过递归方式逐列尝试放置皇后。在每一列中，程序会遍历所有行，并调用 is_safe 函数检查当前位置是否与已放置的皇后冲突。检查范围包括左侧水平行、左上对角线以及左下对角线。

为了支持自动化测试，solve_n_queens 函数设计了 callback 参数。每当找到一个合法解时，程序会通过该回调函数将当前的棋盘状态传递给测试框架进行计数或验证。

2. 项目结构
项目采用标准的 Python 模块化布局：

hw01/

src/
-- init.py
-- eight_queens_solver.py (核心算法实现)

tests/
-- init.py
-- test_eight_queens_solver.py (针对 N=4 和 N=8 的单元测试)

README.md

3. 运行与测试
运行算法：
在 hw01 根目录下执行 python src/eight_queens_solver.py。这将直接在终端打印 N=8 的图形化解。

运行测试：
在 hw01 根目录下执行 python -m unittest discover tests。

预期结果：
测试框架将自动运行两个测试用例。如果算法正确，终端将显示 Ran 2 tests 并提示 OK。

4. 自主修复记录
本项目模拟了 AI 辅助修复的过程：

第一步：故意将 is_safe 函数中的对角线冲突检查逻辑注释掉。
第二步：执行测试命令，发现 N=4 的解数量超过 2 个，测试触发 AssertionError。
第三步：将报错日志提供给 AI，AI 准确指出是函数内部逻辑导致了多余解的产生。
第四步：根据建议恢复代码，测试最终通过。

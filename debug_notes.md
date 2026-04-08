由于你之前在运行过程中遇到了 NameError（误复制引用标签）以及 GitHub 提交时的 rejected 错误，这些都是非常典型的调试案例。

你可以将以下内容直接放入 report.md 的末尾，或者单独保存为 debug_notes.md。

实验调试记录 (Debug Notes)
在完成 MNIST 手写数字识别任务的过程中，针对环境配置、代码执行及版本控制环节遇到的问题，记录如下：

1. 代码语法错误：NameError: name 'cite' is not defined
现象：运行 python train.py 时报错，提示 device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 行末尾存在未定义名称。


原因分析：在从 AI 助手或文档中复制代码时，不小心将解释性的引用标签（如 ）一并粘贴到了编辑器中，导致 Python 解释器无法识别这些非代码字符 。

修改点：清理代码中的所有非 Python 语法字符，确保 device 定义行纯净，修改后程序恢复正常。

2. 模型执行无响应：运行完“无事发生”
现象：执行 python lenet5.py 后，终端没有任何输出直接返回命令行。

原因分析：脚本中虽然定义了 LeNet5 类和训练函数，但缺少主程序入口（Entry Point），导致 Python 解释器加载完类定义后便结束进程。

修改点：在脚本末尾添加了 if __name__ == "__main__": 模块，显式调用了训练与测试函数，并加入了 print 语句以实时反馈训练进度。

3. Git 远程关联冲突：remote origin already exists
现象：执行 git remote add origin <url> 时提示远程仓库 origin 已存在。

原因分析：该本地目录之前可能已经初始化过 Git 或是多次尝试关联不同的远程仓库地址。

修改点：使用 git remote set-url origin <新的URL> 命令强制覆盖现有的远程仓库地址，并通过 git remote -v 验证生效。

4. GitHub 推送失败：rejected (fetch first)
现象：执行 git push 时报错，提示远程仓库包含本地没有的提交。

原因分析：GitHub 远程仓库在创建时初始化了 README 或 .gitignore 文件，导致远程分支进度领先于本地，且两者历史不相关。

修改点：

方案一（采用）：使用 git push -u origin main --force 进行强行推送，适用于初始化阶段覆盖远程空白模板。

方案二（规范）：使用 git pull --allow-unrelated-histories 先拉取合并远程文件，再进行推送。

5. 提交包含大文件（已预见）
现象：git commit 列表显示包含多个 data/MNIST/raw/*.gz 文件，导致提交包体积过大。

原因分析：未提前配置 .gitignore 文件，导致 MNIST 数据集被意外追踪。

修改点：在后续操作中创建 .gitignore 文件并写入 data/ 和 __pycache__/，确保仓库只包含核心源码和报告。

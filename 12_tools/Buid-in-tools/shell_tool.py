from langchain_community.tools import ShellTool

shelltool = ShellTool()

results = shelltool.invoke('dir')

print(results)
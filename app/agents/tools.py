from langchain.tools import ToolRuntime, tool


@tool(parse_docstring=True)
def get_user_favorite_food(runtime: ToolRuntime) -> str:
    """获取用户最喜欢的食物"""
    return "披萨，尤其是必胜客的比萨"

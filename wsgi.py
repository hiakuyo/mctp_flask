import os
import sys

# 将项目根目录添加到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, project_root)

from mctp import create_app  # 根据你的实际工厂函数名调整

# 调用工厂函数创建应用实例
application = create_app()

if __name__ == "__main__":
    application.run(debug=True)
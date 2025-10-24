import os

from flask import Flask
from flask_restful import Api

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='hiakuyo',
        # DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
    )

    # app.config.from_pyfile()使用config.py中的值来重载缺省配置
    if test_config is None:
        # 如果非测试环境且实例配置存在则加载之
        app.config.from_pyfile('config.py',silent=True)
    else:
        # 否则加载测试用配置
        app.config.from_mapping(test_config)

    # 确保实例文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app,prefix='/api/v1')
    
    from .api import reg_resources
    reg_resources(api)

    return app
from flask_restful import Resource, reqparse, abort
from flask import request, jsonify, current_app

'''
# 请求参数解析器 - 用户相关
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help='用户名不能为空')
user_parser.add_argument('email', type=str, required=True, help='邮箱不能为空')
user_parser.add_argument('password', type=str, required=True, help='密码不能为空')

# 请求参数解析器 - 文章相关  
post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help='标题不能为空')
post_parser.add_argument('content', type=str, required=True, help='内容不能为空')
post_parser.add_argument('user_id', type=int, required=True, help='用户ID不能为空')
'''

class test_resource(Resource):
    def get(self):
        return {
            'code':200,
            'data':None,
            'msg':'this is test'
        }
from .resources import (
    test_resource
)

__all__ = [
    'test_resource'
]

def reg_resources(api):
    api.add_resource(test_resource,'/test')
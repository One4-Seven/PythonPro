import pytest
from function import *

@pytest.fixture    # 创建夹具 #
def collection():
    collection = collect_info()
    return collection

def test_make_name():
    really_name = make_name('mike','cheng')
    assert really_name == 'Mike Cheng'

def test_make_middle_name():
    really_name = make_name('jett','fade','sage')
    assert really_name == 'Jett Sage Fade'

def test_collect_info(collection):    # 当测试函数的形参与夹具名相同时会自动运行夹具并且将返回值传给测试函数 #
    collection.collect('english')
    assert 'english' in collection.answers

def test_more_collect_info(collection):
    answers = ['english','chinese','spanish']
    for answer in answers:
        collection.collect(answer)
    for answer in answers:
        assert answer in collection.answers    
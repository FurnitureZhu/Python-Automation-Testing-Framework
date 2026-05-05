import pytest
from common.request_util import RequestUtil
from common.read_yaml import read_yaml
from common.log_util import logger

data = read_yaml("data/login_data.yaml")['login']

@pytest.mark.parametrize("case", data)
def test_login(case):
    logger.info(f"执行用例: {case['name']}")

    resp = RequestUtil.send_request(
        method="POST",
        url="/post",
        json=case['data']
    )

    logger.info(resp.text)

    assert resp.status_code == case['expect']
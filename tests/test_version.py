"""funjson 占位包的基础测试：验证包可导入，且版本信息符合规范。"""

import re

import funjson


def test_import():
    """包必须能正常导入。"""
    assert funjson is not None


def test_version_exists():
    """__version__ 必须存在且是非空字符串。"""
    assert hasattr(funjson, "__version__")
    assert isinstance(funjson.__version__, str)
    assert funjson.__version__ != ""


def test_version_format():
    """__version__ 必须符合语义化版本号格式（主.次.修订）。"""
    assert re.match(r"^\d+\.\d+\.\d+$", funjson.__version__)

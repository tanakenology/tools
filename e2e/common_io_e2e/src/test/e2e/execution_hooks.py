from getgauge.python import before_suite
from src.test.e2e.common_io_impl import install_common_io


@before_suite
def before_suite_hooks():
    install_common_io()

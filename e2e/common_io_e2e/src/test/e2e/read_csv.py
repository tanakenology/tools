import subprocess

from getgauge.python import data_store, step


def install_common_io():
    subprocess.run(["pip", "install", "-e", "../../apps/common_io/."])


@step("<uri> を json として読み込む")
def execute_as_json(uri: str):
    import common_io

    data_store.scenario["response"] = list(common_io.read_csv(uri))


@step("<uri> を list として読み込む")
def execute_as_list(uri: str):
    import common_io

    data_store.scenario["response"] = list(
        common_io.read_csv(uri, row_as_list=True)
    )


@step("返り値が <data_type> と一致する")
def assert_response(data_type: str):
    from src.test.resources.read_csv import expected

    assert data_store.scenario["response"] == expected.response[data_type]

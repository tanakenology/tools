import subprocess

from getgauge.python import data_store, step


def install_common_io():
    subprocess.run(["pip", "install", "-e", "../../apps/common_io/."])


@step("<uri> を json として読み込む")
def execute_read_csv_as_json(uri: str):
    import common_io

    data_store.scenario["response"] = list(common_io.read_csv(uri))


@step("<uri> を list として読み込む")
def execute_read_csv_as_list(uri: str):
    import common_io

    data_store.scenario["response"] = list(
        common_io.read_csv(uri, row_as_list=True)
    )


@step("jsonlines ファイル <uri> を読み込む")
def execute_read_jsonlines(uri: str):
    import common_io

    data_store.scenario["response"] = list(common_io.read_jsonlines(uri))


@step("返り値が <data_type> と一致する")
def assert_response(data_type: str):
    from src.test.resources.read_csv import expected

    assert data_store.scenario["response"] == expected.response[data_type]


@step("<uri> に <data_type> を保存する")
def execute_write_csv(uri: str, data_type: str):
    import common_io
    from src.test.resources.write_csv import actual

    common_io.write_csv(uri, actual.fixtures[data_type])


@step("jsonlines ファイルパス <uri> に <data_type> を保存する")
def execute_write_jsonlines(uri: str, data_type: str):
    import common_io
    from src.test.resources.write_jsonlines import actual

    common_io.write_jsonlines(uri, actual.fixtures[data_type])

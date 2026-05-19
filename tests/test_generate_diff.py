from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_json():
    first_json = get_test_data_path("file1.json")
    second_json = get_test_data_path("file2.json")
    result = read_file("result.txt")

    assert generate_diff(first_json, second_json) == result


def test_generate_diff_yaml():
    first_yaml = get_test_data_path("file1.yml")
    second_yaml = get_test_data_path("file2.yml")
    result = read_file("result.txt")

    assert generate_diff(first_yaml, second_yaml) == result


def test_generate_diff_json_deep():
    first_json = get_test_data_path("file1_deep.json")
    second_json = get_test_data_path("file2_deep.json")
    result = read_file("result_deep.txt")

    assert generate_diff(first_json, second_json) == result


def test_generate_diff_yaml_deep():
    first_yaml = get_test_data_path("file1_deep.yml")
    second_yaml = get_test_data_path("file2_deep.yml")
    result = read_file("result_deep.txt")

    assert generate_diff(first_yaml, second_yaml) == result
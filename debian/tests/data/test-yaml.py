# very crude smoke test of the yaml package

from ruamel.yaml import YAML


def test_load_clib():
    import ruamel.yaml.cyaml

def test_safe_load():
    yaml = YAML(typ="safe", pure=False)
    with open("test-yaml.yaml") as fh:
        y = yaml.load(fh)

    assert len(y['testdata']) == 2

    assert len(y['testdata']['test1']) == 3

    assert len(y['testdata']['test-data-2']) == 2


if __name__ == "__main__":
    test_safe_load()
    print("Complete.")

import unittest

from jsonx import unflatten


class JsonXTestCase(unittest.TestCase):
    def test_unflatten_standard(self):
        input = {
            "first": "second",
            "third": "fourth",
        }
        output = unflatten(data=input)
        assert output == input

    def test_unflatten_nested_dict(self):
        input = {
            "first.second": "third",
            "first.fourth": "fifth",
            "sixth.seventh.eighth.ninth": "tenth",
            "11.12": "thirteenth",
        }
        expected_output = {
            "first": {
                "second": "third",
                "fourth": "fifth",
            },
            "sixth": {
                "seventh": {
                    "eighth": {
                        "ninth": "tenth",
                    },
                },
            },
            "11": {
                "12": "thirteenth",
            },
        }
        output = unflatten(data=input)
        assert output == expected_output

    def test_unflatten_shallow_root_list(self):
        input = {
            "[0]": "zero",
            "[1]": "one",
        }
        expected_output = ["zero", "one"]
        output = unflatten(data=input)
        assert output == expected_output

    def test_unflatten_deep_root_list(self):
        input = {
            "[0].first": "second",
            "[0].third": "fourth",
            "[1].fifth": "sixth",
            "[1].seventh.eighth": "ninth",
            "[2]": "tenth",
        }
        expected_output = [
            {
                "first": "second",
                "third": "fourth",
            },
            {
                "fifth": "sixth",
                "seventh": {
                    "eighth": "ninth"
                },
            },
            "tenth",
        ]
        output = unflatten(data=input)
        assert output == expected_output

    def test_unflatten_nested_list(self):
        input = {
            "first.[0].second": "third",
            "first.[1]": "fourth",
            "first.[2].fifth.sixth.[0]": "seventh",
            "first.[0].eighth": "ninth",
            "first.[0].tenth.eleventh": "twelfth",
            "thirteenth": "fourteenth",
        }
        expected_output = {
            "first":
                [
                    {
                        "second": "third",
                        "eighth": "ninth",
                        "tenth": {
                            "eleventh": "twelfth",
                        },
                    }, "fourth", {
                        "fifth": {
                            "sixth": ["seventh"],
                        },
                    }
                ],
            "thirteenth": "fourteenth",
        }
        output = unflatten(data=input)
        assert output == expected_output


if __name__ == "__main__":
    unittest.main()

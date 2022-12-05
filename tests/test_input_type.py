import pytest
import sys

# setting path
sys.path.append("../src")
from validationOfStringCPE import validationOfInputType


def test_input_type() -> None:

    listOfPossibleInputs = [123, ["check", 56], 6.5, {"car": "bmw"}, (3, 5)]

    for item in listOfPossibleInputs:
        with pytest.raises(TypeError):
            validationOfInputType(item)

from django.core.exceptions import ValidationError

import pytest

from website.validators import pis_validator


class TestPISValidator:
    def test_if_validators_can_have_false_positives(self):
        with pytest.raises(ValidationError):
            pis_validator("aaaaaaaaaaa")
        with pytest.raises(ValidationError):
            pis_validator("aaaaaaaaaaaaaa")
        with pytest.raises(ValidationError):
            pis_validator("123456789101")

    def test_if_validator_can_have_false_negative(self):
        try:
            pis_validator("75123269085")
        except ValidationError:
            assert False, "validator invalidated a valid PIS"

import pytest

class TestPages:

    @pytest.mark.parametrize("user_type", ["admin", "manager", "user"])
    @pytest.mark.parametrize("status", ["active", "inactive", "cancelled", "postponed"])
    def test_check_account(self, user_type, status):
        print(f"{user_type}::{status}")



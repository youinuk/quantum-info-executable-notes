from scripts.validate_mapping import validate

def test_mapping_is_internally_consistent() -> None:
    assert validate() == []

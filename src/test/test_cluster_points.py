from main import convert_radians_to_km


def test_convert_radians_to_km():
    # Test with known input and expected output
    radians = 1.0
    expected_km = 6371.0
    assert convert_radians_to_km(radians) == expected_km
    
    # Test with 0 radians
    radians = 0.0
    expected_km = 0.0
    assert convert_radians_to_km(radians) == expected_km

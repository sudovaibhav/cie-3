from students import test_students_details
def test_students_details():
    expected_output = (
        f"USN: 01fe24bca300\n"
        f"Name: Vaibhav\n"
        f"Division: E\n"
        f"Age: 20\n"
    )
    
    assert students_details("01fe24bca300", "Vaibhav", "E", 20) == expected_output
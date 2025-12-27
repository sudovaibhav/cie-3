def students_details(usn, name, division, age):
    result = (
        f"USN: {usn}\n"
        f"Name: {name}\n"
        f"Division: {division}\n"
        f"Age: {age}\n"                
    )
    return result
if __name__ == "__main__":
    usn = "01fe24bca300"
    name = "Vaibhav"
    division = "E"
    age = 20
    print(students_details(usn, name, division, age))
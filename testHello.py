print("Python exceptions:")

student={
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as errorMessage:
    print("Unable to add int and string")
    print(errorMessage)
except Exception:
    print("Unhandled exception occurred")

print("End of execution")
def register_student(name, event):
    return f"{name} registered for {event}"


def create_event(event_name):
    return f"Event '{event_name}' created successfully"


def mark_attendance(student_name):
    return f"Attendance marked for {student_name}"


def generate_certificate(student_name, event):
    return f"Certificate generated for {student_name} for {event}"


print("Smart Event Management System")

print(create_event("Tech Fest 2026"))
print(register_student("Rahul", "Tech Fest 2026"))
print(mark_attendance("Rahul"))
print(generate_certificate("Rahul", "Tech Fest 2026"))

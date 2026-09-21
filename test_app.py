from app import register_student
from app import create_event
from app import mark_attendance
from app import generate_certificate


def test_register_student():
    assert register_student("Rahul", "Tech Fest 2026") == "Rahul registered for Tech Fest 2026"


def test_create_event():
    assert create_event("Tech Fest 2026") == "Event 'Tech Fest 2026' created successfully"


def test_mark_attendance():
    assert mark_attendance("Rahul") == "Attendance marked for Rahul"


def test_generate_certificate():
    assert generate_certificate("Rahul", "Tech Fest 2026") == "Certificate generated for Rahul for Tech Fest 2026"

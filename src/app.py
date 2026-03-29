"""
NMAMIT MCA Git Workshop - Sample Application
A simple student directory app to practice Git workflows.
"""


def greet(name: str) -> str:
    """Return a greeting message for a student."""
    return f"Hello, {name}! Welcome to the Git Workshop!"


def add_student(students: list, name: str, branch: str) -> list:
    """Add a student to the directory."""
    student = {
        "name": name,
        "branch": branch,
        "semester": "MCA",
    }
    students.append(student)
    return students


def list_students(students: list) -> None:
    """Display all students in the directory."""
    if not students:
        print("No students registered yet.")
        return

    print(f"\n{'Name':<20} {'Branch':<15} {'Semester':<10}")
    print("-" * 45)
    for s in students:
        print(f"{s['name']:<20} {s['branch']:<15} {s['semester']:<10}")


def calculate_attendance(present: int, total: int) -> float:
    """Calculate attendance percentage."""
    if total == 0:
        return 0.0
    return round((present / total) * 100, 2)


if __name__ == "__main__":
    print("=" * 45)
    print("  NMAMIT MCA - Student Directory")
    print("=" * 45)

    directory = []

    directory = add_student(directory, "Tushar Prabhu", "MCA")
    directory = add_student(directory, "Workshop Student", "MCA")

    list_students(directory)

    print(f"\n{greet('MCA Students')}")
    print(f"\nSample Attendance: {calculate_attendance(18, 20)}%")

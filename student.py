class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, gpa):
        """Thêm sinh viên mới vào danh sách"""
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "gpa": gpa
        }
        self.students.append(student)
        print(f"-> Đã thêm sinh viên: {name} ({student_id})")

    def display_students(self):
        """Hiển thị danh sách sinh viên"""
        if not self.students:
            print("Danh sách sinh viên hiện đang trống.")
            return
        
        print("\n=== DANH SÁCH SINH VIÊN ===")
        for s in self.students:
            print(f"Mã SV: {s['id']} | Họ tên: {s['name']} | Tuổi: {s['age']} | GPA: {s['gpa']}")
        print("===========================\n")

    def search_student(self, student_id):
        """Tìm kiếm sinh viên theo mã SV"""
        for s in self.students:
            if s["id"].lower() == student_id.lower():
                return s
        return None


if __name__ == "__main__":
    manager = StudentManager()
    
    # Thêm sinh viên thử nghiệm
    manager.add_student("SV001", "Nguyễn Văn A", 20, 3.5)
    manager.add_student("SV002", "Trần Thị B", 21, 3.8)
    
    # Hiển thị danh sách
    manager.display_students()
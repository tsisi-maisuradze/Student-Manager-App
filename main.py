import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QListWidget
from database import DatabaseManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Manager")
        self.resize(600, 500)
        self.db = DatabaseManager()
        self.setup_ui()
        self.load_students()

    def setup_ui(self):
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("სახელი")

        self.surname_input = QLineEdit()
        self.surname_input.setPlaceholderText("გვარი")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("ასაკი")

        self.faculty_input = QLineEdit()
        self.faculty_input.setPlaceholderText("ფაკულტეტი")

        self.add_btn = QPushButton("დამატება")
        self.add_btn.clicked.connect(self.add_student)

        self.delete_btn = QPushButton("წაშლა")
        self.delete_btn.clicked.connect(self.delete_student)

        self.list_widget = QListWidget()


        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.surname_input)
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(self.faculty_input)
        form_layout.addWidget(self.add_btn)
        form_layout.addWidget(self.delete_btn)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_student(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        age = self.age_input.text()
        faculty = self.faculty_input.text()


        self.db.add_student(name, surname, age, faculty)
        self.load_students()
        self.name_input.clear()
        self.surname_input.clear()
        self.age_input.clear()
        self.faculty_input.clear()

    def delete_student(self):
        selected = self.list_widget.currentItem()
        if selected:
            student_id = int(selected.text().split(":")[0])
            self.db.delete_student(student_id)
            self.load_students()

    def load_students(self):
        self.list_widget.clear()
        for student in self.db.get_students():
            self.list_widget.addItem(f"{student[0]}: {student[1]} {student[2]}, {student[3]} წლის, {student[4]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

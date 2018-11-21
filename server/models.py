from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)
    classroom_id = db.Column(db.Integer, db.ForeignKey(
        'classroom.classroom_id'), nullable=False)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Classroom(db.Model):
    """table of classroom"""

    __tablename__ = "classrooms"

    classroom_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.student_id'), nullable=False)


class Student(db.Model):
    """table of students"""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = (db.String(64), nullable=False)
    last_name = (db.String(64), nullable=False)
    grade = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<Student student_id={self.student_id} first_name={self.first_name} last_name={self.last_name}>"


class Word(db.Model):
    """table of words"""

    __tablename__ = "words"

    word_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    word = (db.String(25), nullable=False)

    def __repr__(self):
        return f"<Word word_id={self.word_id} word={self.word}>"


class StudentWord(db.Model):
    """table of student words"""

    __tablename__ = "studentwords"

    student_word_id = db.Column(
        db.Integer, autoincrement=True, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey(
        'words.word_id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.student_id'), nullable=False)

    def __repr__(self):
        return f"<StudentWord student_word_id={self.student_word_id}>"


class StudentTest(db.Model):
    """table of student tests"""

    __tablename__ = "studenttest"

    student_test_id = db.Column(
        db.Integer, autoincrement=True, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.student_id'), nullable=False)
    test_date = db.Column(db.DateTime, nullable=True)
    num_correct = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<StudentTest student_test_id={self.student_test_id}>"


class WordTest(db.Model):
    """table of student tests"""

    __tablename__ = "wordtest"

    word_test_id = db.Column(
        db.Integer, autoincrement=True, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey(
        'words.word_id'), nullable=False)
    test_date = db.Column(db.DateTime, nullable=True)
    num_correct = db.Column(db.Integer, nullable=True)


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///literacy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")

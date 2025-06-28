from sqlalchemy import text


def test_add_student(db_session):
    """Тест добавления нового студента"""
    # Подготовка тестовых данных
    new_user_id = 9999
    new_email = "test_student@example.com"
    subject_id = 1

    # Удаляем тестовые данные, если они уже есть
    db_session.execute(text("DELETE FROM users WHERE user_id = :user_id"),
                       {"user_id": new_user_id})
    db_session.execute(text("DELETE FROM student WHERE user_id = :user_id"),
                       {"user_id": new_user_id})

    # Добавляем нового пользователя (студента)
    db_session.execute(
        text("INSERT INTO users (user_id, user_email, subject_id) VALUES (:user_id, :email, :subject_id)"),
        {"user_id": new_user_id, "email": new_email, "subject_id": subject_id}
    )

    # Добавляем запись в таблицу student
    db_session.execute(
        text(
            "INSERT INTO student (user_id, level, education_form, subject_id) VALUES (:user_id, 'beginner', 'full-time', :subject_id)"),
        {"user_id": new_user_id, "subject_id": subject_id}
    )

    # Проверяем, что данные добавились
    user = db_session.execute(
        text("SELECT * FROM users WHERE user_id = :user_id"),
        {"user_id": new_user_id}
    ).fetchone()

    student = db_session.execute(
        text("SELECT * FROM student WHERE user_id = :user_id"),
        {"user_id": new_user_id}
    ).fetchone()

    assert user is not None
    assert user.user_email == new_email
    assert student is not None
    assert student.level == "beginner"


def test_update_teacher_email(db_session):
    """Тест изменения email преподавателя"""
    # Выбираем существующего преподавателя для теста
    teacher = db_session.execute(
        text("SELECT * FROM teacher LIMIT 1")
    ).fetchone()

    if not teacher:
        pytest.skip("No teachers found in the database")

    teacher_id = teacher.teacher_id
    new_email = "updated_teacher@example.com"

    # Обновляем email
    db_session.execute(
        text("UPDATE teacher SET email = :email WHERE teacher_id = :teacher_id"),
        {"email": new_email, "teacher_id": teacher_id}
    )

    # Проверяем обновление
    updated_teacher = db_session.execute(
        text("SELECT * FROM teacher WHERE teacher_id = :teacher_id"),
        {"teacher_id": teacher_id}
    ).fetchone()

    assert updated_teacher.email == new_email


def test_soft_delete_subject(db_session):
    """Тест мягкого удаления предмета"""
    # Сначала добавим тестовый предмет
    subject_id = 9999
    subject_title = "Test Subject"

    # Удаляем, если уже существует
    db_session.execute(text("DELETE FROM subject WHERE subject_id = :subject_id"),
                       {"subject_id": subject_id})

    # Добавляем тестовый предмет
    db_session.execute(
        text("INSERT INTO subject (subject_id, subject_title) VALUES (:subject_id, :title)"),
        {"subject_id": subject_id, "title": subject_title}
    )

    # Проверяем, что предмет добавился
    subject = db_session.execute(
        text("SELECT * FROM subject WHERE subject_id = :subject_id"),
        {"subject_id": subject_id}
    ).fetchone()
    assert subject is not None

    # "Удаляем" предмет (soft delete)
    # Для этого сначала добавим колонку is_deleted, если её нет
    try:
        db_session.execute(text("ALTER TABLE subject ADD COLUMN IF NOT EXISTS is_deleted BOOLEAN DEFAULT FALSE"))
    except:
        pass  # Колонка уже существует

    db_session.execute(
        text("UPDATE subject SET is_deleted = TRUE WHERE subject_id = :subject_id"),
        {"subject_id": subject_id}
    )

    # Проверяем, что предмет "удален"
    deleted_subject = db_session.execute(
        text("SELECT * FROM subject WHERE subject_id = :subject_id AND is_deleted = TRUE"),
        {"subject_id": subject_id}
    ).fetchone()

    assert deleted_subject is not None
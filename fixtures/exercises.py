import pytest
from clients.exercises.exercises_client import get_private_exercise_client, ExercisesClient
from clients.exercises.exercises_shema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from pydantic import BaseModel


class ExerciseFixture(BaseModel, frozen=True):
    """
    Pydantic-модель, объединяющая запрос и ответ при создании упражнения.
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Фикстура для инициализации клиента для работы с упражнениями (ExercisesClient).

    :param function_user: Фикстура для создания пользователя.
    :return: Настроенный клиент для работы с упражнениями. (ExercisesClient)
    """
    return get_private_exercise_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(exercise_client: ExercisesClient,
                      function_course: CourseFixture):
    """
    Фикстура для создания упражнения в курсе.

    :param exercise_client: Фикстура для инициализации клиента (ExercisesClient).
    :param function_course: Фикстура для создания курса.
    :return: Pydantic-модель, объединяющая запрос и ответ при создании упражнения.
    """
    request = CreateExerciseRequestSchema(courseId=function_course.course_id)
    response = exercise_client.create_exercise(request=request)
    return ExerciseFixture(request=request, response=response)

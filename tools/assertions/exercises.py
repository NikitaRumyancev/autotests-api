from clients.exercises.exercises_shema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, ExerciseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length


def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    """
    Метод проверяет, что информация в ответе при создании упражнения соответствует информации в
    запросе на создание упражнения.

    :param actual: Фактические данные в ответе.
    :param expected: Ожидаемые данные в ответе.
    :raises:  AssertionError, если хотя бы одно поле не совпадает с ожидаемым.
    """
    assert_equal(actual=actual.exercise.title, expected=expected.title, name="title")
    assert_equal(actual=actual.exercise.course_id, expected=expected.course_id, name="course_id")
    assert_equal(actual=actual.exercise.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.exercise.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.exercise.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.exercise.order_index, expected=expected.order_index, name="order_index")
    assert_equal(actual=actual.exercise.description, expected=expected.description, name="description")
    assert_equal(actual=actual.exercise.estimated_time, expected=expected.estimated_time, name="estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Метод проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные.
    :param expected: Ожидаемые данные.
    :raises: AssertionError, если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.title, expected=expected.title, name="title")
    assert_equal(actual=actual.course_id, expected=expected.course_id, name="course_id")
    assert_equal(actual=actual.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.order_index, expected=expected.order_index, name="order_index")
    assert_equal(actual=actual.description, expected=expected.description, name="description")
    assert_equal(actual=actual.estimated_time, expected=expected.estimated_time, name="estimated_time")


def assert_get_exercise_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercises_response: list[CreateExerciseResponseSchema]
):
    """
   Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

   :param get_exercises_response: Ответ API при запросе списка заданий.
   :param create_exercises_response: Список API ответов при создании заданий.
   :raises AssertionError: Если данные заданий не совпадают.
   """
    assert_length(actual=get_exercises_response.exercises, expected=create_exercises_response, name="exercises")

    for index, exercise in enumerate(create_exercises_response):
        assert_exercise(actual=get_exercises_response.exercises[index], expected=exercise.exercise)

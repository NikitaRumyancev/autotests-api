from clients.exercises.exercises_shema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    """
    Метод проверяет, что фактические данные упражнения соответсвуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises: AssertionError, если хотя бы одно поле не совпадает.
    """
    assert_equal(actual=actual.exercise.title, expected=expected.title, name="title")
    assert_equal(actual=actual.exercise.course_id, expected=expected.course_id, name="course_id")
    assert_equal(actual=actual.exercise.max_score, expected=expected.max_score, name="max_score")
    assert_equal(actual=actual.exercise.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.exercise.min_score, expected=expected.min_score, name="min_score")
    assert_equal(actual=actual.exercise.order_index, expected=expected.order_index, name="order_index")
    assert_equal(actual=actual.exercise.description, expected=expected.description, name="description")
    assert_equal(actual=actual.exercise.estimated_time, expected=expected.estimated_time, name="estimated_time")
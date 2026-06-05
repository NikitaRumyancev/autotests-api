from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_shema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesQuerySchema, GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:

    def test_create_exercise(self,
                             exercises_client: ExercisesClient,
                             function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.course_id)
        response = exercises_client.create_exercise_api(request=request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_exercise_response(actual=response_data, expected=request)

        validate_json_schema(instance=response.json(), schema=CreateExerciseResponseSchema.model_json_schema())

    def test_get_exercise(self,
                          exercises_client: ExercisesClient,
                          function_exercise: ExerciseFixture):
        query = GetExercisesQuerySchema(course_id=function_exercise.response.exercise.course_id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_exercise_response(response_data, [function_exercise.response])

        validate_json_schema(instance=response.json(), schema=GetExercisesResponseSchema.model_json_schema())

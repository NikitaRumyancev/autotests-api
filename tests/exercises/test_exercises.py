from http import HTTPStatus

import allure
import pytest

from clients.errors_schemas import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_shema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExercisesQuerySchema, GetExercisesResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture, function_exercise
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response, \
    assert_get_exercise_response
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
from allure_commons.types import Severity


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
class TestExercises:
    """
    Тестовый класс для тестирования сценариев связанных с файлами.
    """

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create exercise")
    def test_create_exercise(self,
                             exercises_client: ExercisesClient,
                             function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.course_id)
        response = exercises_client.create_exercise_api(request=request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_exercise_response(actual=response_data, expected=request)

        validate_json_schema(instance=response.json(), schema=CreateExerciseResponseSchema.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get exercise")
    def test_get_exercise(self,
                          exercises_client: ExercisesClient,
                          function_exercise: ExerciseFixture):
        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_exercise_response(
            create_exercise_request=function_exercise.request,
            get_exercise_response=response_data)

        validate_json_schema(instance=response.json(), schema=GetExerciseResponseSchema.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update exercise")
    def test_update_exercise(self,
                             exercises_client: ExercisesClient,
                             function_exercise: ExerciseFixture):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            exercise_id=function_exercise.response.exercise.id,
            request=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_update_exercise_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=UpdateExerciseResponseSchema.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete exercise")
    def test_delete_exercise(self,
                             exercises_client: ExercisesClient,
                             function_exercise: ExerciseFixture):
        exercises_client.delete_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = InternalErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(actual=response_data)

        validate_json_schema(instance=response.json(), schema=InternalErrorResponseSchema.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("Get exercises")
    def test_get_exercises(self,
                           exercises_client: ExercisesClient,
                           function_exercise: ExerciseFixture,
                           function_course: CourseFixture):
        query = GetExercisesQuerySchema(course_id=function_course.course_id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

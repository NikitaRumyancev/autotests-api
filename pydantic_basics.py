import uuid

from pydantic import BaseModel, Field, ConfigDict, alias_generators, computed_field
from pydantic.alias_generators import to_camel
from pydantic.json_schema import model_json_schema


model_data = {
    "id": "",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string"
}

class CourseShema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = Field(default="BOBOBO")
    max_score: int = 100
    min_score: int = 10
    description: str = "description"
    estimated_time: str = "estimatedTime"

    @computed_field()
    def barabash(self) -> str:
        return str(self.description)

model1 = CourseShema()

print(model1.model_dump_json(by_alias=True))

# model2 = CourseShema(**model_data)
# print(model2.model_dump_json(by_alias=True))
#
# # #print(course_model)
#
# course_create_data = {
#     "id": 1332,
#     "title": "test_title",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "test_description",
#     "estimatedTime": "two_weeks"
# }
#
# json_str = """
# {
#     "id": 1222,
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "estimatedTime": "string"
# }
# """
#
# model = CourseShema(**course_create_data)
# print(model)
#
# print(f"Course model dict:", model.model_dump(by_alias=True))
#
# print(f"Course model JSON:", model.model_dump_json(by_alias=True))
#
#
#
# model_json_schemas = CourseShema.model_validate_json(json_str)
# print(model_json_schemas)

# import platform
#
#
# print(f'{platform.system()}, {platform.release()}')
#
# Windows, 11
# 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)]
# import sys
#
#
# print(sys.version)
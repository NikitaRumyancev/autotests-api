from enum import Enum


class AllureFeature(str, Enum):
    USERS = "Users"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    FILES = "Files"
    AUTHENTICATION = "Authentication"
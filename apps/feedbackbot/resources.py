import json
from datetime import time
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, Widget

from .models import Student, Teacher, Lesson, ClassSchedule, Score, Group


class StudentResource(resources.ModelResource):
    group = fields.Field(
        column_name='group',
        attribute='group',
        widget=ForeignKeyWidget(Group, 'group_num'))

    class Meta:
        model = Student
        fields = ('login_id', 'password', 'first_name', 'last_name', 'group')
        exclude = ('id',)
        import_id_fields = ['login_id']


class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name')

    def get_import_id_fields(self):
        return ['id']


class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson
        fields = ('id', 'name',)

    def get_import_id_fields(self):
        return ['id']


class TimeWidget(Widget):
    def clean(self, value, row=None, **kwargs):
        if value:
            value = str(value)
            try:
                return time.fromisoformat(value)
            except ValueError:
                return None
        return None


class ClassScheduleResource(resources.ModelResource):
    group = fields.Field(
        column_name='group',
        attribute='group',
        widget=ForeignKeyWidget(Group, 'group_num'))
    lesson = fields.Field(
        column_name='lesson',
        attribute='lesson',
        widget=ForeignKeyWidget(Lesson, 'name'))
    teacher = fields.Field(
        column_name='teacher',
        attribute='teacher',
        widget=ForeignKeyWidget(Teacher, 'full_name'))

    class Meta:
        model = ClassSchedule
        fields = ('day', 'start_time', 'room', 'group', 'lesson', 'teacher')
        exclude = ('id',)
        import_id_fields = ['day', 'start_time', 'group', 'lesson', 'teacher']


class ScoreResource(resources.ModelResource):
    class Meta:
        model = Score
        fields = ('id', 'score_for_teacher', 'feedback', 'teacher__full_name', 'lesson__name')

    def get_import_id_fields(self):
        return ['id']


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        fields = ('id', 'group_num', 'type')

    def get_import_id_fields(self):
        return ['id']
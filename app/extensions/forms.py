from django import forms
from core.models import Student, Assignment
from enrollments.models import Enrollment
from extensions.models import Extension, Date
import datetime

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class StudentIdForm(forms.Form):
    """
    This form should have a single field: student_id (int).
    It should be validated against the sis_user_id field in the Student model.
    The input integer should be 9 digits long and should be in the string of the sis_user_id field.
    """
    student_id = forms.IntegerField(label="Student ID")

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if len(str(student_id)) != 9:
            raise forms.ValidationError("Student ID must be 9 digits long")
        return student_id
    
    def clean(self):

        cleaned_data = super(StudentIdForm, self).clean()
        student_id = cleaned_data.get('student_id')

        if student_id:
            try:
                Student.objects.get(sis_user_id__contains=str(student_id))
            except Student.DoesNotExist:
                raise forms.ValidationError("Student ID does not exist")
        return cleaned_data
    
class CourseForm(forms.Form):
    """
    This has a choice field containing all of the courses for the student.
    The student_id is in the url and should be used to get all the enrollment objects that belong to the student.
    Use a Choice Field to display the courses (not a ModelChoiceField).
    """

    def __init__(self, *args, **kwargs):
        student_id = kwargs.pop('student_id', None)
        super(CourseForm, self).__init__(*args, **kwargs)
        choices=[(enrollment.canvas_course_id, enrollment.course) for enrollment in Enrollment.objects.filter(sis_user_id__contains=student_id)]
        print("choices:", choices)
        self.fields['course'] = forms.ChoiceField(
            choices=choices
            )



class AssignmentForm(forms.Form):
    """
    Create a Model Form using the Extension model.

    This has a dropdown field containing all of the assignments for the course.
    The course_canvas_id is in the url and is used to get all the assignments that belong to the course.
    Only list assignments if they are active.
    Use a ChoiceField to display the assignments (not a ModelChoiceField).
    Use a ChoiceField to display the options (1 week, 2 weeks)
    """

    def __init__(self, *args, **kwargs):
        print("kwargs:", kwargs)
        print("args:", args)
        course_canvas_id = kwargs.pop('course_canvas_id', None)
        student_id = kwargs.pop('student_id', None)
        super(AssignmentForm, self).__init__(*args, **kwargs)
        choices=[(assignment.assignment_id, assignment.assignment_name) for assignment in Assignment.objects.filter(course__course_id=course_canvas_id, active=True)]
        self.fields['assignment'] = forms.ChoiceField(
            choices=choices
            )            
        self.fields['reason'] = forms.CharField(
            widget=forms.Textarea
            )

        student = Student.objects.get(sis_user_id__contains=str(student_id))

        # get current datetime
        now = datetime.datetime.now()

        # get Date objects that are active and have a start date before now and a finish date after now
        date = Date.objects.get(start__lte=now, finish__gte=now)
        print("Dates:", date.start, date.finish, now)

        # get count of approved extensions for the student that are within the current date range and have no files attached
        count = Extension.objects.filter(student=student, extension_deadline__lte=date.finish, extension_deadline__gte=date.start, approved=True, files__exact="").count()

        print("count:", count)

        if count <2:
            file_required = False
            file_help_text = "If you choose not to upload evidence (e.g. a medical note/certificate) then this application will be approved automatically and you will use one of your available extensions."
        else:
            file_required = True
            file_help_text = "You have already had two ELPs approved for the current period. You must upload evidence (e.g. a medical note/certificate) to support your application."


        self.fields['files'] = forms.FileField(
        required=file_required,
        label="Evidence upload",
        help_text=file_help_text,

        )
        
  












    

 


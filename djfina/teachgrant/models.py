from django.db import models

# Create your models here.
class TeachGrant(models.Model):
    student_name = models.CharField(max_length=50)
    carthage_id = models.CharField(max_length=7)
    TEACH_grant_eligible_program_of_study = models.CharField(max_length=30)
    GPA_REQUIREMENT_CHOICES = (
        ('continuing undergrad and grad students', 'Continuing Undergrad And Graduate Students'),
        ('new freshmen students', 'New Freshmen Students'),
        ('new undergrad transfer students', 'New Undergrad Transfer Students'),
        ('new graduate students', 'New Graduate Students'),
    )
    gpa_requirements = models.CharField(max_length=40, choices=GPA_REQUIREMENT_CHOICES,default='continuing undergrad and grad students')
    undergrad_enrolled_in_grant_eligible_program = models.BooleanField()
    grad_enrolled_in_grant_eligible_program = models.BooleanField()
    filed_fafsa = models.BooleanField()
    understand_conditions = models.BooleanField()
    submit_date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.student_name

class ProxyTeachGrant(TeachGrant):
    class Meta:
        proxy = True
        app_label = 'Financial_Aid'
        verbose_name = 'Teach Grant Form'


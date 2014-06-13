from django.db import models

# Create your models here.
class TeachGrant(models.Model):
    student_name = models.CharField(max_length=50, verbose_name='Student Name')
    carthage_id = models.CharField(max_length=7, verbose_name='Carthage ID')
    TEACH_grant_eligible_program_of_study = models.CharField(max_length=30,
                                                             verbose_name='Indicate your TEACH grant eligible program of study')
    GPA_REQUIREMENT_CHOICES = (
        ('continuing undergrad and grad students', 'Continuing Undergrad And Graduate Students'),
        ('new freshmen students', 'New Freshmen Students'),
        ('new undergrad transfer students', 'New Undergrad Transfer Students'),
        ('new graduate students', 'New Graduate Students'),
    )
    gpa_requirements = models.CharField(max_length=40,
                                        choices=GPA_REQUIREMENT_CHOICES,
                                        default='continuing undergrad and grad students',
                                        verbose_name='Current status')
    
    undergrad_enrolled_in_grant_eligible_program =\
    models.BooleanField(verbose_name="Undergraduate enrolled in a grant-eligible program")
    
    grad_enrolled_in_grant_eligible_program =\
    models.BooleanField(verbose_name='Graduate enrolled in a grant-eligible program')
    
    filed_fafsa = models.BooleanField(verbose_name='I agree with the FAFSA conditions')
    
    understand_conditions = models.BooleanField(verbose_name=\
    'I understand that if I am awarded a Federal TEACH Grant, I must do the following')
    
    submit_date = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.student_name

class ProxyTeachGrant(TeachGrant):
    class Meta:
        proxy = True
        app_label = 'Financial_Aid'
        verbose_name = 'Teach Grant Form'


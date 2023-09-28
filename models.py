import datetime

from rest_framework.request import Request
from django.utils.functional import cached_property
from django.conf import settings
from django.db import models
from tinymce.models import HTMLField

from sapp.models import AbstractUser, SM, FileField, ImageField, AbstractSettings, AbstractType, cls


class Settings(AbstractSettings):

    ATTENDANCE_STATUSES = ("P", "A", "HD", "H", "L", "DD")

    class Meta(SM.Meta):
        verbose_name = "SAPP HR Settings"
        verbose_name_plural = "SAPP HR Settings"

    work_days = models.CharField(max_length=7, default="012345")
    half_work_days = models.CharField(max_length=7, default="6")
    month_start_day = models.CharField(max_length=2, default="27")
    month_end_day = models.CharField(max_length=2, default="26")

    def __str__(self):
        return "Sapp HR Settings"


class Department(SM):
    icon = "fas fa-user-tag"
    list_field_names = ("id", "name", "supervisor")
    detail_field_names = ("id", "name", "supervisor", "about")
    api_methods = ("get_department_contract_stats_api",)

    name = models.CharField(max_length=256)
    about = models.TextField(max_length=512)
    supervisor: models.ForeignKey[SM] = models.ForeignKey("sapp_hr.Employee", on_delete=models.SET_NULL, blank=True, null=True)
    
    @classmethod
    def get_department_contract_stats_api(cls, request: Request, kwds: dict):
        return cls.get_department_contract_stats()

    @classmethod
    def get_department_contract_stats(cls):
        data = {}
        for d in Department.objects.all():
            data[f"{d.name}"] = Contract.objects.filter(department_id=d.pk, expire_date=None).count()
        return data

    def __str__(self):
        return self.name


class Grade(SM):
    icon = "fas fa-dollar-sign"
    list_field_names = ("id", "name", "salary", )
    detail_field_names = list_field_names + ("about", )
    api_methods = ("get_grade_contract_stats_api", "get_grade_salaries_stats_api", "get_salaries_stats_api")

    name = models.CharField(max_length=256)
    salary = models.DecimalField(max_digits=16, decimal_places=2)
    about = models.TextField(max_length=512)
    
    @classmethod
    def get_grade_contract_stats_api(cls, request: Request, kwds: dict):
        return cls.get_grade_contract_stats()

    @classmethod
    def get_grade_contract_stats(cls):
        data = {}
        for i in Grade.objects.all():
            data[f"{i.name}"] = Contract.objects.filter(grade_id=i.pk, expire_date=None).count()
        return data
    
    @classmethod
    def get_grade_salaries_stats_api(cls, request: Request, kwds: dict):
        return cls.get_grade_salaries_stats()

    @classmethod
    def get_grade_salaries_stats(cls):
        data = {}
        for i in Grade.objects.all():
            data[f"{i.name}"] = sum([c[0] for c in Contract.objects.filter(grade_id=i.pk, expire_date=None).values_list("grade__salary").order_by("grade__salary")])
        return data
    
    @classmethod
    def get_salaries_stats_api(cls, request: Request, kwds: dict):
        return cls.get_salaries_stats()

    @classmethod
    def get_salaries_stats(cls):
        data = {}
        for i in Grade.objects.all():
            data[f"{i.name}"] = i.salary
        return data

    def __str__(self):
        return self.name


class Skill(SM):
    icon = "fas fa-certificate"
    list_field_names = ("id", "name",  "about")
    detail_field_names = list_field_names

    name = models.CharField(max_length=256)
    about = models.TextField(max_length=512)

    def __str__(self):
        return self.name


class Rank(SM):
    icon = "fas fa-sort-amount-up"
    list_field_names = ("id", "name")
    detail_field_names = list_field_names + ("about", )
    api_methods = ("get_rank_contract_stats_api",)

    name = models.CharField(max_length=256)
    about = models.TextField(max_length=512)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_rank_contract_stats_api(cls, request: Request, kwds: dict):
        return cls.get_rank_contract_stats()

    @classmethod
    def get_rank_contract_stats(cls):
        data = {}
        for i in Grade.objects.all():
            data[f"{i.name}"] = Contract.objects.filter(rank_id=i.pk, expire_date=None).count()
        return data


class Award(SM):
    icon = "fas fa-award"
    list_field_names = ("id", "name", "image", "award_type")
    detail_field_names = list_field_names

    TYPES = ("Annual", "Training", "Once Off", "Achievement")

    name = models.CharField(max_length=128)
    about = HTMLField()
    image = ImageField()
    award_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*TYPES))

    def __str__(self):
        return self.name


class Target(SM):
    icon = "fas fa-hiking"
    list_field_names = ("id", "name", "target_type", "max_score")
    detail_field_names = list_field_names + ("about", )
    filter_field_names = ("target_type",)

    TYPES = ("Educational", "Productivity", "Descipline")

    name = models.CharField(max_length=128)
    about = HTMLField()
    target_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*TYPES))
    max_score = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name


class Course(SM):
    icon = "fas fa-user-graduate"
    list_field_names = ("id", "name", "image", "course_type")
    detail_field_names = list_field_names + ("about", ) + SM.sm_meta_field_names

    TYPES = ("Annual", "Training", "Once Off", "Achievement", "Drill")

    name = models.CharField(max_length=128)
    about = HTMLField()
    course_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*TYPES))

    def __str__(self):
        return self.name


class Ceremony(SM):
    icon = "fas fa-calendar-alt"
    list_field_names = ("id", "name", "start_date")
    has_notes = True
    has_attachments = True

    TYPES = ("Annual", "Once Off", "Jubilee")

    name = models.CharField(max_length=128)
    about = HTMLField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    ceremony_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*TYPES))

    def __str__(self):
        return f"{self.sm_str} {self.name} - {self.start_date}"


class Person(SM):
    '''Employee/Applicant'''
    icon = "fas fa-user-tie"
    cols_css_class = cls.COL_MD6
    list_field_names = ("id", "full_name", "id_number", "gender", "employment_type")
    has_attachments = True
    has_notes = True

    EMPLOYMENT_TYPES = ("Pearmanent", "Temporal", "Contract", "Consultant", "Industrial Attachment")
    ID_DOCUMENTS = ("License", "Passport", "National ID", "Other")

    class Meta(SM.Meta):
        abstract = True

    user: models.ForeignKey[AbstractUser] = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    id_document = models.CharField(max_length=128, choices=SM.iter_as_choices(*ID_DOCUMENTS))
    id_number = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=SM.iter_as_choices("M", "F", "O"))
    DOB = models.DateField()
    employment_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*EMPLOYMENT_TYPES))
    resume = FileField(upload_to="personnel", blank=True, null=True, serialize=cls.CLS_COL_12)
    id_document_file = FileField(upload_to="personnel", blank=True, null=True, serialize=cls.CLS_COL_12)
    proof_of_residence_file = FileField(upload_to="personnel", blank=True, null=True, serialize=cls.CLS_COL_12)
    address = models.TextField(max_length=128, blank=True, null=True, serialize=cls.CLS_COL_12)
    about = HTMLField(blank=True, null=True, serialize=cls.CLS_COL_12)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.sm_str}: {self.full_name}"
    
    def set_user_fields(self):
        if self.user:
            for field in ("first_name", "last_name", "email", "phone", "gender", "DOB"):
                if not getattr(self, field):
                    setattr(self, field, getattr(self.user, field))
    
    def save(self, *args, **kwargs):
        self.set_user_fields()
        super().save(*args, **kwargs)
    
    @property
    def age(self):
        return (datetime.date.today() - self.DOB).days // 365


class Employee(Person):
    icon = "fas fa-user-tie"
    queryset_names = ("contracts", "awards", "targets", "skills")

    
    supervisor: models.ForeignKey[SM] = models.ForeignKey("sapp_hr.Employee", on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def contracts(self):
        return Contract.objects.filter(employee=self)

    @property
    def awards(self):
        return EmployeeAward.objects.filter(employee=self)

    @property
    def targets(self):
        return EmployeeTarget.objects.filter(employee=self)

    @property
    def skills(self):
        return EmployeeSkill.objects.filter(employee=self)
    
    def get_str_prefix(self):
        return "EMP"


class EmployeeAward(SM):
    icon = "fas fa-trophy"
    cols_css_class = cls.COL_MD6
    list_field_names = ("id", "employee", "award", "ceremony", "date")
    filter_field_names = ("employee", "award", "ceremony")

    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    ceremony = models.ForeignKey(Ceremony, on_delete=models.SET_NULL, blank=True, null=True)
    about = HTMLField()

    def __str__(self):
        return f"{self.sm_str} {self.employee} {self.award}"
    
    @property
    def list_url(self):
        return (self.employee_id and self.employee.detail_url) or super().list_url


class EmployeeTarget(SM):
    icon = "fas fa-trophy"
    cols_css_class = "col-md-4"
    list_field_names = ("id", "employee", "target", "date", "score")
    filter_field_names = ("employee", "target")
    
    has_notes = True
    has_attachments = True

    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    due = models.DateField()
    score = models.PositiveIntegerField(default=0)
    comments = HTMLField(max_length=128)

    def __str__(self):
        return f"{self.sm_str} {self.employee} {self.target}"
    
    @property
    def list_url(self):
        return (self.employee_id and self.employee.detail_url) or super().list_url


class EmployeeSkill(SM):
    icon = "fas fa-id-badge"
    cols_css_class = "col-md-4"
    list_field_names = ("id", "employee", "skill", "score")
    filter_field_names = ("employee", "skill")
    
    has_notes = True
    has_attachments = True

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    comments = HTMLField(max_length=128, serialize=cls.CLS_COL_12)

    def __str__(self):
        return f"{self.sm_str} {self.employee} {self.skill}"
    
    @property
    def list_url(self):
        return (self.employee_id and self.employee.detail_url) or super().list_url


class Contract(SM):
    icon = "fas fa-file-signature"
    cols_css_class = cls.COL_LG6
    list_field_names = ("id", "employee", "position", "department")
    filter_field_names = ("employee", "department", "grade", "rank", "work_type", "termination_reason", "position")
    api_methods = ("get_contract_work_types_stats_api", "get_contract_termination_reasons_stats_api")

    has_attachments = True
    has_notes = True
    confirm_delete = True

    WORK_TYPES = ("On Demand", "Fulltime", "Remote", "Hybrid")
    TERMINATION_REASONS = ("Suspenision", "Death", "Fired", "Promotion", "Departments Switch", "Demotion", "Career Break")

    full_name = models.CharField(max_length=256, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    position = models.CharField(max_length=256)
    start_date = models.DateField()
    expire_date = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT, blank=True, null=True)
    work_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*WORK_TYPES))
    application_letter = FileField(upload_to="sapp_hr_contract_application_letters", blank=True, null=True)
    file = FileField(upload_to="sapp_hr_contract_files", blank=True, null=True)
    image = ImageField(upload_to="sapp_hr_contract_images", blank=True, null=True)
    salary = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    working_hours = models.FloatField(default=8)
    default_attendance_status = models.CharField(max_length=2, choices=SM.iter_as_choices(*Settings.ATTENDANCE_STATUSES), default="P")
    default_check_in = models.TimeField(blank=True, null=True)
    default_check_out = models.TimeField(blank=True, null=True)
    default_weekly_hours = models.PositiveIntegerField(default=40)
    details = models.TextField(max_length=512, blank=True, null=True)
    termination_explanation = models.TextField(max_length=1024, blank=True, null=True)
    termination_reason = models.CharField(max_length=128, blank=True, null=True, choices=SM.iter_as_choices(*TERMINATION_REASONS))

    def __str__(self):
        return f"{self.sm_str}: {self.full_name}"
    
    @classmethod
    def get_contract_work_types_stats_api(cls, request: Request, kwds: dict):
        return cls.get_contract_work_types_stats()

    @classmethod
    def get_contract_work_types_stats(cls):
        data = {}
        for  i in cls.WORK_TYPES:
            data[i] = Contract.objects.filter(work_type=i).count()
        return data
    
    @classmethod
    def get_contract_termination_reasons_stats_api(cls, request: Request, kwds: dict):
        return cls.get_contract_termination_reasons_stats()

    @classmethod
    def get_contract_termination_reasons_stats(cls):
        data = {}
        for  i in cls.TERMINATION_REASONS:
            data[i] = Contract.objects.filter(termination_reason=i).count()
        return data
    
    def set_full_name(self):
        if not self.full_name:
            self.full_name = self.employee.full_name
    
    def save(self, *args, **kwargs):
        self.set_full_name()
        return super().save(*args, **kwargs)


class Remuneration(SM):
    icon = "fas fa-money-check-alt"
    list_field_names = ("id", "contract", "date", "amount", "purpose")
    filter_field_names = ("date", "contract", "purpose", "amount")
    PURPOSES = ("Health Incentive", "Overtime Incentive", "Holiday Incentive", "Bonus", "Reward", "Wage", "Medical")

    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    about = models.TextField(max_length=512)
    purpose = models.CharField(max_length=32, choices=SM.iter_as_choices(*PURPOSES))


class Deduction(SM):
    icon = "fas fa-funnel-dollar"
    list_field_names = ("id", "remuneration", "amount", "purpose")
    filter_field_names = ("remuneration", "purpose", "amount")
    PURPOSES = ("Half Days and Absentees", "Poor Perfomance", "Budget Constraints", "Penalty", "Petty")

    remuneration = models.ForeignKey(Remuneration, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=16, decimal_places=2)
    about = models.TextField(max_length=512)
    purpose = models.CharField(max_length=32, choices=SM.iter_as_choices(*PURPOSES))


class Vacancy(SM):
    icon = "fas fa-sticky-note"
    list_field_names = ("id", "title", "grade", "rank", "department", "work_type", "positions", "expired")
    filter_field_names = ("grade", "rank", "department", "work_type")
    has_attachments = True
    has_notes = True

    class Meta(SM.Meta):
        verbose_name_plural = "Vacancies"

    title = models.CharField(max_length=128)
    description = HTMLField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT)
    work_type = models.CharField(max_length=32, choices=SM.iter_as_choices(*Contract.WORK_TYPES))
    file = FileField(upload_to="sapp_hr_contract_files")
    expire_date = models.DateField()
    positions = models.PositiveIntegerField(default=0)

    @property
    def expired(self):
        return self.now.date() < self.expire_date
    
    def __str__(self):
        return f"{self.title} - {self.expire_date}"


class Applicant(Person):
    icon = "fas fa-male"
    list_field_names = Person.list_field_names + ("vacancy", "status")
    filter_field_names = Person.filter_field_names + ("vacancy", "status")

    STATUSES = ("open", "reviewed", "closed", "rejected", "passed")

    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=32, choices=SM.iter_as_choices(*STATUSES), default="open")


class Leave(SM):
    icon = "fas fa-file-alt"
    PURPOSES = ("Sick", "Emergency", "Suspension", "Holiday")

    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()
    reason = models.TextField(max_length=512)
    purpose = models.CharField(max_length=32, choices=SM.iter_as_choices(*PURPOSES))
    file = FileField(upload_to="leaves")

    @property
    def duration(self):
        return (self.end - self.start).days or 1


# class Shift(SM):
#     icon = "fas fa-calendar-week"

class JobType(AbstractType):
    pass


class Job(SM):
    icon = "fas fa-hands"
    cols_css_class = cls.COL_12MD6LG4
    list_field_names = ("id", "manager", "title", "creation_timestamp")
    filter_field_names = ("manager", "job_type", "rating", "title")
    queryset_names = ("tasks", )
    str_prefix = "JOB"

    title = models.CharField(max_length=128, serialize=cls.CLS_COL_12)
    manager = models.ForeignKey(Contract, on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, on_delete=models.PROTECT)
    rating = models.PositiveIntegerField(choices=SM.iter_as_choices(*range(11)), blank=True, null=True)
    due = models.DateTimeField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    estimated_hours = models.FloatField(blank=True, null=True)
    details = HTMLField(blank=True, null=True, serialize=cls.CLS_COL_12)
    notes = models.TextField(max_length=512, blank=True, null=True, serialize=cls.CLS_COL_12)

    def __str__(self):
        return f"{self.sm_str} {self.title}"
    
    @cached_property
    def tasks(self):
        return Task.objects.filter(job_id=self.pk)


class Task(SM):
    icon = "fas fa-tasks"
    list_field_names = ("id", "assignee", "job", "title", "creation_timestamp")

    assignee = models.ForeignKey(Contract, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=SM.iter_as_choices(*range(11)), blank=True, null=True)
    details = HTMLField(blank=True, null=True)
    notes = models.TextField(max_length=512, blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    estimated_hours = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.sm_str} {self.title}"
    
    @property
    def list_url(self):
        return (self.job_id and self.job.detail_url) or super().list_url


class Attendance(SM):
    icon = "fas fa-calendar-check"
    cols_css_class = cls.CLS_COL_12MD6LG4
    api_methods = ("create_register_for_date_api", "get_register_for_date_api", "create_update_attendance_api", "get_register_data_api")
    list_field_names = ("id", "contract", "date", "status", "check_in", "check_out")
    filter_field_names = ("status", "date", "contract")

    per_page = 100

    class Meta(SM.Meta):
        unique_together = (("contract", "date"),)

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=2, choices=SM.iter_as_choices(*Settings.ATTENDANCE_STATUSES))
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.sm_str} {self.contract} - {self.date}"
    
    @property
    def hours_worked(self):
        if not (self.check_in and self.check_out):
            return 0
        return round((self.check_out - self.check_in).seconds / 3600, 2)
    
    # @property
    # def list_url(self):
    #     return self.contract.detail_url
    
    @classmethod
    def create_register_for_date(cls, date):
        already_saved = [i[0] for i in Attendance.objects.filter(date=date).values_list("contract_id")]
        active_contracts = Contract.objects.filter(
            models.Q(start_date__lte=date),
            models.Q(expire_date__gte=date) | models.Q(expire_date=None)
        ).exclude(id__in=already_saved)
        attendances:list[Attendance] = []
        for contract in active_contracts:
            attendances.append(
                Attendance(
                    contract = contract,
                    date = date,
                    status = contract.default_attendance_status,
                )
            )
        Attendance.objects.bulk_create(attendances)
        return len(attendances)
    
    @classmethod
    def create_register_for_date_api(cls, request: Request, rkwds: dict):
        return cls.create_register_for_date(date=datetime.date.fromisoformat(request.data["date"]))
    
    @classmethod
    def get_register_for_date_api(cls, request: Request, rkwds: dict):
        todays_attendances = Attendance.objects.filter(date=datetime.date.fromisoformat(request.data["date"])).select_related("contract")
        attendances = [
            {
                "contract_str": str(i.contract),
                "contract": i.contract.pk,
                "attendance": i.pk,
                "status": i.status,
                "check_in": i.check_in,
                "check_out": i.check_out,
            } for i in todays_attendances
        ]
        return {
            "attendances": attendances,
            "attendance_status_choices": Settings.ATTENDANCE_STATUSES
        }
    
    @classmethod
    def create_update_attendance_api(cls, request: Request, rkwds: dict):
        data = request.data
        pk = data.get("attendance")
        cleaned_data = {
            "contract_id": int(data["contract"]),
            "status": data["status"],
            "check_in": data["check_in"] or None,
            "check_out": data["check_out"] or None,
        }
        print(cleaned_data)
        if pk:
            Attendance.objects.filter(id=int(pk)).update(**cleaned_data)
        else:
            Attendance.objects.create(**cleaned_data)
    
    @classmethod
    def get_register_data_api(cls, request: Request, rkwds: dict):
        return cls.get_register_data(
            start_date=datetime.datetime.fromisoformat(request.data["start_date"]),
            end_date=datetime.datetime.fromisoformat(request.data["end_date"])
        )

    @classmethod
    def get_register_data(cls, start_date: datetime.date, end_date: datetime.date):
        header, body = {}, {}
        end_date = end_date + datetime.timedelta(days=1)
        active_contracts = Contract.objects.filter(models.Q(start_date__lt=end_date),
            models.Q(expire_date__gt=start_date) | models.Q(expire_date=None))
        for i in range((end_date - start_date).days):
            date = start_date + datetime.timedelta(days=i)
            is_work_day = date.weekday() < 5
            header[date.__str__()] = {
                "date": date,
                "is_work_day": is_work_day
            }
        for contract in active_contracts:
            cntrct = {
                "id": contract.pk,
                "employee": contract.employee.__str__(),
                "str": str(contract)
            }
            hours_worked = 0
            attendances = []
            for (k, v) in header.items():
                if not v["is_work_day"]:
                    attendances.append("W")
                    continue
                att = Attendance.objects.filter(contract_id=contract.pk, date=v["date"]).first()
                if att:
                    attendances.append(att.status)
                    hours_worked += att.hours_worked
                else:
                    attendances.append("X")
            days_absent = attendances.count("A")
            double_days = attendances.count("DD")
            days_present = attendances.count("P") + double_days
            days_worked = attendances.count("P") + (double_days*2)
            leave_days = attendances.count("L")
            blank_days = attendances.count("X")
            weekend_days = attendances.count("W")
            attendances_count = len(attendances)
            try:
                percentage = int(((days_worked)/(attendances_count-(leave_days+blank_days+weekend_days)))*100)
            except ZeroDivisionError:
                percentage = 0
            body[str(contract.pk)] = {
                "contract": cntrct,
                "attendances": attendances,
                "attendances_count": attendances_count,
                "days_absent": days_absent,
                "days_present": days_present,
                "days_worked": days_worked,
                "leave_days": leave_days,
                "blank_days": blank_days,
                "hours_worked": hours_worked,
                "percentage": percentage
            }
        return dict(header=header, body=body)
    
    @classmethod
    def get_list_actions_links(cls, request):
        return [
            {
                "title": "Daily Register",
                "link": f"/{settings.SAPP_URL}/sapp_hr/mark-register/"
            },
            {
                "title": "Attendance Register",
                "link": f"/{settings.SAPP_URL}/sapp_hr/attendance-register/"
            },
        ]
    
    def set_default_check_in_out(self):
        self.check_in = self.check_in or self.contract.default_check_in
        self.check_out = self.check_out or self.contract.default_check_out
    
    def save(self, *args, **kwargs):
        self.set_default_check_in_out()
        super().save(*args, **kwargs)

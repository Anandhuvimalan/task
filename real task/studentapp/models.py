from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.DO_NOTHING)
    materials_provided = models.ManyToManyField(Material, blank=True, null=True)

    def __str__(self):
        return self.name
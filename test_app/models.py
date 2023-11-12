from django.db import models


TEST_CHOICES = (
    ("programing", "PROGRAMING"),
    ("science", "SCIENCE"),
)


class Test(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(choices=TEST_CHOICES, max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name



class Questions(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.question

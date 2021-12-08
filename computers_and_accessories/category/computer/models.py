from django.db import models

from base_models.bm_computers_and_accessories.models import BaseModelComputerAndAccessories
from department.models import Department
from category.models import Category


class Computer(BaseModelComputerAndAccessories):
    screen_size = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100, default='Intel')
    operating_system = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images_computer/',
                              default='computer_and_accessories_images/default.png')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)

    objects = models.Manager()

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'Computer'

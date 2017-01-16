import django_tables2 as tables
from families.models import Meal

class MealTable(tables.Table):

    class Meta:
        model = Meal
        
    time = tables.Column(accessor='time')

from django.db import models

# Create your models here.
class Food(models.Model):
  name = models.CharField(verbose_name="Food Name", max_length=200)
  calories = models.FloatField(verbose_name="Calories (kcal)")
  total_fat = models.FloatField(verbose_name="Total Fat (g)")
  saturated_fat = models.FloatField(verbose_name="Saturated Fat (g)")
  cholesterol = models.FloatField(verbose_name="Cholesterol (mg)")
  sodium = models.FloatField(verbose_name="Sodium (mg)")
  total_carbohydrate = models.FloatField(verbose_name="Total Carbohydrate (g)")
  dietary_fibre = models.FloatField(verbose_name="Dietary Fibre (g)")
  sugar = models.FloatField(verbose_name="Sugar (g)")
  protein = models.FloatField(verbose_name="Protein (g)")
  
  def __str__(self):
    return self.name
  
class Meal(models.Model):
  BREAKFAST = 1
  LUNCH = 2
  MEAL_TIME_TYPES = (
    (BREAKFAST, "Breakfast"),
    (LUNCH, "Lunch") 
  )	
  food = models.ForeignKey(Food, verbose_name="Food",on_delete = models.CASCADE)
  serving_size = models.IntegerField(verbose_name="Serving Size")
  meal_time = models.IntegerField(verbose_name="Meal Time", choices=MEAL_TIME_TYPES)
  
  def get_total_calories(self):
    return self.serving_size*self.food.calories
  def get_total_total_fat(self):
    return self.serving_size*self.food.total_fat
  def get_total_saturated_fat(self):
    return self.serving_size*self.food.saturated_fat
  def get_total_cholesterol(self):
    return self.serving_size*self.food.cholesterol
  def get_total_sodium(self):
    return self.serving_size*self.food.sodium
  def get_total_total_carbohydrate(self):
    return self.serving_size*self.food.total_carbohydrate
  def get_total_dietary_fibre(self):
    return self.serving_size*self.food.dietary_fibre
  def get_total_sugar(self):
    return self.serving_size*self.food.sugar
  def get_total_protein(self):
    return self.serving_size*self.food.protein
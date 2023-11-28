from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('imgUrl', models.CharField(max_length=200)),
                ('calorie', models.FloatField()),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=30)),
                ('foodImgUrl', models.CharField(max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('calorie', models.FloatField()),
                ('natrium', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('imgUrl', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_figure', models.FloatField()),
                ('measurement_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userexercise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.center')),
            ],
        ),
        migrations.CreateModel(
            name='MealAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealamount', to='main.food')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mealamount', to='main.meal')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='main.foodcategory'),
        ),
        migrations.CreateModel(
            name='ExerciseAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exerciseamount', to='main.exercisecategory')),
                ('userexercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exerciseamount', to='main.userexercise')),
            ],
        ),
        migrations.CreateModel(
            name='BloodPressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField()),
                ('measurement_date', models.DateField()),
                ('measurement_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloodpressure', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

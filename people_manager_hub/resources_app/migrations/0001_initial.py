# Generated by Django 2.1.5 on 2020-01-09 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_img', models.URLField()),
                ('website_img', models.URLField()),
                ('document_img', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Design assets',
            },
        ),
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.EmailField(max_length=70)),
            ],
            options={
                'verbose_name_plural': 'Global settings',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=256)),
                ('priority', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5, help_text='Use this field to determine relative position of this module on the page. Lower numbers appear earlier on page.')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources_app.Resource')),
            ],
            bases=('resources_app.resource',),
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources_app.Page')),
                ('instruction_title', models.CharField(max_length=100)),
                ('instruction_text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Home page',
            },
            bases=('resources_app.page',),
        ),
        migrations.CreateModel(
            name='ResourcesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources_app.Page')),
                ('banner_image', models.URLField()),
                ('animated_gif', models.URLField()),
            ],
            bases=('resources_app.page',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources_app.Resource')),
            ],
            bases=('resources_app.resource',),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources_app.Resource')),
            ],
            bases=('resources_app.resource',),
        ),
        migrations.AddField(
            model_name='resourcemodule',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resources_app.Page'),
        ),
        migrations.AddField(
            model_name='resourcemodule',
            name='resources',
            field=models.ManyToManyField(to='resources_app.Resource'),
        ),
    ]

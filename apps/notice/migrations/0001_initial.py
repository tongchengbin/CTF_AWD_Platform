# Generated by Django 2.1.7 on 2019-08-05 20:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='公告时间')),
                ('notice_title', models.TextField(null=True, verbose_name='公告题目')),
                ('notice_content', models.TextField(null=True, verbose_name='公告内容')),
                ('notice_competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competition_name1', to='competition.CompetitionProfile', verbose_name='比赛名称')),
            ],
            options={
                'verbose_name': '比赛公告',
                'verbose_name_plural': '比赛公告',
                'ordering': ['-notice_time'],
            },
        ),
    ]

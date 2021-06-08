# Generated by Django 2.2.18 on 2021-02-09 04:21

from django.db import migrations, models
import django.utils.timezone
import django_fsm
from jsonfield.fields import JSONField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JSONWebhookData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django_fsm.FSMIntegerField(choices=[(0, 'New'), (1, 'Processing'), (2, 'Processed'), (-1, 'Error')], default=0, protected=True)),
                ('source', models.GenericIPAddressField(null=True)),
                ('received', models.DateTimeField(default=django.utils.timezone.now)),
                ('headers', JSONField()),
                ('body', models.BinaryField()),
                ('content', JSONField(null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='f_name',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='l_name',
            new_name='username',
        ),
    ]

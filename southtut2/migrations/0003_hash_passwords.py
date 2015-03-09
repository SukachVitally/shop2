# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        import random, hashlib, string
        for user in orm.User.objects.all():
            user.password_salt = "".join([random.choice(string.ascii_letters) for i in range(8)]).encode('utf-8')
            user.password = user.password.encode('utf-8')
            user.password_hash = hashlib.sha1(user.password_salt + user.password).hexdigest()
            user.save()

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

    models = {
        'southtut2.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '40'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '8'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['southtut2']
    symmetrical = True

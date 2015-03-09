# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.dances_whenever_able'
        db.add_column('southtut_knight', 'dances_whenever_able',
                      self.gf('django.db.models.fields.BooleanField')(default=datetime.datetime(2015, 3, 9, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.dances_whenever_able'
        db.delete_column('southtut_knight', 'dances_whenever_able')


    models = {
        'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['southtut']
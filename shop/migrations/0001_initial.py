# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductGroup'
        db.create_table('shop_productgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('shop', ['ProductGroup'])

        # Adding model 'Product'
        db.create_table('shop_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('shop', ['Product'])

        # Adding model 'ProductGroupRelation'
        db.create_table('shop_productgrouprelation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.ProductGroup'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'])),
        ))
        db.send_create_signal('shop', ['ProductGroupRelation'])

        # Adding model 'ProductInfoType'
        db.create_table('shop_productinfotype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('shop', ['ProductInfoType'])

        # Adding model 'ProductInfo'
        db.create_table('shop_productinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.ProductInfoType'])),
        ))
        db.send_create_signal('shop', ['ProductInfo'])


    def backwards(self, orm):
        # Deleting model 'ProductGroup'
        db.delete_table('shop_productgroup')

        # Deleting model 'Product'
        db.delete_table('shop_product')

        # Deleting model 'ProductGroupRelation'
        db.delete_table('shop_productgrouprelation')

        # Deleting model 'ProductInfoType'
        db.delete_table('shop_productinfotype')

        # Deleting model 'ProductInfo'
        db.delete_table('shop_productinfo')


    models = {
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'shop.productgroup': {
            'Meta': {'object_name': 'ProductGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'shop.productgrouprelation': {
            'Meta': {'object_name': 'ProductGroupRelation'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.ProductGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"})
        },
        'shop.productinfo': {
            'Meta': {'object_name': 'ProductInfo'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.ProductInfoType']"})
        },
        'shop.productinfotype': {
            'Meta': {'object_name': 'ProductInfoType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['shop']
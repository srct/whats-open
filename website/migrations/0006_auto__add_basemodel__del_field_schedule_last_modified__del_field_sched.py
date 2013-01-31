# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseModel'
        db.create_table('website_basemodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('website', ['BaseModel'])

        # Deleting field 'Schedule.last_modified'
        db.delete_column('website_schedule', 'last_modified')

        # Deleting field 'Schedule.id'
        db.delete_column('website_schedule', 'id')

        # Adding field 'Schedule.basemodel_ptr'
        db.add_column('website_schedule', 'basemodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.BaseModel'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'OpenTime.last_modified'
        db.delete_column('website_opentime', 'last_modified')

        # Deleting field 'OpenTime.id'
        db.delete_column('website_opentime', 'id')

        # Adding field 'OpenTime.basemodel_ptr'
        db.add_column('website_opentime', 'basemodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.BaseModel'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Restaurant.last_modified'
        db.delete_column('website_restaurant', 'last_modified')

        # Deleting field 'Restaurant.id'
        db.delete_column('website_restaurant', 'id')

        # Adding field 'Restaurant.basemodel_ptr'
        db.add_column('website_restaurant', 'basemodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['website.BaseModel'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'BaseModel'
        db.delete_table('website_basemodel')

        # Adding field 'Schedule.last_modified'
        db.add_column('website_schedule', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Schedule.id'
        db.add_column('website_schedule', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'Schedule.basemodel_ptr'
        db.delete_column('website_schedule', 'basemodel_ptr_id')

        # Adding field 'OpenTime.last_modified'
        db.add_column('website_opentime', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OpenTime.id'
        db.add_column('website_opentime', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'OpenTime.basemodel_ptr'
        db.delete_column('website_opentime', 'basemodel_ptr_id')

        # Adding field 'Restaurant.last_modified'
        db.add_column('website_restaurant', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Restaurant.id'
        db.add_column('website_restaurant', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Deleting field 'Restaurant.basemodel_ptr'
        db.delete_column('website_restaurant', 'basemodel_ptr_id')


    models = {
        'website.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'website.opentime': {
            'Meta': {'object_name': 'OpenTime', '_ormbases': ['website.BaseModel']},
            'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'end_day': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'open_times'", 'to': "orm['website.Schedule']"}),
            'start_day': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'website.restaurant': {
            'Meta': {'object_name': 'Restaurant', '_ormbases': ['website.BaseModel']},
            'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'main_schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_main'", 'to': "orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'special_schedules': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_special'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Schedule']"})
        },
        'website.schedule': {
            'Meta': {'object_name': 'Schedule', '_ormbases': ['website.BaseModel']},
            'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valid_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valid_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
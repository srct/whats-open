# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Schedule.last_modified'
        db.add_column('website_schedule', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'OpenTime.last_modified'
        db.add_column('website_opentime', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 28, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Restaurant.last_modified'
        db.add_column('website_restaurant', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 1, 28, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Schedule.last_modified'
        db.delete_column('website_schedule', 'last_modified')

        # Deleting field 'OpenTime.last_modified'
        db.delete_column('website_opentime', 'last_modified')

        # Deleting field 'Restaurant.last_modified'
        db.delete_column('website_restaurant', 'last_modified')


    models = {
        'website.opentime': {
            'Meta': {'object_name': 'OpenTime'},
            'end_day': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'open_times'", 'to': "orm['website.Schedule']"}),
            'start_day': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'website.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'main_schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_main'", 'to': "orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'special_schedules': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_special'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Schedule']"})
        },
        'website.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valid_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valid_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
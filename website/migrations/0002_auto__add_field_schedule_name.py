# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Schedule.name'
        db.add_column('website_schedule', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Southside Schedule', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Schedule.name'
        db.delete_column('website_schedule', 'name')


    models = {
        'website.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainSchedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_main'", 'to': "orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'specialSchedules': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_special'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Schedule']"})
        },
        'website.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'dateValidEnd': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dateValidStart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'friClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'friOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'monOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'satClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'satOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sunOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thuClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thuOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tueClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tueOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wedClose': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wedOpen': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
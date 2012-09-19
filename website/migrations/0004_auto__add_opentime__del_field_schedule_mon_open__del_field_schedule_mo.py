# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OpenTime'
        db.create_table('website_opentime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='open_times', to=orm['website.Schedule'])),
            ('start_day', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_day', self.gf('django.db.models.fields.IntegerField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('website', ['OpenTime'])

        # Deleting field 'Schedule.mon_open'
        db.delete_column('website_schedule', 'mon_open')

        # Deleting field 'Schedule.mon_close'
        db.delete_column('website_schedule', 'mon_close')

        # Deleting field 'Schedule.sat_open'
        db.delete_column('website_schedule', 'sat_open')

        # Deleting field 'Schedule.fri_close'
        db.delete_column('website_schedule', 'fri_close')

        # Deleting field 'Schedule.sat_close'
        db.delete_column('website_schedule', 'sat_close')

        # Deleting field 'Schedule.fri_open'
        db.delete_column('website_schedule', 'fri_open')

        # Deleting field 'Schedule.sun_open'
        db.delete_column('website_schedule', 'sun_open')

        # Deleting field 'Schedule.tue_close'
        db.delete_column('website_schedule', 'tue_close')

        # Deleting field 'Schedule.thu_open'
        db.delete_column('website_schedule', 'thu_open')

        # Deleting field 'Schedule.wed_close'
        db.delete_column('website_schedule', 'wed_close')

        # Deleting field 'Schedule.thu_close'
        db.delete_column('website_schedule', 'thu_close')

        # Deleting field 'Schedule.tue_open'
        db.delete_column('website_schedule', 'tue_open')

        # Deleting field 'Schedule.sun_close'
        db.delete_column('website_schedule', 'sun_close')

        # Deleting field 'Schedule.wed_open'
        db.delete_column('website_schedule', 'wed_open')


    def backwards(self, orm):
        # Deleting model 'OpenTime'
        db.delete_table('website_opentime')

        # Adding field 'Schedule.mon_open'
        db.add_column('website_schedule', 'mon_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.mon_close'
        db.add_column('website_schedule', 'mon_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sat_open'
        db.add_column('website_schedule', 'sat_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.fri_close'
        db.add_column('website_schedule', 'fri_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sat_close'
        db.add_column('website_schedule', 'sat_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.fri_open'
        db.add_column('website_schedule', 'fri_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sun_open'
        db.add_column('website_schedule', 'sun_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.tue_close'
        db.add_column('website_schedule', 'tue_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.thu_open'
        db.add_column('website_schedule', 'thu_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.wed_close'
        db.add_column('website_schedule', 'wed_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.thu_close'
        db.add_column('website_schedule', 'thu_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.tue_open'
        db.add_column('website_schedule', 'tue_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sun_close'
        db.add_column('website_schedule', 'sun_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.wed_open'
        db.add_column('website_schedule', 'wed_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)


    models = {
        'website.opentime': {
            'Meta': {'object_name': 'OpenTime'},
            'end_day': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'open_times'", 'to': "orm['website.Schedule']"}),
            'start_day': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'website.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_main'", 'to': "orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'special_schedules': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_special'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Schedule']"})
        },
        'website.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valid_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valid_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
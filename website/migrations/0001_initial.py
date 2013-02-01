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

        # Adding model 'Restaurant'
        db.create_table('website_restaurant', (
            ('basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('main_schedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_main', to=orm['website.Schedule'])),
        ))
        db.send_create_signal('website', ['Restaurant'])

        # Adding M2M table for field special_schedules on 'Restaurant'
        db.create_table('website_restaurant_special_schedules', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['website.restaurant'], null=False)),
            ('schedule', models.ForeignKey(orm['website.schedule'], null=False))
        ))
        db.create_unique('website_restaurant_special_schedules', ['restaurant_id', 'schedule_id'])

        # Adding model 'Schedule'
        db.create_table('website_schedule', (
            ('basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('valid_start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('valid_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Schedule'])

        # Adding model 'OpenTime'
        db.create_table('website_opentime', (
            ('basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.BaseModel'], unique=True, primary_key=True)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='open_times', to=orm['website.Schedule'])),
            ('start_day', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_day', self.gf('django.db.models.fields.IntegerField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('website', ['OpenTime'])


    def backwards(self, orm):
        # Deleting model 'BaseModel'
        db.delete_table('website_basemodel')

        # Deleting model 'Restaurant'
        db.delete_table('website_restaurant')

        # Removing M2M table for field special_schedules on 'Restaurant'
        db.delete_table('website_restaurant_special_schedules')

        # Deleting model 'Schedule'
        db.delete_table('website_schedule')

        # Deleting model 'OpenTime'
        db.delete_table('website_opentime')


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
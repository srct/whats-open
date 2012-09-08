# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table('website_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mainSchedule', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_main', to=orm['website.Schedule'])),
        ))
        db.send_create_signal('website', ['Restaurant'])

        # Adding M2M table for field specialSchedules on 'Restaurant'
        db.create_table('website_restaurant_specialSchedules', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['website.restaurant'], null=False)),
            ('schedule', models.ForeignKey(orm['website.schedule'], null=False))
        ))
        db.create_unique('website_restaurant_specialSchedules', ['restaurant_id', 'schedule_id'])

        # Adding model 'Schedule'
        db.create_table('website_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dateValidStart', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dateValidEnd', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('monOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('monClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tueOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('tueClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wedOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('wedClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thuOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('thuClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('friClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('satOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('satClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunOpen', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sunClose', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('website', ['Schedule'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table('website_restaurant')

        # Removing M2M table for field specialSchedules on 'Restaurant'
        db.delete_table('website_restaurant_specialSchedules')

        # Deleting model 'Schedule'
        db.delete_table('website_schedule')


    models = {
        'website.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainSchedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_main'", 'to': "orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'specialSchedules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'restaurant_special'", 'symmetrical': 'False', 'to': "orm['website.Schedule']"})
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
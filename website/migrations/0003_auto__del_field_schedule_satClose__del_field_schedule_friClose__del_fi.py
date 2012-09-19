# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Schedule.satClose'
        db.delete_column('website_schedule', 'satClose')

        # Deleting field 'Schedule.friClose'
        db.delete_column('website_schedule', 'friClose')

        # Deleting field 'Schedule.tueClose'
        db.delete_column('website_schedule', 'tueClose')

        # Deleting field 'Schedule.wedClose'
        db.delete_column('website_schedule', 'wedClose')

        # Deleting field 'Schedule.monOpen'
        db.delete_column('website_schedule', 'monOpen')

        # Deleting field 'Schedule.friOpen'
        db.delete_column('website_schedule', 'friOpen')

        # Deleting field 'Schedule.dateValidStart'
        db.delete_column('website_schedule', 'dateValidStart')

        # Deleting field 'Schedule.sunOpen'
        db.delete_column('website_schedule', 'sunOpen')

        # Deleting field 'Schedule.tueOpen'
        db.delete_column('website_schedule', 'tueOpen')

        # Deleting field 'Schedule.monClose'
        db.delete_column('website_schedule', 'monClose')

        # Deleting field 'Schedule.wedOpen'
        db.delete_column('website_schedule', 'wedOpen')

        # Deleting field 'Schedule.sunClose'
        db.delete_column('website_schedule', 'sunClose')

        # Deleting field 'Schedule.thuOpen'
        db.delete_column('website_schedule', 'thuOpen')

        # Deleting field 'Schedule.thuClose'
        db.delete_column('website_schedule', 'thuClose')

        # Deleting field 'Schedule.satOpen'
        db.delete_column('website_schedule', 'satOpen')

        # Deleting field 'Schedule.dateValidEnd'
        db.delete_column('website_schedule', 'dateValidEnd')

        # Adding field 'Schedule.valid_start'
        db.add_column('website_schedule', 'valid_start',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.valid_end'
        db.add_column('website_schedule', 'valid_end',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.mon_open'
        db.add_column('website_schedule', 'mon_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.mon_close'
        db.add_column('website_schedule', 'mon_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.tue_open'
        db.add_column('website_schedule', 'tue_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.tue_close'
        db.add_column('website_schedule', 'tue_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.wed_open'
        db.add_column('website_schedule', 'wed_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.wed_close'
        db.add_column('website_schedule', 'wed_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.thu_open'
        db.add_column('website_schedule', 'thu_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.thu_close'
        db.add_column('website_schedule', 'thu_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.fri_open'
        db.add_column('website_schedule', 'fri_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.fri_close'
        db.add_column('website_schedule', 'fri_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sat_open'
        db.add_column('website_schedule', 'sat_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sat_close'
        db.add_column('website_schedule', 'sat_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sun_open'
        db.add_column('website_schedule', 'sun_open',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sun_close'
        db.add_column('website_schedule', 'sun_close',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Restaurant.mainSchedule'
        db.delete_column('website_restaurant', 'mainSchedule_id')

        # Adding field 'Restaurant.main_schedule'
        db.add_column('website_restaurant', 'main_schedule',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='restaurant_main', to=orm['website.Schedule']),
                      keep_default=False)

        # Removing M2M table for field specialSchedules on 'Restaurant'
        db.delete_table('website_restaurant_specialSchedules')

        # Adding M2M table for field special_schedules on 'Restaurant'
        db.create_table('website_restaurant_special_schedules', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['website.restaurant'], null=False)),
            ('schedule', models.ForeignKey(orm['website.schedule'], null=False))
        ))
        db.create_unique('website_restaurant_special_schedules', ['restaurant_id', 'schedule_id'])


    def backwards(self, orm):
        # Adding field 'Schedule.satClose'
        db.add_column('website_schedule', 'satClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.friClose'
        db.add_column('website_schedule', 'friClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.tueClose'
        db.add_column('website_schedule', 'tueClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.wedClose'
        db.add_column('website_schedule', 'wedClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.monOpen'
        db.add_column('website_schedule', 'monOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.friOpen'
        db.add_column('website_schedule', 'friOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.dateValidStart'
        db.add_column('website_schedule', 'dateValidStart',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sunOpen'
        db.add_column('website_schedule', 'sunOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.tueOpen'
        db.add_column('website_schedule', 'tueOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.monClose'
        db.add_column('website_schedule', 'monClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.wedOpen'
        db.add_column('website_schedule', 'wedOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.sunClose'
        db.add_column('website_schedule', 'sunClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.thuOpen'
        db.add_column('website_schedule', 'thuOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.thuClose'
        db.add_column('website_schedule', 'thuClose',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.satOpen'
        db.add_column('website_schedule', 'satOpen',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Schedule.dateValidEnd'
        db.add_column('website_schedule', 'dateValidEnd',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Schedule.valid_start'
        db.delete_column('website_schedule', 'valid_start')

        # Deleting field 'Schedule.valid_end'
        db.delete_column('website_schedule', 'valid_end')

        # Deleting field 'Schedule.mon_open'
        db.delete_column('website_schedule', 'mon_open')

        # Deleting field 'Schedule.mon_close'
        db.delete_column('website_schedule', 'mon_close')

        # Deleting field 'Schedule.tue_open'
        db.delete_column('website_schedule', 'tue_open')

        # Deleting field 'Schedule.tue_close'
        db.delete_column('website_schedule', 'tue_close')

        # Deleting field 'Schedule.wed_open'
        db.delete_column('website_schedule', 'wed_open')

        # Deleting field 'Schedule.wed_close'
        db.delete_column('website_schedule', 'wed_close')

        # Deleting field 'Schedule.thu_open'
        db.delete_column('website_schedule', 'thu_open')

        # Deleting field 'Schedule.thu_close'
        db.delete_column('website_schedule', 'thu_close')

        # Deleting field 'Schedule.fri_open'
        db.delete_column('website_schedule', 'fri_open')

        # Deleting field 'Schedule.fri_close'
        db.delete_column('website_schedule', 'fri_close')

        # Deleting field 'Schedule.sat_open'
        db.delete_column('website_schedule', 'sat_open')

        # Deleting field 'Schedule.sat_close'
        db.delete_column('website_schedule', 'sat_close')

        # Deleting field 'Schedule.sun_open'
        db.delete_column('website_schedule', 'sun_open')

        # Deleting field 'Schedule.sun_close'
        db.delete_column('website_schedule', 'sun_close')

        # Adding field 'Restaurant.mainSchedule'
        db.add_column('website_restaurant', 'mainSchedule',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='restaurant_main', to=orm['website.Schedule']),
                      keep_default=False)

        # Deleting field 'Restaurant.main_schedule'
        db.delete_column('website_restaurant', 'main_schedule_id')

        # Adding M2M table for field specialSchedules on 'Restaurant'
        db.create_table('website_restaurant_specialSchedules', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['website.restaurant'], null=False)),
            ('schedule', models.ForeignKey(orm['website.schedule'], null=False))
        ))
        db.create_unique('website_restaurant_specialSchedules', ['restaurant_id', 'schedule_id'])

        # Removing M2M table for field special_schedules on 'Restaurant'
        db.delete_table('website_restaurant_special_schedules')


    models = {
        'website.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_main'", 'to': "orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'special_schedules': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_special'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['website.Schedule']"})
        },
        'website.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'fri_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'fri_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mon_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'mon_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sat_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sat_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sun_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'sun_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thu_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'thu_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tue_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'tue_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'valid_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valid_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'wed_close': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'wed_open': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
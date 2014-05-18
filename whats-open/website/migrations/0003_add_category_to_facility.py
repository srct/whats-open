# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'website_category', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['website.BaseModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['Category'])

        # Adding field 'Facility.category'
        db.add_column(u'website_facility', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='facilities', null=True, to=orm['website.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'website_category')

        # Deleting field 'Facility.category'
        db.delete_column(u'website_facility', 'category_id')


    models = {
        u'website.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'website.category': {
            'Meta': {'object_name': 'Category', '_ormbases': [u'website.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'website.facility': {
            'Meta': {'ordering': "['name']", 'object_name': 'Facility', '_ormbases': [u'website.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'facilities'", 'null': 'True', 'to': u"orm['website.Category']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'main_schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facility_main'", 'to': u"orm['website.Schedule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'special_schedules': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'facility_special'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['website.Schedule']"})
        },
        u'website.opentime': {
            'Meta': {'object_name': 'OpenTime', '_ormbases': [u'website.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'end_day': ('django.db.models.fields.IntegerField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'open_times'", 'to': u"orm['website.Schedule']"}),
            'start_day': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'website.schedule': {
            'Meta': {'ordering': "['name']", 'object_name': 'Schedule', '_ormbases': [u'website.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['website.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'valid_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'valid_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['website']
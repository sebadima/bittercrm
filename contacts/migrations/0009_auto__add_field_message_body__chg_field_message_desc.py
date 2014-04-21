# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.body'
        db.add_column(u'contacts_message', 'body',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1000),
                      keep_default=False)


        # Changing field 'Message.desc'
        db.alter_column(u'contacts_message', 'desc', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Message.body'
        db.delete_column(u'contacts_message', 'body')


        # Changing field 'Message.desc'
        db.alter_column(u'contacts_message', 'desc', self.gf('django.db.models.fields.TextField')(max_length=1000))

    models = {
        u'contacts.action': {
            'Meta': {'object_name': 'Action'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.category': {
            'Meta': {'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Action']"}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Category']"}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'example@example.com'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'default': "'lastname'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "'...'", 'max_length': '200'}),
            'rating': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '200'})
        },
        u'contacts.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['contacts']
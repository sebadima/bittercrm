# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Action'
        db.create_table(u'contacts_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'contacts', ['Action'])

        # Adding model 'Category'
        db.create_table(u'contacts_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'contacts', ['Category'])

        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=200)),
            ('lastname', self.gf('django.db.models.fields.CharField')(default='lastname', max_length=200)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(default='example@example.com', max_length=200)),
            ('rating', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=200)),
            ('notes', self.gf('django.db.models.fields.CharField')(default='...', max_length=200)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Category'])),
        ))
        db.send_create_signal(u'contacts', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Action'
        db.delete_table(u'contacts_action')

        # Deleting model 'Category'
        db.delete_table(u'contacts_category')

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')


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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Category']"}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'example@example.com'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'default': "'lastname'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "'...'", 'max_length': '200'}),
            'rating': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '200'})
        }
    }

    complete_apps = ['contacts']
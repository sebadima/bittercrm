# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Clienti.rating'
        db.add_column(u'clienti_clienti', 'rating',
                      self.gf('django.db.models.fields.CharField')(default='1.0', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Clienti.rating'
        db.delete_column(u'clienti_clienti', 'rating')


    models = {
        u'clienti.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'clienti': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clienti.Clienti']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'clienti.clienti': {
            'Meta': {'object_name': 'Clienti'},
            'annotazioni': ('django.db.models.fields.CharField', [], {'default': "'...'", 'max_length': '200'}),
            'citta': ('django.db.models.fields.CharField', [], {'default': "'citta'", 'max_length': '200'}),
            'cognome': ('django.db.models.fields.CharField', [], {'default': "'cognome'", 'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'esempio@esempio.com'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "'nome'", 'max_length': '200'}),
            'ragione_sociale': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '200'})
        }
    }

    complete_apps = ['clienti']
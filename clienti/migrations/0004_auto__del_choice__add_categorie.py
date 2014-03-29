# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Choice'
        db.delete_table(u'clienti_choice')

        # Adding model 'Categorie'
        db.create_table(u'clienti_categorie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campo1', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('campo2', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'clienti', ['Categorie'])


    def backwards(self, orm):
        # Adding model 'Choice'
        db.create_table(u'clienti_choice', (
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('clienti', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clienti.Clienti'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'clienti', ['Choice'])

        # Deleting model 'Categorie'
        db.delete_table(u'clienti_categorie')


    models = {
        u'clienti.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'campo1': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'campo2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
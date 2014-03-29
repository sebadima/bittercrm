# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Clienti.mese_ultima_consegna'
        db.delete_column(u'clienti_clienti', 'mese_ultima_consegna')

        # Deleting field 'Clienti.giorno_ultima_consegna'
        db.delete_column(u'clienti_clienti', 'giorno_ultima_consegna')

        # Deleting field 'Clienti.anno_ultima_consegna'
        db.delete_column(u'clienti_clienti', 'anno_ultima_consegna')

        # Adding field 'Clienti.nome'
        db.add_column(u'clienti_clienti', 'nome',
                      self.gf('django.db.models.fields.CharField')(default='nome', max_length=200),
                      keep_default=False)

        # Adding field 'Clienti.cognome'
        db.add_column(u'clienti_clienti', 'cognome',
                      self.gf('django.db.models.fields.CharField')(default='cognome', max_length=200),
                      keep_default=False)

        # Adding field 'Clienti.email'
        db.add_column(u'clienti_clienti', 'email',
                      self.gf('django.db.models.fields.CharField')(default='esempio@esempio.com', max_length=200),
                      keep_default=False)


        # Changing field 'Clienti.citta'
        db.alter_column(u'clienti_clienti', 'citta', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):
        # Adding field 'Clienti.mese_ultima_consegna'
        db.add_column(u'clienti_clienti', 'mese_ultima_consegna',
                      self.gf('django.db.models.fields.CharField')(default='03', max_length=4),
                      keep_default=False)

        # Adding field 'Clienti.giorno_ultima_consegna'
        db.add_column(u'clienti_clienti', 'giorno_ultima_consegna',
                      self.gf('django.db.models.fields.CharField')(default='23', max_length=2),
                      keep_default=False)

        # Adding field 'Clienti.anno_ultima_consegna'
        db.add_column(u'clienti_clienti', 'anno_ultima_consegna',
                      self.gf('django.db.models.fields.CharField')(default='2014', max_length=4),
                      keep_default=False)

        # Deleting field 'Clienti.nome'
        db.delete_column(u'clienti_clienti', 'nome')

        # Deleting field 'Clienti.cognome'
        db.delete_column(u'clienti_clienti', 'cognome')

        # Deleting field 'Clienti.email'
        db.delete_column(u'clienti_clienti', 'email')


        # Changing field 'Clienti.citta'
        db.alter_column(u'clienti_clienti', 'citta', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'ragione_sociale': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clienti']
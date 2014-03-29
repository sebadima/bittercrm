# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Clienti'
        db.create_table(u'clienti_clienti', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ragione_sociale', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('indirizzo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('citta', self.gf('django.db.models.fields.CharField')(default='Siracusa', max_length=100)),
            ('annotazioni', self.gf('django.db.models.fields.CharField')(default='Bombola da 15 Kg ...', max_length=200)),
            ('giorno_ultima_consegna', self.gf('django.db.models.fields.CharField')(default='23', max_length=2)),
            ('mese_ultima_consegna', self.gf('django.db.models.fields.CharField')(default='03', max_length=4)),
            ('anno_ultima_consegna', self.gf('django.db.models.fields.CharField')(default='2014', max_length=4)),
        ))
        db.send_create_signal(u'clienti', ['Clienti'])

        # Adding model 'Choice'
        db.create_table(u'clienti_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clienti', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clienti.Clienti'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'clienti', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'Clienti'
        db.delete_table(u'clienti_clienti')

        # Deleting model 'Choice'
        db.delete_table(u'clienti_choice')


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
            'anno_ultima_consegna': ('django.db.models.fields.CharField', [], {'default': "'2014'", 'max_length': '4'}),
            'annotazioni': ('django.db.models.fields.CharField', [], {'default': "'Bombola da 15 Kg ...'", 'max_length': '200'}),
            'citta': ('django.db.models.fields.CharField', [], {'default': "'Siracusa'", 'max_length': '100'}),
            'giorno_ultima_consegna': ('django.db.models.fields.CharField', [], {'default': "'23'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mese_ultima_consegna': ('django.db.models.fields.CharField', [], {'default': "'03'", 'max_length': '4'}),
            'ragione_sociale': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clienti']
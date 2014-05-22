# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'isobres_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('direccio', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('telefon', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'isobres', ['Client'])

        # Adding model 'Hostal'
        db.create_table(u'isobres_hostal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('direccio', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('telefon', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'isobres', ['Hostal'])

        # Adding model 'Habitacio'
        db.create_table(u'isobres_habitacio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['isobres.Hostal'])),
            ('numero_habitacio', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('preu_nit', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'isobres', ['Habitacio'])

        # Adding model 'Reserva'
        db.create_table(u'isobres_reserva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('habitacio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['isobres.Habitacio'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['isobres.Client'])),
            ('data_ent', self.gf('django.db.models.fields.DateTimeField')()),
            ('data_sort', self.gf('django.db.models.fields.DateTimeField')()),
            ('confirmada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('qualificacio', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comenari_qualificacio', self.gf('django.db.models.fields.TextField')(default='', max_length=150)),
        ))
        db.send_create_signal(u'isobres', ['Reserva'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'isobres_client')

        # Deleting model 'Hostal'
        db.delete_table(u'isobres_hostal')

        # Deleting model 'Habitacio'
        db.delete_table(u'isobres_habitacio')

        # Deleting model 'Reserva'
        db.delete_table(u'isobres_reserva')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'isobres.client': {
            'Meta': {'object_name': 'Client'},
            'direccio': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'isobres.habitacio': {
            'Meta': {'object_name': 'Habitacio'},
            'hostal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['isobres.Hostal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_habitacio': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'preu_nit': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'isobres.hostal': {
            'Meta': {'object_name': 'Hostal'},
            'direccio': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'telefon': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'isobres.reserva': {
            'Meta': {'object_name': 'Reserva'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['isobres.Client']"}),
            'comenari_qualificacio': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '150'}),
            'confirmada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_ent': ('django.db.models.fields.DateTimeField', [], {}),
            'data_sort': ('django.db.models.fields.DateTimeField', [], {}),
            'habitacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['isobres.Habitacio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'qualificacio': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['isobres']
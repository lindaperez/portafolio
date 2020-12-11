from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    started = models.DateTimeField()
    ended = models.DateTimeField(blank=True, null=True)
    backend = models.CharField(max_length=50)
    frontend = models.CharField(max_length=50)
    repo_name = models.CharField(max_length=100)
    repo_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'project'
        ordering = ["-title"]

    def __str__(self):
        return self.title


class RelProjectComment(models.Model):
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    comment = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'rel_project_comment'


class CatStateFeature(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cat_state_feature'

class RelProjectFeature(models.Model):
    feat_state = models.ForeignKey(CatStateFeature, models.DO_NOTHING, db_column='feat_state')
    description = models.CharField(max_length=500)
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')

    class Meta:
        managed = False
        db_table = 'rel_project_feature'


class RelProjectUser(models.Model):
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'rel_project_user'


class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'


class View(models.Model):
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project')
    description = models.CharField(max_length=50)
    picpath = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'view'

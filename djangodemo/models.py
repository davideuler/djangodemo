#coding:utf-8

from django.db import models

STATUS_CHOICES = (('submmiting','提案中'),('signed','报价已签'),('ongoing','启动中'),('released','已发布'),
                  ('PO','已开票'),('fee_received','已收款'),('terminated','已终止'))

class Project(models.Model):
    name = models.CharField(max_length=100,verbose_name='项目名称', help_text='项目的名称')
    customer_name = models.CharField(max_length=100,verbose_name='客户名称', help_text='客户名称')
    charger = models.CharField(max_length=100,verbose_name='负责人', help_text='内部负责人')
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,verbose_name='项目状态', help_text='项目的状态')
    total_fee = models.CharField(max_length=100,verbose_name='项目金额', help_text='项目的金额')
    team = models.CharField(max_length=100,verbose_name='团队', help_text='团队')

    def __str__(self):              # __unicode__ on Python 2
        return self.name + '_' + self.customer_name

    def __unicode__(self):           # fix UnicodeEncodeError
        return u"%s" % self.name

    class Meta:
        managed = True
        db_table = 'project'
        verbose_name =  u'项目'
        verbose_name_plural = u'项目'
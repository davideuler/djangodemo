#--coding=utf-8--

MODELS = {
    'datasource': {
        'table_name': 'report_datasource',
        'table_desc': '数据源',
        'fields':
        {
             'name' : '数据源名称',
             'ip' : '服务器IP',
             'conn_str' : '连接字符串',
             'type' : '数据库类型 Mysql/Mssql/Oracle/Postgresql/Xls',
             'creator' : '创建者',
	     'shared' : '是否与其他用户共享数据源:y/n',
             'created_time' : '创建时间',
             'updated_time' : '更新时间',
             'comment' : '备注',
        }
    },
	
    'mainDataDefinition': {
        'table_name': 'main_data_definition',
        'table_desc': '主数据表',
        'fields':
        {
             'name' : '表名称',
             'name_en' : '表英文名称',
             'report_datasource_id' : '数据源ID',
             'sql' : '查询sql',
             'key_column' : '主键字段名；用于唯一标识一条数据，关联从表数据',
             'creator' : '创建者',
             'created_time' : '创建时间',
             'updated_time' : '更新时间',
             'comment' : '备注',
        }
    },

    'extraDataDefinition': {
        'table_name': 'extra_data_definition',
        'table_desc': '从数据表',
        'fields':
        {
             'name' : '表名称',
             'name_en' : '表英文名称',
             'report_datasource_id' : '数据源ID',
             'sql' : '查询sql',
             'depend_on_tablename' : '依赖的数据表名',
             'relation_keys' : '关联主表的字段名，多个key以逗号分隔',
             'creator' : '创建者',
             'created_time' : '创建时间',
             'updated_time' : '更新时间',
             'comment' : '备注',
        }
    },

    'report': {
        'table_name': 'report',
        'table_desc': '数据报表',
        'fields':
        {
             'report_name' : '报表名称',
             'report_name_en' : '报表英文名(不含空格)',
             'email_receivers' : '报告的邮件接受者(多个接受者之间以逗号分隔)',
             'creator' : '创建者',
             'created_time' : '创建时间',
             'updated_time' : '更新时间',
             'comment' : '备注',
        }
    },

    'reportMainData': {
        'table_name': 'report_maindata',
        'table_desc': '数据报表主数据定义',
        'fields':
        {
             'report_id' : '报表ID',
             'step' : '步骤',
             'main_data_definition_id' : '主数据',
             'creator' : '创建者',
             'comment' : '备注',
        }
    },

    'reportExtraData': {
        'table_name': 'report_extradata',
        'table_desc': '报表的关联从数据定义',
        'fields':
        {
             'report_id' : '报表ID',
             'step' : '步骤',
             'extra_data_definition_id' : '关联的从数据',
             'creator' : '创建者',
             'comment' : '备注',
        }
    },


    'reportFilter': {
        'table_name': 'report_filter',
        'table_desc': '报表的数据过滤器',
        'fields':
        {
             'report_id' : '报表ID',
             'step' : '步骤',
             'filter_name' : '过滤器名称',
             'filter_definition' : '过滤器定义(如 Duplicator:{KeyColumns:{phone,username}} 定义一个根据 phone,username去重的过滤器 )',
             'creator' : '创建者',
             'created_time' : '创建时间',
             'updated_time' : '更新时间',
             'comment' : '备注',
        }
    },


    'reportDataFields': {
        'table_name': 'report_data_fields',
        'table_desc': '报表数据的字段',
        'fields':
        {
             'report_id' : '报表ID',
             'report_data_name' : '报表data_name',
             'data_field_name' : 'data数据表数据的字段名',
             'included_in_report' : '改字段是否被收集作为报表的字段',
             'report_field_name' : '报表的字段名',
             'comment' : '备注',
        }
    },

    'reportDetailPostQueries': {
        'table_name': 'report_detail_post_queries',
        'table_desc': '报表明细的后处理查询SQL',
        'fields':
        {
             'report_id' : '报表ID',
             'post_query_name' : '后处理查询的名字',
             'post_query_sql' : '查询SQL',
             'comment' : '备注',
        }
    },

    'reportTemplate': {
        'table_name': 'report_template',
        'table_desc': '报表的模版文件',
        'fields':
        {
             'report_id' : '报表ID',
             'report_template_url' : '模版文件url',
             'creator' : '创建者',
             'comment' : '备注',
        }
    },

    'reportArchiveHistory': {
        'table_name': 'report_archive_history',
        'table_desc': '报表的归档历史记录',
        'fields':
        {
             'report_id' : '报表ID',
             'report_detail_tablename' : '保存报表明细数据的数据表名称',
             'report_generate_time': '报表生成时间',
             'report_name' : '报表名称',
             'report_filepath' : '报表文件路径',
             'report_serialized_object_filepath' : '序列化的Json格式的Report对象文件路径,可以用来跟明细数据一起重新生成报表文件',
             'created_time' : '创建时间',
             'updated_time' : '更新时间',
             'comment' : '备注',
        }
    },


}

'''
class Holiday(models.Model):
    date = models.DateField(verbose_name='日期')

    updated_time = models.DateTimeField(verbose_name= '数据更新时间')

    class Meta:
        managed = False
        db_table = 'holiday'
        verbose_name =  u'假期'
        verbose_name_plural = u'假期'
'''


def generate_models():
    for model_name,info in MODELS.iteritems():
        model_str = '''
class %model_name%(models.Model):
    %column_def%

    class Meta:
        managed = False
        db_table = '%table_name%'
        verbose_name =  u'%table_desc%'
        verbose_name_plural = u'%table_desc%'
'''
        table_name = info['table_name']
        table_desc = info['table_desc']
        fields = info['fields']
        model_str = model_str.replace('%model_name%',model_name.title())
        model_str = model_str.replace('%table_name%',table_name)
        model_str = model_str.replace('%table_desc%',table_desc)
        
        column_def = ''
        for field_name,field_desc in fields.iteritems():
            if 'time' in field_name:
                column_def += ("\r\n    %s = models.DateTimeField(verbose_name='%s')" % (field_name,field_desc) ) 
            elif 'date' in field_name:
                column_def += ("\r\n    %s = models.DateTimeField(verbose_name='%s')" % (field_name,field_desc) )
            else:
                column_def += ("\r\n    %s = models.CharField(max_length=100, blank=True, null=True, verbose_name='%s')" % (field_name,field_desc) ) 
        
        print(model_str.replace('%column_def%',column_def))

'''
CREATE TABLE `t_holiday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL COMMENT '日期',
  `updated_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
def table_creation_sql():
    for model_name,info in MODELS.iteritems():
        sql_str = '''
CREATE TABLE `%table_name%` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
%field_def%      PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
        table_name = info['table_name']
        table_desc = info['table_desc']
        fields = info['fields']
        sql_str = sql_str.replace('%table_name%',table_name)
        
        field_def = ''
        for field_name,field_desc in fields.iteritems():
            if 'time' in field_name:
                field_def += ("      `%s` datetime NOT NULL COMMENT '%s',\r\n" % (field_name,field_desc) )
            elif 'date' in field_name:
                field_def += ("      `%s` datetime NOT NULL COMMENT '%s',\r\n" % (field_name,field_desc) ) 
            else:
                field_def += ("      `%s` varchar(100) DEFAULT NULL COMMENT '%s',\r\n" % (field_name,field_desc) ) 
        sql_str = sql_str.replace('%field_def%',field_def)
        print(sql_str)
        

if __name__ == '__main__':
    generate_models()
    table_creation_sql()

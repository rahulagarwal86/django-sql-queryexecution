from django.shortcuts import render_to_response
from django.template import RequestContext
from sqloperation.decorator import superuser_only
from django.contrib.admin.views.decorators import staff_member_required
from django.db import connection, transaction
import sys

'''
Function used to execute sql query on MySQL DB
'''
@staff_member_required
@superuser_only
def execute_sql( request ):
    if request.method == "POST": 
        cursor = connection.cursor()  
        sql = request.POST['id_sqlquery']
        data = []
        try:            
            cursor.execute( sql )
            rows_effected = cursor.rowcount
            result = cursor.fetchall()
            desc = cursor.description
            if desc:                
                header = [d[0].title() for d in desc]
                data.append( header )
                for row in result:
                    data.append( row )
            transaction.commit_unless_managed()
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            rows_effected = 0
            data.append( exc_type )
            data.append( exc_value )
        return render_to_response( 'sqloperation/sql_result.html', locals(), context_instance = RequestContext( request ) )
    else:
        return render_to_response( 'sqloperation/raw_sql.html', locals(), context_instance = RequestContext( request ) )


    

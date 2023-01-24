import time
import glob 
import itertools
from datetime import date, timedelta
import dateutil.parser
import csv 
import os 
import json 
import io 
import requests
import traceback
import shutil
import boto3
from pytz import timezone
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader,BinaryDecoder
import avro
# import tableauserverclient as TSC 
# from tableauhyperapi import HyperProcess, Telemetry, Connection#, CreateMode, NOT_NULLABLE, NULLABLE, SqlType,TableDefinition, Inserter, escape_name, escape_string_literal, HyperException, print_exception, TableName
import zipfile
import teradatasql
import pyodbc
from requests_ntlm import HttpNtlmAuth
try:
    import cx_Oracle
except:
    pass 
try: 
    from jira import JIRA
except: 
    pass
import pandas as pd
import numpy as np 
import ssl

#from cassandra.cluster import Cluster
#from cassandra.auth import PlainTextAuthProvider
#from cassandra.query import BatchStatement
# import tableauserverclient as TSC 
# from tableauhyperapi import HyperProcess, Telemetry, Connection,TableName,escape_string_literal#, CreateMode, NOT_NULLABLE, NULLABLE, SqlType,TableDefinition, Inserter, escape_name, escape_string_literal, HyperException, print_exception, TableName

exec(open("C:\\ds\\cari-uswm-s3\\alteryx-tools\\supporting_functions.py",'r+').read())

# teradatasql.connect(host='idwprd.card.jpmchase.net',user="E824291",password=SupportingFunctions().decode_binary(b'MVBlYXMmQ2Fycm90cw=='),logmech='LDAP')

# try:
#     exec(open("C:\\ds\\cari-uswm-s3\\alteryx-tools\\supporting_functions.py",'r+').read())
# except:
#     exec(requests.get("https://uswm-code-repository.apps.dev.na-1z.gap.jpmchase.net/read/supporting_functions.py",verify=False).text)

def duration_print(duration):
    if duration > 60:
        print ("Duration: " + "{0:,.2f}".format(duration/60) + " minutes")
    elif duration > 3:
        print ("Duration: " + "{0:,.2f}".format(duration) + " seconds")

def duration_print_start(start_time):
    end_time = time.time()
    duration = (end_time - start_time)
    duration_print(duration)

python_files_to_process = [i for i in glob.glob(os.path.join(os.getcwd(),'*.py')) if 'pyapp.py' not in i]
for python_latest_local_file_script in python_files_to_process:
    start_time = time.time()
    print ("Running: " + python_latest_local_file_script)
    try:
        exec(open(python_latest_local_file_script,'r+').read())
    except:
        traceback.print_exc()
    duration_print_start(start_time)

while True:
    try:
        ran_input_text =  input( ">>>")
        if ran_input_text == "":
            python_files_to_process = [i for i in glob.glob(os.path.join(os.getcwd(),'*.py')) if 'pyapp.py' not in i]
            for python_latest_local_file_script in python_files_to_process:
                start_time = time.time()
                #print ("Running: " + python_latest_local_file_script)
                try:
                    exec(open(python_latest_local_file_script,'r+').read())
                except:
                    traceback.print_exc()
                duration_print_start(start_time)
            # ran_input_text =  input( ">>>")
        else:
            code = ran_input_text
            exec(code)
    except:
        traceback.print_exc()

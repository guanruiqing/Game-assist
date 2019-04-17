#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
No Man's Sky: Refined table
'''

__author__ = 'guanruiqing'


import json
from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    file_text, Generate_table = Generate_table_reload()
    Generate_table_html = Generate_table_print(Generate_table)
    return '''<form action='/save' method='post'>
                <p>
                  <input name='save' size=28>
                  <input type='submit' value='Save'>
                  <input type='reset' value='Reset'>
                </p>
              </form>
              <form action='/delete' method='post'>
                <p>
                  <input name='delete' size=28>
                  <input type='submit' value='Delete'>
                  <input type='reset' value='Reset'>
                </p>
              </form>
              <form action='/select' method='post'>
                <p>
                  <input name='s1' size=1> +
                  <input name='s2' size=1> +
                  <input name='s3' size=1> =
                  <input name='s4' size=1>
                  <input type='submit' value='Select'>
                  <input type='reset' value='Reset'>
                </p>
              </form>
              <hr />
              %s
           '''%(Generate_table_html)

@app.route('/save', methods=['POST'])
def home_save():
    file_text, Generate_table = Generate_table_reload()
    try:
        input_save = json.loads(request.form['save'].replace('\'','"'))
        status = Generate_table_save_check(input_save, Generate_table)
        if status != 'repeat':
            Generate_table.append(input_save)
            Generate_table_save(file_text, Generate_table)
    except Exception:
        status = 'input error'
    return '''<input type="button" value='Return' onclick="location.href='/'">
              <hr />
              <p>%s</p>
           '''%(status)

@app.route('/delete', methods=['POST'])
def home_delete():
    file_text, Generate_table = Generate_table_reload()
    try:
        input_delete = json.loads(request.form['delete'].replace('\'','"'))
        if input_delete in Generate_table:
            Generate_table.remove(input_delete)
            status = str(input_delete)
            Generate_table_save(file_text, Generate_table)
        else:
            status = 'not found'
    except Exception:
        status = 'input error'
    return '''<input type="button" value='Return' onclick="location.href='/'">
              <hr />
              <p>%s</p>
           '''%(status)

@app.route('/select', methods=['POST'])
def home_select():
    file_text, Generate_table = Generate_table_reload()
    s1, s2, s3, s4 = request.form['s1'], request.form['s2'], request.form['s3'], request.form['s4']
    Generate_table_cache = Generate_table_select(s1, s2, s3, s4, Generate_table)
    Generate_table_html = Generate_table_print(Generate_table_cache)
    return '''<input type="button" value='Return' onclick="location.href='/'">
              <hr />
              %s
           '''%(Generate_table_html)

    


def Generate_table_reload():
    with open(__file__, 'r') as f:
        file_text = f.readlines()
        Generate_table = json.loads(file_text[-1])
    return file_text, Generate_table

def Generate_table_save(file_text, Generate_table):
    with open(__file__, 'w') as f:
        file_text[-1] = json.dumps(Generate_table)
        f.writelines(file_text)

def Generate_table_save_check(input_save, Generate_table):
    Reactant_list = list(input_save[0].keys())
    for i in Generate_table:
        if list(i[0].keys()) == Reactant_list:
                return 'repeat'
    return str(input_save)

def Generate_table_print(Generate_table):
    Generate_table_html = ''
    for i in Generate_table:
        Generate_table_html = Generate_table_html + '<p>' + str(i) + '</p>'
    return Generate_table_html

def Generate_table_select(s1, s2, s3, s4, Generate_table):
    Generate_table_cache1 = Generate_table[:]
    while True:
        Generate_table_cache2 = Generate_table_cache1[:]
        if s1:
            for i in Generate_table_cache1:
                if s1 not in i[0]:
                    Generate_table_cache1.remove(i)
        if s2:
            for i in Generate_table_cache1:
                if s2 not in i[0]:
                    Generate_table_cache1.remove(i)
        if s3:
            for i in Generate_table_cache1:
                if s3 not in i[0]:
                    Generate_table_cache1.remove(i)
        if s4:
            for i in Generate_table_cache1:
                if s4 not in i[1]:
                    Generate_table_cache1.remove(i)
        if Generate_table_cache1 ==Generate_table_cache2:
            break
    return Generate_table_cache1


if __name__=='__main__':
    app.run(host='192.168.0.201', port=5000, debug=True)
    #app.run(host='192.168.0.201', port=5000)


[[{"\u94b4": 2, "\u6c27\u6c14": 2}, {"\u79bb\u5b50\u94b4": 5}], [{"\u94a0": 1, "\u6d53\u7f29\u78b3": 1}, {"\u785d\u9178\u94a0": 2}], [{"\u94dc": 1, "\u6709\u8272\u91d1\u5c5e": 1}, {"\u94dc": 4}], [{"\u94dc": 2}, {"\u6709\u8272\u91d1\u5c5e": 1}]]
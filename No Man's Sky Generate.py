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
        if sorted(list(i[0].keys())) == sorted(Reactant_list):
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
        if Generate_table_cache1 == Generate_table_cache2:
            break
    return Generate_table_cache1


if __name__=='__main__':
    #app.run(host='192.168.0.201', port=5000, debug=True)
    app.run(host='127.0.0.1', port=5000)


[[{"\u94a0": 1, "\u6d53\u7f29\u78b3": 1}, {"\u785d\u9178\u94a0": 2}], [{"\u94dc": 1, "\u6709\u8272\u91d1\u5c5e": 1}, {"\u94dc": 4}], [{"\u94dc": 2}, {"\u6709\u8272\u91d1\u5c5e": 1}], [{"\u94f6": 100}, {"\u73bb\u7483": 1}], [{"\u91d1": 1}, {"\u9ec4\u94c1\u77ff": 1}], [{"\u94c2": 5}, {"\u7eb3\u7c73\u661f\u56e2": 1}], [{"\u666e\u8335": 10}, {"\u7eb3\u7c73\u661f\u56e2": 1}], [{"\u8150\u85e4": 3}, {"\u9b3c\u7caa": 1}], [{"\u6c27\u6c14": 1}, {"\u78b3": 1}], [{"\u4e8c\u6c22": 30}, {"\u4e8c\u6c22\u51dd\u80f6": 1}], [{"\u4e8c\u6c22\u51dd\u80f6": 1}, {"\u4e8c\u6c22": 50}], [{"\u78b3\u6676\u4f53": 1}, {"\u6d53\u7f29\u78b3": 150}], [{"\u7a00\u6709\u91d1\u5c5e\u5143\u7d20": 1}, {"\u7eaf\u94c1\u6c27\u4f53": 150}], [{"\u56db\u94b4": 1}, {"\u79bb\u5b50\u94b4": 150}], [{"\u6c2f\u5316\u7269\u6676\u683c\u5316": 1}, {"\u6c2f": 150}], [{"\u4e0d\u7a33\u5b9a\u7684\u94a0": 1}, {"\u785d\u9178\u94a0": 150}], [{"\u8d85\u6c27\u5316\u7269\u6676\u4f53": 1}, {"\u6c27\u6c14": 150}], [{"\u94b4": 2}, {"\u79bb\u5b50\u94b4": 1}], [{"\u79bb\u5b50\u94b4": 1}, {"\u94b4": 2}], [{"\u78b3": 2}, {"\u6d53\u7f29\u78b3": 1}], [{"\u6d53\u7f29\u78b3": 1}, {"\u78b3": 2}], [{"\u94a0": 2}, {"\u785d\u9178\u94a0": 1}], [{"\u785d\u9178\u94a0": 1}, {"\u94a0": 2}], [{"\u94c1\u6c27\u4f53\u7c89\u672b": 1}, {"\u7eaf\u94c1\u6c27\u4f53": 1}], [{"\u7eaf\u94c1\u6c27\u4f53": 2}, {"\u78c1\u5316\u7269\u94c1\u6c27\u4f53": 1}], [{"\u78c1\u5316\u7269\u94c1\u6c27\u4f53": 1}, {"\u7eaf\u94c1\u6c27\u4f53": 2}], [{"\u9549": 1}, {"\u6709\u8272\u91d1\u5c5e": 1}], [{"\u94df": 1}, {"\u6709\u8272\u91d1\u5c5e": 2}], [{"\u827e\u6885\u91cc\u5c14": 2}, {"\u6709\u8272\u91d1\u5c5e": 3}], [{"\u6d3b\u6027\u9549": 1}, {"\u6709\u8272\u91d1\u5c5e": 2}], [{"\u6d3b\u6027\u94df": 1}, {"\u6709\u8272\u91d1\u5c5e": 4}], [{"\u6d3b\u6027\u827e\u6885\u91cc\u5c14": 1}, {"\u6709\u8272\u91d1\u5c5e": 3}], [{"\u6d3b\u6027\u94dc": 1}, {"\u6709\u8272\u91d1\u5c5e": 1}], [{"\u77ff\u8102": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 1}], [{"\u9ec4\u94c1\u77ff": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 1}], [{"\u6c28": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 1}], [{"\u94c0": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 1}], [{"\u4e8c\u6c27\u5316\u7269": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 1}], [{"\u78f7": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 1}], [{"\u76d0": 2}, {"\u6c2f": 1}], [{"\u6c2f": 1}, {"\u76d0": 2}], [{"\u6c2e": 3}, {"\u786b\u78fa": 1}], [{"\u6c21": 3}, {"\u6c2e": 1}], [{"\u786b\u78fa": 3}, {"\u6c21": 1}], [{"\u5269\u4f59\u7c98\u7a20\u7269": 1}, {"\u9ecf\u6027\u6d41\u8d28": 1}], [{"\u9ecf\u6027\u6d41\u8d28": 1}, {"\u6d3b\u4f53\u7c98\u8d28": 1}], [{"\u6d3b\u4f53\u7c98\u8d28": 1}, {"\u5931\u63a7\u7684\u6a21\u5177": 1}], [{"\u5931\u63a7\u7684\u6a21\u5177": 5}, {"\u7eb3\u7c73\u661f\u56e2": 1}], [{"\u751f\u9508\u7684\u91d1\u5c5e": 1}, {"\u94c1\u6c27\u4f53\u7c89\u672b": 2}], [{"\u6c1a": 5}, {"\u4e8c\u6c22": 1}], [{"\u771f\u83cc\u9709": 1}, {"\u78b3": 2}], [{"\u51b0\u971c\u6c34\u6676": 1}, {"\u78b3": 2}], [{"\u4f3d\u9a6c\u6839": 1}, {"\u78b3": 2}], [{"\u4ed9\u4eba\u638c\u8089": 1}, {"\u78b3": 2}], [{"\u65e5\u5149\u8304": 1}, {"\u78b3": 2}], [{"\u661f\u8fb0\u6735": 1}, {"\u78b3": 2}], [{"\u846b\u82a6\u6735": 1}, {"\u94a0": 1}], [{"\u6d77\u85fb\u888b": 1}, {"\u6c27\u6c14": 1}], [{"\u9b3c\u7caa": 3}, {"\u8150\u85e4": 2}], [{"\u963f\u6d1b\u59c6": 1}, {"\u94f6": 250}], [{"\u80ae\u810f\u9752\u94dc": 1}, {"\u94f6": 250}], [{"\u8d6b\u7f57\u514b\u65af": 1}, {"\u94f6": 250}], [{"\u6676\u571f\u77ff": 1}, {"\u94f6": 250}], [{"\u8f90\u77ff": 1}, {"\u94f6": 250}], [{"\u5217\u7c73\u59c6": 1}, {"\u91d1": 125}], [{"\u954d\u9530\u91d1": 1}, {"\u91d1": 125}], [{"\u683c\u5170\u4e01": 1}, {"\u91d1": 125}], [{"\u5269\u4f59\u7c98\u7a20\u7269": 1, "\u9b3c\u7caa": 1}, {"\u91d1": 1}], [{"\u91d1": 1, "\u94f6": 1}, {"\u94c2": 1}], [{"\u4e8c\u6c22": 1, "\u94c0": 1}, {"\u6d53\u7f29\u78b3": 2}], [{"\u4e8c\u6c22": 1, "\u786b\u78fa": 1}, {"\u65e5\u5149\u8304": 1}], [{"\u4e8c\u6c22": 1, "\u6c21": 1}, {"\u94c0": 1}], [{"\u4e8c\u6c22": 1, "\u6c2e": 1}, {"\u6c28": 1}], [{"\u4e8c\u6c22": 1, "\u6c27\u6c14": 1}, {"\u76d0": 1}], [{"\u4e8c\u6c22": 1, "\u78b3": 1}, {"\u9b3c\u7caa": 1}], [{"\u4e8c\u6c22": 1, "\u6d53\u7f29\u78b3": 1}, {"\u8150\u85e4": 1}], [{"\u4e8c\u6c22": 1, "\u6c1a": 1}, {"\u6c18": 1}], [{"\u94c1\u6c27\u4f53\u7c89\u672b": 1, "\u78b3": 1}, {"\u78c1\u5316\u94c1\u6c27\u4f53": 1}], [{"\u94c1\u6c27\u4f53\u7c89\u672b": 1, "\u6d53\u7f29\u78b3": 1}, {"\u78c1\u5316\u94c1\u6c27\u4f53": 2}], [{"\u7eaf\u94c1\u6c27\u4f53": 1, "\u78b3": 1}, {"\u78c1\u5316\u94c1\u6c27\u4f53": 2}], [{"\u7eaf\u94c1\u6c27\u4f53": 1, "\u6d53\u7f29\u78b3": 1}, {"\u78c1\u5316\u94c1\u6c27\u4f53": 3}], [{"\u94c1\u6c27\u4f53\u7c89\u672b": 1, "\u6c27\u6c14": 1}, {"\u751f\u9508\u7684\u91d1\u5c5e": 1}], [{"\u7eaf\u94c1\u6c27\u4f53": 1, "\u6c27\u6c14": 1}, {"\u751f\u9508\u7684\u91d1\u5c5e": 2}], [{"\u78b3": 2, "\u6c27\u6c14": 2}, {"\u6d53\u7f29\u78b3": 5}], [{"\u6d53\u7f29\u78b3": 1, "\u6c27\u6c14": 2}, {"\u6d53\u7f29\u78b3": 6}], [{"\u94b4": 2, "\u6c27\u6c14": 2}, {"\u79bb\u5b50\u94b4": 5}]]

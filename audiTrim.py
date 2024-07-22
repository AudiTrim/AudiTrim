import os
import pickle
import json
import sys
import time
import networkx as nx
import matplotlib.pyplot as plt
import re
def getfiles(darpa):
    if darpa == 'theia3':
        files = [
            # 'ta1-theia-e3-official-6r.json', 'ta1-theia-e3-official-6r.json.1',
            #      'ta1-theia-e3-official-6r.json.2',
                 # 'ta1-theia-e3-official-6r.json.3', 'ta1-theia-e3-official-6r.json.4',
                 # 'ta1-theia-e3-official-6r.json.5',
                 'ta1-theia-e3-official-6r.json.6', 'ta1-theia-e3-official-6r.json.7',
                 'ta1-theia-e3-official-6r.json.8',
                 # 'ta1-theia-e3-official-6r.json.9',
                 # 'ta1-theia-e3-official-6r.json.10',
            # 'ta1-theia-e3-official-6r.json.11','ta1-theia-e3-official-6r.json.12'
        ]
        # files = ['ta1-theia-e3-official-6r.json.6', 'ta1-theia-e3-official-6r.json.7',
        #          'ta1-theia-e3-official-6r.json.8',]
        return files

    elif darpa == 'trace3':
        files = ['ta1-trace-e3-official-1.json', 'ta1-trace-e3-official-1.json.1',
                 'ta1-trace-e3-official-1.json.2', 'ta1-trace-e3-official-1.json.3',
                 'ta1-trace-e3-official-1.json.4', 'ta1-trace-e3-official-1.json.5',
                 'ta1-trace-e3-official-1.json.6']
        return files
    elif darpa == 'cadets3':
        files = [
                    'ta1-cadets-e3-official.json',
                    'ta1-cadets-e3-official.json.1',
                    'ta1-cadets-e3-official.json.2',
                    'ta1-cadets-e3-official-1.json',
                    'ta1-cadets-e3-official-1.json.1',
                    'ta1-cadets-e3-official-1.json.2',
                    'ta1-cadets-e3-official-1.json.3',
                    'ta1-cadets-e3-official-1.json.4',
                    'ta1-cadets-e3-official-2.json',
                    'ta1-cadets-e3-official-2.json.1',
                 ]
        return files
    elif darpa == 'clearscope3':
        files = [
                    'ta1-clearscope-e3-official-2.json',
                    'ta1-clearscope-e3-official-2.json.1',
                    'ta1-clearscope-e3-official-2.json.2',
                    'ta1-clearscope-e3-official-2.json.3',
                    'ta1-clearscope-e3-official-2.json.4',
                    'ta1-clearscope-e3-official-2.json.5',
                    'ta1-clearscope-e3-official-2.json.6',
                    'ta1-clearscope-e3-official-2.json.7',
                    'ta1-clearscope-e3-official-2.json.8',
                    'ta1-clearscope-e3-official-2.json.9',
                    'ta1-clearscope-e3-official-2.json.10',
                    'ta1-clearscope-e3-official-2.json.11',
                    'ta1-clearscope-e3-official-2.json.12',
                    'ta1-clearscope-e3-official-2.json.13',
                    'ta1-clearscope-e3-official-2.json.14',
                    'ta1-clearscope-e3-official-2.json.15',
                    'ta1-clearscope-e3-official-2.json.16',
                    'ta1-clearscope-e3-official-2.json.17',
                    'ta1-clearscope-e3-official-2.json.18',
                    'ta1-clearscope-e3-official-2.json.19',
                    'ta1-clearscope-e3-official-2.json.20',
                    'ta1-clearscope-e3-official-2.json.21',
                    'ta1-clearscope-e3-official-2.json.22',
                    'ta1-clearscope-e3-official-2.json.23',
                    'ta1-clearscope-e3-official-2.json.24',
                    'ta1-clearscope-e3-official-2.json.25',
                    'ta1-clearscope-e3-official-2.json.26',
                    'ta1-clearscope-e3-official-2.json.27',
                    'ta1-clearscope-e3-official-2.json.28',
                 ]
        return files
    elif darpa == 'cadets5':
        files = [
            'ta1-cadets-1-e5-official-2.bin.json',
            'ta1-cadets-1-e5-official-2.bin.json.1',
            'ta1-cadets-1-e5-official-2.bin.1.json',
            'ta1-cadets-1-e5-official-2.bin.1.json.1',
            'ta1-cadets-1-e5-official-2.bin.2.json',
            'ta1-cadets-1-e5-official-2.bin.2.json.1',
            'ta1-cadets-1-e5-official-2.bin.3.json',
            'ta1-cadets-1-e5-official-2.bin.3.json.1',
            'ta1-cadets-1-e5-official-2.bin.4.json',
            'ta1-cadets-1-e5-official-2.bin.4.json.1',
            'ta1-cadets-1-e5-official-2.bin.5.json',
            'ta1-cadets-1-e5-official-2.bin.5.json.1',
        ]
        return files
    elif darpa == 'theia5':
        files = [
            'ta1-theia-1-e5-official-1.json',
            'ta1-theia-1-e5-official-1.json.1',
            'ta1-theia-1-e5-official-1.json.2',
        ]
        return files
    elif darpa == 'trace5':
        files = [
            'ta1-trace-1-e5-official-1.bin.1.json',
            'ta1-trace-1-e5-official-1.bin.1.json.1',
            'ta1-trace-1-e5-official-1.bin.2.json',
            'ta1-trace-1-e5-official-1.bin.2.json.1',
            'ta1-trace-1-e5-official-1.bin.3.json',
            'ta1-trace-1-e5-official-1.bin.3.json.1',
        ]
        return files
    return []
events = {'EVENT_OPEN': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    'EVENT_WRITE': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    'EVENT_MMAP': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.MemoryObject'),
    # 'EVENT_READ': (
    # 'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    'EVENT_READ': (
    'com.bbn.tc.schema.avro.cdm18.FileObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_CONNECT': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_SENDTO': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    # 'EVENT_RECVFROM': (
    # 'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_RECVFROM': (
    'com.bbn.tc.schema.avro.cdm18.NetFlowObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_MPROTECT': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.MemoryObject'),
    'EVENT_CLONE': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_UNLINK': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    'EVENT_SHM': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.MemoryObject'),
    'EVENT_MODIFY_FILE_ATTRIBUTES': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    # 'EVENT_RECVMSG': (
    # 'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_RECVMSG': (
    'com.bbn.tc.schema.avro.cdm18.NetFlowObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_WRITE_SOCKET_PARAMS': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    # 'EVENT_READ_SOCKET_PARAMS': (
    # 'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_READ_SOCKET_PARAMS': (
    'com.bbn.tc.schema.avro.cdm18.NetFlowObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_EXECUTE': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    'EVENT_SENDMSG': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject')}
event_type = \
    {'EVENT_UPDATE': -1,
     'EVENT_UNLINK': 17,
     'EVENT_CONNECT': 12,
     'EVENT_BOOT': 0,
     'EVENT_OPEN': 1,
     'EVENT_RECVMSG': 7,
     'EVENT_SENDMSG': 5,
     'EVENT_SHM': 16,
     'EVENT_MPROTECT': 11,
     'EVENT_SENDTO': 3,
     'EVENT_READ': 2,
     'EVENT_READ_SOCKET_PARAMS': 14,
     'EVENT_RECVFROM': 4,
     'EVENT_MODIFY_FILE_ATTRIBUTES': 15,
     'EVENT_CLONE': 9,
     'EVENT_EXECUTE': 10,
     'EVENT_MMAP': 8,
     'EVENT_WRITE': 6,
     'EVENT_WRITE_SOCKET_PARAMS': 13
     }
cadets_event_type = {'EVENT_WRITE': 1,
                   'EVENT_READ': 0,
                   'EVENT_CHANGE_PRINCIPAL': 10,
                   'EVENT_EXECUTE': 5,
                   'EVENT_LSEEK': 9,
                   'EVENT_OPEN': 6,
                   'EVENT_EXIT': 2,
                   'EVENT_RECVFROM': 18,
                   'EVENT_ACCEPT': 22,
                   'EVENT_UNLINK': 13,
                   'EVENT_TRUNCATE': 12,
                   'EVENT_RECVMSG': 25,
                   'EVENT_MODIFY_PROCESS': 8,
                   'EVENT_CLOSE': 4,
                   'EVENT_FCNTL': 23,
                   'EVENT_RENAME': 20,
                   'EVENT_OTHER': 27,
                   'EVENT_FORK': 3,
                   'EVENT_SENDMSG': 24,
                   'EVENT_SIGNAL': 15,
                   'EVENT_SENDTO': 17,
                   'EVENT_CREATE_OBJECT': 11,
                   'EVENT_BIND': 14,
                   'EVENT_CONNECT': 16,
                   'EVENT_MMAP': 7,
                   'EVENT_MODIFY_FILE_ATTRIBUTES': 19,
                   'EVENT_FLOWS_TO': 21,
                   'EVENT_LINK': 26
                   }
clearscope_event_type = {'EVENT_UPDATE': -1,
     'EVENT_UNLINK': 17,
     'EVENT_CONNECT': 12,
     'EVENT_BOOT': 0,
     'EVENT_OPEN': 1,
     'EVENT_RECVMSG': 7,
     'EVENT_SENDMSG': 5,
     'EVENT_SHM': 16,
     'EVENT_MPROTECT': 11,
     'EVENT_SENDTO': 3,
     'EVENT_READ': 2,
     'EVENT_READ_SOCKET_PARAMS': 14,
     'EVENT_RECVFROM': 4,
     'EVENT_MODIFY_FILE_ATTRIBUTES': 15,
     'EVENT_CLONE': 9,
     'EVENT_EXECUTE': 10,
     'EVENT_MMAP': 8,
     'EVENT_WRITE': 6,
     'EVENT_WRITE_SOCKET_PARAMS': 13
     }
node_type = {'com.bbn.tc.schema.avro.cdm18.Subject': 0,
             'com.bbn.tc.schema.avro.cdm18.NetFlowObject': 2,
             'com.bbn.tc.schema.avro.cdm18.FileObject': 3,
             'com.bbn.tc.schema.avro.cdm18.MemoryObject': 1
             }



def processCadets3(darpa='cadets3'):
    files_attack_nodes = [
        [
            '/usr/log/devc',
            '/tmp/vUgefal',
            '/etc/passwd',
            '/etc/group',
        ],
        [
            'tmp/grain',
            '/etc/group',
            '/etc/passwd',
            'vUgefal',
        ],
        [
            'tmux-1002',
            'vUgefal',
            'XIM',
            'mission',
            'netlog',
            'sendmail',
            'grain',
            'test'
        ],
        [
            '/tmp/pEja72mA',
            '/tmp/memhelp.so',
            '/tmp/done.so'
        ]
        #
        # '/var/log/devc',
        # '/etc/passwd',
        # '/etc/group',
        # '/usr/log/devc'
        #
        # '/tmp/minions',
        # '/tmp/test',
        # '/var/log/sendmail',
        # 'tmp/grain',
        # '/var/log/sendmail.st',
    ]
    networks_attack_nodes = [
        [
            '81.49.200.166',
            '61.167.39.128',
            '78.205.235.65',
            '139.123.0.113',
            '200.36.109.214',
            '154.145.113.18',
        ],
        [
            '155.162.39.48',
            '25.159.96.207',
            '76.56.184.25',
            '198.115.236.119',
        ],
        [
            '25.159.96.207',
            '53.158.101.118',
            '155.162.39.48',
            '76.56.184.25',
            '198.115.236.119',
        ],
        [
            '25.159.96.207',
            '76.56.184.25',
            '53.158.101.118',
            '155.162.39.48',
        ]
    ]
    subjects_attack_nodes = [
        [
            # 'nginx',
            'test',
            'exploit',
            'vUgefal'
        ],
        [
            # 'nginx',
            'test',
            'exploit',
            'vUgefal'
        ],
        [
            'test',
            'main',
            'main',
            'XIM',
            'tmux-1002',
        ],
        [
            # 'nginx',
            'test',
            'main',
            'ssh',
            'whoami',
            'pEja72mA',
        ]

    ]
    timestamp = [
        [1523029224, 1523048424],
        [1523480424, 1523473224],
        [1523556024, 1523563224],
        [1523625624, 1523631624],
        [1800000000, 1900000000]
    ]
    time_index = 0

    print("process")
    filelist = getfiles(darpa)
    # subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
    # networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    # files = pickle.load(open(darpa + '/files.pkl', 'rb'))
    # host = '83C8ED1F-5045-DBCD-B39F-918F0DF4F851'
    # anomaly_nodes = pickle.load(open(darpa+'/anomaly_nodes.pkl', 'rb'))



    subjects = {}
    networks = {}
    files = {}
    host = ''
    anomaly_nodes = {}
    anomaly_events = {}


    vicinity = {}

    cnt = 0
    count = 0
    code = -1
    total = 0

    ccnt = 0
    cccnt = 0
    for i in filelist:
        code += 1
        print(i + '----------------------------------------------')
        file = open('../darpa/'+darpa+'/'+i, 'r')
        line = file.readline()
        times = 0
        new_data = []
        neighbor = {}

        while line:
            times += 1
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
                cnt += 1
                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue
                try:
                    if host != re.findall('"hostId":"(.*?)"', line)[0]:
                        line = file.readline()
                        continue
                except:
                    line = file.readline()
                    continue

                eid = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['uuid']
                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 1000000000.0
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                try:
                    cmd = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['name']['string']
                except:
                    cmd = ''
                try:
                    path = re.findall('"exec":"(.*?)"', line)[0]
                except:
                    path = ''

                if sub not in subjects:
                    subjects[sub] = ['', '', '']


                if sub in subjects:
                    subjects[sub][0] = path
                    subjects[sub][1] = cmd

                if pre1 in files and files[pre1] == '':

                    if '"predicateObjectPath":null,' not in line and '<unknown>' not in line:
                        try:
                            path_name = re.findall('"predicateObjectPath":{"string":"(.*?)"', line)[0]
                            files[pre1] = path_name
                        except:
                            print(line)
                            print(data)
                            print(data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'))
                            return

                if types == 'EVENT_CLONE':
                    subjects[pre1][2] = sub

                if types == 'EVENT_BOOT':
                    line = file.readline()
                    continue

                if not cadets_event_type.__contains__(types):
                    line = file.readline()
                    continue

                if pre1 not in files and pre1 not in networks and pre1 not in subjects:
                    line = file.readline()
                    continue

                tmp = count
                if time > timestamp[time_index][0]:
                    time_index += 1
                if time_index > 0 and time < timestamp[time_index-1][1]:

                    if subjects[sub][0] in subjects_attack_nodes[time_index-1]:
                        count += 1
                        anomaly_events[eid] = 0
                        if sub not in anomaly_nodes:
                            anomaly_nodes[sub] = 0
                        if pre1 not in anomaly_nodes:
                            anomaly_nodes[pre1] = 0
                        anomaly_nodes[sub] += 1
                        anomaly_nodes[pre1] += 1

                    elif pre1 in networks and tmp == count:
                        # if subjects[sub][0] == other_nodes:
                        for k in networks_attack_nodes[time_index-1]:
                            if k in networks[pre1]:
                                count += 1
                                anomaly_events[eid] = 0
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                    elif pre1 in files and tmp == count:
                        # if subjects[sub][0] == other_nodes:
                        for k in files_attack_nodes[time_index-1]:
                            if k in files[pre1]:
                                count += 1
                                anomaly_events[eid] = 0
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                    # if sub in anomaly_nodes and tmp == count:
                    #     count += 1
                    #     if sub not in anomaly_nodes:
                    #         anomaly_nodes[sub] = 0
                    #     if pre1 not in anomaly_nodes:
                    #         anomaly_nodes[pre1] = 0
                    #     anomaly_nodes[sub] += 1
                    #     anomaly_nodes[pre1] += 1


                subject = sub
                object = pre1
                if sub not in vicinity:
                    vicinity[subject] = []
                if 'REC' in types or 'READ' in types or 'EXECUTE' in types:
                    a = pre1
                    pre1 = sub
                    sub = a

                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    new_data.append([pre1, sub, 'EVENT_READ', time])
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    line = file.readline()
                    continue

                # OUR METHOD
                if sub not in neighbor:
                    neighbor[sub] = {}
                if pre1 not in neighbor:
                    neighbor[pre1] = {}
                try:

                    if pre1 not in neighbor[sub]:
                        neighbor[sub][pre1] = (time, types)
                        if sub not in neighbor[pre1]:
                            neighbor[pre1] = {}
                        else:
                            neighbor[pre1] = {sub: neighbor[pre1][sub]}
                        new_data.append([sub, pre1, types, time])
                    elif time - neighbor[sub][pre1][0] > 1 or neighbor[sub][pre1][1] != types:
                        neighbor[sub][pre1] = (time, types)
                        neighbor[pre1] = {}
                        new_data.append([sub, pre1, types, time])
                except:
                    print(neighbor)
                    print(neighbor[sub])
                    print(neighbor[sub][pre1])
                    return



            else:
                if not data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.MemoryObject'):
                    uid = re.findall('"uuid":"(.*?)"', line)[0]
                if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Host'):
                    if host == '':
                        host = data['datum']['com.bbn.tc.schema.avro.cdm18.Host']['uuid']
                        print(host)
                    else:
                        print(data)
                elif re.findall('"hostId":"(.*?)"', line)[0] != host:
                    line = file.readline()
                    continue

                if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Subject'):

                    if subjects.__contains__(data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']):
                        line = file.readline()
                        continue
                    if data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'] is None:
                        parentUid =''
                    else:
                        parentUid = data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    if not subjects.__contains__(parentUid):
                        parentUid = ''
                    try:
                        path = re.findall('"path":"(.*?)"', line)[0]
                        cmdline = re.findall('"string":"(.*?)"', line)[0]

                    except:
                        path = ''
                        cmdline = ''
                    subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = [path, cmdline, parentUid]
                elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.FileObject'):
                    files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = ''

                elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.NetFlowObject'):
                    networks[data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['uuid']] = data['datum'][
                        'com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remoteAddress'] + '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remotePort']) + '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localAddress'])+ '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localPort'])
            line = file.readline()

        prune_data = []
        _neighbor = {}
        num = len(new_data)
        for i in range(num - 1, -1, -1):
            time = new_data[i][3]
            oid = new_data[i][0]
            pid = new_data[i][1]
            types = new_data[i][2]
            if pid not in _neighbor:
                _neighbor[pid] = {}
            if oid not in _neighbor:
                _neighbor[oid] = {}
            if oid not in _neighbor[pid]:
                _neighbor[pid][oid] = (time, types)
                _neighbor[oid] = {}
                prune_data.append(new_data[i])
            elif _neighbor[pid][oid][0] - time > 1 or _neighbor[pid][oid][1] != types:
                _neighbor[pid][oid] = (time, types)
                _neighbor[oid] = {}
                prune_data.append(new_data[i])

            else:
                _neighbor[pid][oid] = time

        new_data = []
        num = len(prune_data)
        for i in range(num - 1, -1, -1):
            new_data.append(prune_data[i])
        for i in new_data:
            vicinity[i[0]].append((i[2], i[3], i[1]))

        num = len(new_data)
        print(num)
        total += num
        pickle.dump(new_data, open(darpa + '/'+darpa+'_'+str(code)+'.pkl', 'wb'))

    pickle.dump(subjects, open(darpa+'/subjects.pkl', 'wb'))
    pickle.dump(networks, open(darpa+'/networks.pkl', 'wb'))
    pickle.dump(files, open(darpa+'/files.pkl', 'wb'))
    pickle.dump(vicinity, open(darpa + '/vicinity.pkl', 'wb'))
    pickle.dump(anomaly_events, open(darpa + '/anomaly_events.pkl', 'wb'))
    pickle.dump(anomaly_nodes, open(darpa + '/anomaly_nodes.pkl', 'wb'))
    print("the num of events: " + str(cnt))
    print("the num of entries: " + str(times))
    print("After AudiTrim: " + str(total))


def processTheia3(darpa='theia3'):
    files_attack_nodes = [
        [
            'gtcache',
            'libdrakon.linux.x64.so',
            '/home/admin/clean',
            '/dev/glx_alsa_675',
            '/home/admin/profile',
            '/var/log/xdev',
            '/var/log/wdev',
            '/var/log/mail',
            '/tmp/memtrace.so'
        ],
        [
            'tcexec'
        ]

    ]
    networks_attack_nodes = [
        [
            '141.43.176.203',
            '104.228.117.21',
            '149.52.198.23',
            '5.214.163.155',
            '146.153.68.151',

        ],
        [

        ]

    ]
    subjects_attack_nodes = [
        [
            'whoami',
            'ps',
            '/home/admin/clean',
            'home/admin/profile',
            '/home/admin/profile (deleted)',
            '/home/admin/clean (deleted)'
            '/etc/firefox/native-messaging-hosts/gtcache'
            '/var/log/mail'
        ],
        [
            'whoami',
            'ps',
            '/home/admin/clean',
            'home/admin/profile',
            '/home/admin/profile (deleted)',
            '/home/admin/clean (deleted)'
            '/etc/firefox/native-messaging-hosts/gtcache'
            'tcexec',
        ]


    ]
    timestamp = [
        [1523551473, 1523560833],
        [1523643633, 1523647833],
        [1800000000, 1900000000]
    ]
    time_index = 0
    print("process")
    filelist = getfiles(darpa)
    subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
    networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    files = pickle.load(open(darpa + '/files.pkl', 'rb'))

    # subjects = {}
    # networks = {}
    # files = {}
    hasshow = {}

    all_vicinity = {}
    vicinity = {}
    # host = ''
    host = '0A00063C-5254-00F0-0D60-000000000070'
    nodes = {}
    cnt = 0
    count = 0
    code = -1
    anomaly_nodes = {}

    for i in filelist:
        time_limit_exceed = 0
        code += 1
        print(i + '----------------------------------------------')
        file = open('../darpa/' + darpa + '/' + i, 'r')
        line = file.readline()
        times = 0
        new_data = []
        neighbor = {}
        while line:
            times += 1
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
                cnt += 1
                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or \
                        data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue
                try:
                    if host != re.findall('"hostId":"(.*?)"', line)[0]:
                        line = file.readline()
                        continue
                except:
                    line = file.readline()
                    continue



                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 1000000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']

                if sub not in all_vicinity:
                    all_vicinity[sub] = []
                all_vicinity[sub].append([types, pre1, time])
                line = file.readline()
                continue

                if sub not in subjects:
                    line = file.readline()
                    continue
                if types == 'EVENT_CLONE':
                    subjects[pre1][2] = sub

                if types == 'EVENT_BOOT':
                    line = file.readline()
                    continue

                if not clearscope_event_type.__contains__(types):
                    line = file.readline()
                    continue

                if pre1 not in files and pre1 not in networks and pre1 not in subjects:
                    line = file.readline()
                    continue

                tmp = count
                if time > timestamp[time_index][0]:
                    time_index += 1
                if time_index > 0 and time < timestamp[time_index - 1][1]:

                    if subjects[sub][0] in subjects_attack_nodes[time_index - 1]:
                        count += 1
                        if sub not in anomaly_nodes:
                            anomaly_nodes[sub] = 0
                        if pre1 not in anomaly_nodes:
                            anomaly_nodes[pre1] = 0
                        anomaly_nodes[sub] += 1
                        anomaly_nodes[pre1] += 1

                    elif pre1 in networks and tmp == count:
                        # if subjects[sub][0] == other_nodes:
                        for k in networks_attack_nodes[time_index - 1]:
                            if k in networks[pre1]:
                                count += 1
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                    elif pre1 in files and tmp == count:
                        # if subjects[sub][0] == other_nodes:
                        for k in files_attack_nodes[time_index - 1]:
                            if k in files[pre1]:
                                count += 1
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                subject = sub
                object = pre1
                if sub not in vicinity:
                    vicinity[subject] = []
                if 'REC' in types or 'READ' in types or 'EXECUTE' in types:
                    a = pre1
                    pre1 = sub
                    sub = a

                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    new_data.append([pre1, sub, 'EVENT_READ', time])
                    vicinity[subject].append(('EVENT_READ', time, pre1))
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    vicinity[subject].append(('EVENT_WRITE', time, pre2))
                    line = file.readline()
                    continue

                vicinity[subject].append((types, time, object))
                line = file.readline()
                continue
                # OUR METHOD
                if sub not in neighbor:
                    neighbor[sub] = {}
                if pre1 not in neighbor:
                    neighbor[pre1] = {}
                try:

                    if pre1 not in neighbor[sub]:
                        neighbor[sub][pre1] = (time, types)
                        if sub not in neighbor[pre1]:
                            neighbor[pre1] = {}
                        else:
                            neighbor[pre1] = {sub: neighbor[pre1][sub]}
                        new_data.append([sub, pre1, types, time])
                        vicinity[subject].append((types, time, object))
                    elif time - neighbor[sub][pre1][0] > 1 or neighbor[sub][pre1][1] != types:
                        neighbor[sub][pre1] = (time, types)
                        neighbor[pre1] = {}
                        new_data.append([sub, pre1, types, time])
                        vicinity[subject].append((types, time, object))
                except:
                    print(neighbor)
                    print(neighbor[sub])
                    print(neighbor[sub][pre1])
                    return

            else:
                line = file.readline()
                continue
                if not data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.MemoryObject'):
                    uid = re.findall('"uuid":"(.*?)"', line)[0]
                    nodes[uid] = line
                if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Host'):
                    if host == '':
                        host = data['datum']['com.bbn.tc.schema.avro.cdm18.Host']['uuid']
                        print(host)
                    else:
                        print(data)
                elif re.findall('"hostId":"(.*?)"', line)[0] != host:
                    line = file.readline()
                    continue

                if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Subject'):
                    if subjects.__contains__(data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']):
                        line = file.readline()
                        continue
                    if data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'] is None:
                        parentUid =''
                    else:
                        parentUid = data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    if subjects.__contains__(parentUid):
                        # parentUid = subjects[parentUid]
                        pass
                    else:
                        parentUid = ''
                    try:
                        path = re.findall('"path":"(.*?)"', line)[0]
                        cmdline = re.findall('"string":"(.*?)"', line)[0]
                        subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = [path, cmdline, parentUid]
                    except:
                        subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = ['', '', parentUid]
                elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.FileObject'):

                    filename = re.findall('"filename":"(.*?)"', line)
                    if len(filename)==1:
                        files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = filename[0]
                    else:
                        try:
                            localPrincipal = re.findall('"localPrincipal":{"com.bbn.tc.schema.avro.cdm18.UUID":"(.*?)"', line)[0]
                            filename = subjects[localPrincipal][0]
                            files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = filename
                        except:
                            files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = 'null'
                            # return
                elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.NetFlowObject'):
                    networks[data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['uuid']] = data['datum'][
                        'com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remoteAddress'] + '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remotePort']) + '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localAddress'])+ '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localPort'])

            line = file.readline()

        # pickle.dump(new_data, open(darpa + '/'+darpa+'_'+str(code)+'.pkl', 'wb'))
        # print(len(new_data))
    print(cnt)
    # pickle.dump(subjects, open(darpa + '/subjects.pkl', 'wb'))
    # pickle.dump(networks, open(darpa + '/networks.pkl', 'wb'))
    # pickle.dump(files, open(darpa + '/files.pkl', 'wb'))
    # pickle.dump(vicinity, open(darpa + '/vicinity.pkl', 'wb'))
    pickle.dump(all_vicinity, open(darpa + '/all_vicinity.pkl', 'wb'))

    # pickle.dump(nodes, open(darpa + '/nodes.pkl', 'wb'))
    # pickle.dump(anomaly_nodes, open(darpa + '/anomaly_nodes.pkl', 'wb'))


def processClearScope3(darpa='clearscope3'):

    files_attack_nodes = [
        [
            '/tmp/vUgefal',
            'credentials',
            'drakon',
        ],
        [
            'drakon',
            'shellcode',
            'csb.tracee',
            'libdrakon.android.arm32',
        ],
        [
            'tmp18d17sn1',
            '/data/data/org.mozilla.fennec_firefox_dev/shared_lib',
            '424',
        ],
        [
            'MsgApp',
            'screen',
            'MetaApp',
        ]
    ]
    networks_attack_nodes = [
        [
            '208.75.117.3',
            '208.75.117.2',
            '62.83.155.175',
         ],
        [
            '153.178.46.202',
            '111.82.111.27',
            '166.199.230.185',
            '188.167.106.122',
            '140.57.183.17',
            '193.72.18.131',
        ],
        [
            '153.178.46.202',
            '111.82.111.27',
            '166.199.230.185',
            '188.167.106.122',
            '140.57.183.17',
            '193.72.18.131',
        ],
        [
            '53.157.70.118'
        ]

    ]
    subjects_attack_nodes = [
        [
            'credentials',
            'vUgefal',
            'phishing',
            'putfile',
        ],
        [
            '/data/data/org.mozilla.fennec_firefox_dev/shared_files',
            '/data/local/tmp',
            'csb.tracee.27331.27355',
            '/data/data/org.mozilla.fennec_firefox_dev/csb.tracee.27331.27355',
            'drakon',
            'libdrakon.android.arm32',
        ],
        [
            '/data/data/org.mozilla.fennec_firefox_dev/shared_lib',
            '/data/data/org.mozilla.fennec_firefox_dev/lib',
            'putfile',
            'whoami',
            'com.metasploit.stage'
        ],
        [
            'com.metasploit.stage',
            'com.android.camera2'

        ]
    ]
    timestamp = [
        [1523041224, 1523048424],
        [1523469624, 1523478624],
        [1523563224, 1523566824],
        [1523631624, 1523649624],
        [1800000000, 1900000000]

    ]

    print("process")
    filelist = getfiles(darpa)
    subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
    networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    files = pickle.load(open(darpa + '/files.pkl', 'rb'))

    # subjects = {}
    # networks = {}
    # files = {}
    time_index = 0
    hasshow = {}

    vicinity = {}
    host = '5957F7A8-2EAB-D99C-459A-408A1F427D29'
    nodes = {}
    cnt = 0
    count = 0
    code = -1
    anomaly_nodes = {}

    for i in filelist:
        time_limit_exceed = 0
        code += 1
        print(i + '----------------------------------------------')
        file = open('../darpa/'+darpa+'/'+i, 'r')
        line = file.readline()
        times = 0
        new_data = []
        neighbor = {}
        while line:
            times += 1
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
                cnt += 1
                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue
                try:
                    if host != re.findall('"hostId":"(.*?)"', line)[0]:
                        line = file.readline()
                        continue
                except:
                    line = file.readline()
                    continue

                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 1000000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                if time > 1800000000 or str(time)[:3] != '152':
                    line = file.readline()
                    time_limit_exceed += 1
                    continue
                if types == 'EVENT_CLONE':
                    subjects[pre1][2] = sub

                if types == 'EVENT_BOOT':
                    line = file.readline()
                    continue

                if not clearscope_event_type.__contains__(types):
                    line = file.readline()
                    continue

                if pre1 not in files and pre1 not in networks and pre1 not in subjects:
                    line = file.readline()
                    continue

                tmp = count
                if time > timestamp[time_index][0]:
                    time_index += 1
                if time_index > 0 and time < timestamp[time_index - 1][1]:


                    if subjects[sub][0] in subjects_attack_nodes[time_index - 1]:
                        count += 1
                        if sub not in anomaly_nodes:
                            anomaly_nodes[sub] = 0
                        if pre1 not in anomaly_nodes:
                            anomaly_nodes[pre1] = 0
                        anomaly_nodes[sub] += 1
                        anomaly_nodes[pre1] += 1

                    elif pre1 in networks and tmp == count:
                        # if subjects[sub][0] == other_nodes:
                        for k in networks_attack_nodes[time_index - 1]:
                            if k in networks[pre1]:
                                count += 1
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                    elif pre1 in files and tmp == count:
                        # if subjects[sub][0] == other_nodes:
                        for k in files_attack_nodes[time_index - 1]:
                            if k in files[pre1]:
                                count += 1
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break



                subject = sub
                object = pre1
                if sub not in vicinity:
                    vicinity[subject] = []
                if 'REC' in types or 'READ' in types or 'EXECUTE' in types:
                    a = pre1
                    pre1 = sub
                    sub = a

                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    new_data.append([pre1, sub, 'EVENT_READ', time])
                    vicinity[subject].append(('EVENT_READ', time, pre1))
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    vicinity[subject].append(('EVENT_WRITE', time, pre2))
                    line = file.readline()
                    continue
                # OUR METHOD
                if sub not in neighbor:
                    neighbor[sub] = {}
                if pre1 not in neighbor:
                    neighbor[pre1] = {}
                try:

                    if pre1 not in neighbor[sub]:
                        neighbor[sub][pre1] = (time, types)
                        if sub not in neighbor[pre1]:
                            neighbor[pre1] = {}
                        else:
                            neighbor[pre1] = {sub: neighbor[pre1][sub]}
                        new_data.append([sub, pre1, types, time])
                        vicinity[subject].append((types, time, object))
                    elif time - neighbor[sub][pre1][0] > 1 or neighbor[sub][pre1][1] != types:
                        neighbor[sub][pre1] = (time, types)
                        neighbor[pre1] = {}
                        new_data.append([sub, pre1, types, time])
                        vicinity[subject].append((types, time, object))
                except:
                    print(neighbor)
                    print(neighbor[sub])
                    print(neighbor[sub][pre1])
                    return

            else:
                line = file.readline()
                continue
                # if not data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.MemoryObject'):
                #     uid = re.findall('"uuid":"(.*?)"', line)[0]
                #     nodes[uid] = line
                if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Host'):
                    if host == '':
                        host = data['datum']['com.bbn.tc.schema.avro.cdm18.Host']['uuid']
                        print(host)
                    else:
                        print(data)
                # elif
                #     line = file.readline()
                #     continue

                if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Subject'):
                    if re.findall('"hostId":"(.*?)"', line)[0] != host:
                        line = file.readline()
                        continue
                    if subjects.__contains__(data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']):
                        line = file.readline()
                        continue
                    if data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'] is None:
                        parentUid =''
                    else:
                        parentUid = data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    cmdline = re.findall('"string":"(.*?)"', line)[0]
                    try:
                        path = re.findall('"path":"(.*?)"', line)[0]

                    except:
                        path = ''

                    subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = [path, cmdline, parentUid]
                elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.FileObject'):
                    if re.findall('"hostId":"(.*?)"', line)[0] != host:
                        line = file.readline()
                        continue
                    path = re.findall('"path":"(.*?)"', line)[0]
                    files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = path

                    # filename = re.findall('"filename":"(.*?)"', line)
                    # if len(filename)==1:
                    #     files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = filename[0]
                    # else:
                    #     try:
                    #         localPrincipal = re.findall('"localPrincipal":{"com.bbn.tc.schema.avro.cdm18.UUID":"(.*?)"', line)[0]
                    #         print(data)
                    #         filename = subjects[localPrincipal][0]
                    #         files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = filename
                    #     except:
                    #         files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = 'null'
                elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.NetFlowObject'):
                    if re.findall('"hostId":"(.*?)"', line)[0] != host:
                        line = file.readline()
                        continue
                    networks[data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['uuid']] = data['datum'][
                        'com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remoteAddress'] + '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remotePort']) + '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localAddress'])+ '/' + str(
                        data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localPort'])

            line = file.readline()
        num = len(new_data)
        print(num)
        print(time_limit_exceed)

        pickle.dump(new_data, open(darpa+'/'+darpa+'_'+str(code)+'.pkl', 'wb'))

    print(cnt)
    print(count)
    print(len(anomaly_nodes))
    cnt = 0
    for i in subjects:
        if subjects[i][0] != '':
            cnt += 1
    print(cnt)
    print(len(subjects)-cnt)

    cnt = 0
    for i in files:
        if files[i] != '':
            cnt += 1
    print(cnt)
    print(len(files) - cnt)

    pickle.dump(subjects, open(darpa+'/subjects.pkl', 'wb'))
    pickle.dump(networks, open(darpa+'/networks.pkl', 'wb'))
    pickle.dump(files, open(darpa+'/files.pkl', 'wb'))
    pickle.dump(vicinity, open(darpa + '/vicinity.pkl', 'wb'))
    pickle.dump(nodes, open(darpa + '/nodes.pkl', 'wb'))
    pickle.dump(anomaly_nodes, open(darpa + '/anomaly_nodes.pkl', 'wb'))

def cpr(darpa):
    files = getfiles(darpa)
    code = 0
    first = {}
    _in = {}
    _out = {}
    total = 0
    for i in files:
        print(i + '----------------------------------------------')
        file = open('../darpa/'+darpa+'/'+i, 'r')
        new_file = open('../darpa/'+darpa+'/'+'new'+i, 'w')
        line = file.readline()
        times = 0
        new_data = []
        nodes = {}
        while line:
            times += 1
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue
                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']

                if 'REC' in types or 'READ' in types:
                    a = pre1
                    pre1 = sub
                    sub = a
                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    new_data.append([pre1, sub, 'EVENT_READ', time])
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    new_file.write(line)
                    if pre1 not in nodes:
                        nodes[pre1] = 1
                    if sub not in nodes:
                        nodes[sub] = 1
                    if pre2 not in nodes:
                        nodes[pre2] = 1
                    line = file.readline()
                    continue
                if sub not in _in:
                    _in[sub] = {}
                if sub not in _out:
                    _out[sub] = {}
                if pre1 not in _in:
                    _in[pre1] = {}
                if pre1 not in _out:
                    _out[pre1] = {}
                if pre1 in _out[sub] and sub in _in[pre1]:
                    line = file.readline()
                    continue
                else:
                    _out[sub][pre1] = 0
                    _in[pre1][sub] = 0
                    _out[pre1] = {}
                    _in[sub] = {}
                    new_data.append([sub, pre1, types, time])
                    new_file.write(line)
            else:
                line = new_file.write(line)
            line = file.readline()
        num = len(new_data)
        total += num
        code += 1
    print("After CPR: " + str(total))

def fulldependency(darpa):
    files = getfiles(darpa)
    code = 0
    total = 0
    first = {}
    for i in files:
        print(i + '----------------------------------------------')
        file = open('../darpa/'+darpa+'/'+i, 'r')
        line = file.readline()
        times = 0
        new_data = []
        neighbor = {}
        last = {}
        while line:
            times += 1
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue
                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']

                if 'REC' in types or 'READ' in types:
                    a = pre1
                    pre1 = sub
                    sub = a
                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    new_data.append([pre1, pre2, 'EVENT_UPDATE', time])
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    line = file.readline()
                    continue

                if sub in last and last[sub] == pre1:
                    line = file.readline()
                    continue
                last[sub] = pre1
                if pre1 in last and last[pre1] == sub:
                    pass
                else:
                    last[pre1] = ''


                if sub not in neighbor:
                    neighbor[sub] = {}
                if pre1 not in neighbor[sub]:
                    neighbor[sub][pre1] = time
                    neighbor[pre1] = {}
                    new_data.append([sub, pre1, types, time])
                elif time - neighbor[sub][pre1] > 10 and False:
                    neighbor[sub][pre1] = time
                    neighbor[pre1] = {}
                    new_data.append([sub, pre1, types, time])
                else:
                    neighbor[sub][pre1] = time
                    if types not in first:
                        first[types] = 1
                    else:
                        first[types] += 1
            else:
                pass
            line = file.readline()
        num = len(new_data)
        total += num
        pickle.dump(new_data, open('../darpa/'+darpa+'/edge_fd_'+str(code)+'.pkl', 'wb'))
        code += 1
    print("After F-DPR: " + str(total))

def globalsemantics(darpa):
    files = getfiles(darpa)
    code = 0
    first = {}
    total = 0
    for i in files:
        print(i + '----------------------------------------------')
        file = open('../darpa/'+darpa+'/'+i, 'r')
        line = file.readline()
        times = 0
        new_data = []
        neighbor = {}
        nodes = {}
        all = 0
        while line:
            times += 1
            # if times % 1000000 == 0:
            #     print(times)
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):

                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue

                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']

                if 'REC' in types or 'READ' in types:
                    a = pre1
                    pre1 = sub
                    sub = a
                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    # pre2 = uid_id[pre2]
                    new_data.append([pre1, sub, 'EVENT_READ', time])
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    if pre1 not in nodes:
                        nodes[pre1] = 1
                    if sub not in nodes:
                        nodes[sub] = 1
                    if pre2 not in nodes:
                        nodes[pre2] = 1
                    line = file.readline()
                    continue
                all += 1
                if sub not in neighbor:
                    neighbor[sub] = {}
                if pre1 not in neighbor[sub]:
                    neighbor[sub][pre1] = time
                    neighbor[pre1] = {}
                    new_data.append([sub, pre1, types, time])
                    if sub not in nodes:
                        nodes[sub] = 1
                    if pre1 not in nodes:
                        nodes[pre1] = 1
                elif time - neighbor[sub][pre1] > 10 and False:
                    neighbor[sub][pre1] = time
                    neighbor[pre1] = {}
                    new_data.append([sub, pre1, types, time])
                else:
                    neighbor[sub][pre1] = time
                    if types not in first:
                        first[types] = 1
                    else:
                        first[types] += 1

            else:
                pass
            line = file.readline()
        num = len(new_data)
        total += num
        code += 1
    print("After GlobalSemantic: " + str(total))

'''
flag = True表示开启时间窗口策略
flag = False表示只按照因果依赖进行剪枝
对比工作采用的是基于因果依赖剪枝，没有时间窗口限制，因此对比时将flag设置为False
'''
def auditrim(darpa, flag=False):
    files = getfiles(darpa)
    code = 0
    total = 0
    neighbor = {}
    interval = {}
    tfile = open('../threatrace/d_10_678.txt', 'w')
    for i in files:
        print(i + '----------------------------------------------')
        file = open('../darpa/'+darpa+'/'+i, 'r')
        # new_file = open('../darpa/' + darpa + '/' + 'f_0_cda_' + i, 'w')
        line = file.readline()
        times = 0
        new_data = []
        while line:
            times += 1
            # if times % 1000000 == 0:
            #     print(times)
            data = json.loads(line)
            data = dict(data)

            if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
                if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
                    line = file.readline()
                    continue
                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']

                # if 'MMAP' in types or 'MPROTE' in types:
                #     line = file.readline()
                #     continue

                if 'REC' in types or 'READ' in types:
                    a = pre1
                    pre1 = sub
                    sub = a
                if 'RENAME' in types:
                    pre2 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject2'][
                        'com.bbn.tc.schema.avro.cdm18.UUID']
                    # new_file.write(line)
                    new_data.append([pre1, sub, 'EVENT_READ', time])
                    new_data.append([sub, pre2, 'EVENT_WRITE', time])
                    line = file.readline()
                    continue
                # OUR METHOD
                if sub not in neighbor:
                    neighbor[sub] = {}
                    interval[sub] = {}
                if pre1 not in neighbor:
                    neighbor[pre1] = {}
                    interval[pre1] = {}
                if pre1 not in neighbor[sub]:
                    neighbor[sub][pre1] = time
                    interval[sub][pre1] = 100
                    if sub not in neighbor[pre1]:
                        neighbor[pre1] = {}
                        interval[pre1] = {}
                    else:
                        neighbor[pre1] = {sub: neighbor[pre1][sub]}
                        interval[pre1] = {sub: interval[pre1][sub]}
                    # new_file.write(line)
                    new_data.append([sub, pre1, types, time])
                elif time - neighbor[sub][pre1] >= interval[sub][pre1] and flag:
                    neighbor[sub][pre1] = time
                    neighbor[pre1] = {}
                    if sub not in neighbor[pre1]:
                        neighbor[pre1] = {}
                        interval[pre1] = {}
                    else:
                        neighbor[pre1] = {sub: neighbor[pre1][sub]}
                        interval[pre1] = {sub: interval[pre1][sub]}
                    # new_file.write(line)
                    new_data.append([sub, pre1, types, time])
                else:
                    interval[sub][pre1] = min(100, 2 * (time - neighbor[sub][pre1]) + 0.1)
                    neighbor[sub][pre1] = time
            else:
                pass
            line = file.readline()
        num = len(new_data)
        print(num)
        for l in new_data:
            if l[2] not in events:
                continue
            tfile.write(l[0] + '\t' + events[l[2]][0] + '\t' + l[1] + '\t' + events[l[2]][1] + '\t' + l[2] + '\n')
        # prune_data = []
        # new_neighbor = {}
        # new_interval = {}
        # for i in range(num-1, -1, -1):
        #     time = new_data[i][3]
        #     oid = new_data[i][0]
        #     pid = new_data[i][1]
        #     if pid not in new_neighbor:
        #         new_neighbor[pid] = {}
        #         new_interval[pid] = {}
        #     if oid not in new_neighbor:
        #         new_neighbor[oid] = {}
        #     if oid not in new_neighbor[pid]:
        #         new_neighbor[pid][oid] = time
        #         new_interval[pid][oid] = 100
        #         new_neighbor[oid] = {}
        #         new_interval[oid] = {}
        #         prune_data.append(new_data[i])
        #     elif new_neighbor[pid][oid] - time > new_interval[pid][oid] and flag:
        #         interval[sub][pre1] = 10
        #         new_neighbor[pid][oid] = time
        #         new_neighbor[oid] = {}
        #         prune_data.append(new_data[i])
        #     else:
        #         interval[sub][pre1] = min(100, 2 * (time - neighbor[sub][pre1]) + 0.1)
        #         new_neighbor[pid][oid] = time
        #
        # num = len(prune_data)
        # total += num
        code += 1

    print('After AudiTrim: ' + str(total))



auditrim('theia3', True)

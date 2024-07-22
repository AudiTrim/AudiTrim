import os
import pickle
import json
import sys

import networkx as nx
import matplotlib.pyplot as plt
import re
def getfiles(darpa):
    if darpa == 'theia3':
        files = [
            'ta1-theia-e3-official-6r.json', 'ta1-theia-e3-official-6r.json.1',
                 'ta1-theia-e3-official-6r.json.2',
                 'ta1-theia-e3-official-6r.json.3', 'ta1-theia-e3-official-6r.json.4',
                 'ta1-theia-e3-official-6r.json.5',
                 'ta1-theia-e3-official-6r.json.6', 'ta1-theia-e3-official-6r.json.7',
                 'ta1-theia-e3-official-6r.json.8',
                 'ta1-theia-e3-official-6r.json.9',
                 'ta1-theia-e3-official-6r.json.10','ta1-theia-e3-official-6r.json.11','ta1-theia-e3-official-6r.json.12']
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
    'EVENT_READ': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.FileObject'),
    # 'EVENT_READ': (
    # 'com.bbn.tc.schema.avro.cdm18.FileObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_CONNECT': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_SENDTO': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_RECVFROM': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    # 'EVENT_RECVFROM': (
    # 'com.bbn.tc.schema.avro.cdm18.NetFlowObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
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
    'EVENT_RECVMSG': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    # 'EVENT_RECVMSG': (
    # 'com.bbn.tc.schema.avro.cdm18.NetFlowObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
    'EVENT_WRITE_SOCKET_PARAMS': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    'EVENT_READ_SOCKET_PARAMS': (
    'com.bbn.tc.schema.avro.cdm18.Subject', 'com.bbn.tc.schema.avro.cdm18.NetFlowObject'),
    # 'EVENT_READ_SOCKET_PARAMS': (
    # 'com.bbn.tc.schema.avro.cdm18.NetFlowObject', 'com.bbn.tc.schema.avro.cdm18.Subject'),
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

netThre = 20
netTimes = 100
processThre = 20
processTimes = 100
fileThre = 20
fileTimes = 100

def statistics():
    neighbor = {}
    neighbor_types = {}
    diff_neighbor = {}
    for i in range(3):
        dataEdge = pickle.load(open('theia/edge_cpr_' + str(i) + '.pkl', 'rb'))
        for edge in dataEdge:
            typeSrc = events[edge[2]][0]
            typeDst = events[edge[2]][1]
            if edge[0] not in neighbor:
                neighbor[edge[0]] = {}
                neighbor_types[edge[0]] = {}
                diff_neighbor[edge[0]] = {}
            if typeDst not in neighbor_types[edge[0]]:
                neighbor_types[edge[0]][typeDst] = 1
                diff_neighbor[edge[0]][typeDst] = 0
            else:
                neighbor_types[edge[0]][typeDst] += 1
            if edge[1] not in neighbor[edge[0]]:
                neighbor[edge[0]][edge[1]] = 1
                diff_neighbor[edge[0]][typeDst] += 1
            else:
                neighbor[edge[0]][edge[1]] += 1
    pickle.dump((neighbor, neighbor_types, diff_neighbor), open('statistics.pkl', 'rb'))

def process(darpa):
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
        ],
        [
            'tcexec',
            'thunderbird'
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
    subjects = {}
    files = {}
    networks = {}
    vicinity = {}
    host = ''
    nodes = {}
    cnt = 0
    code = -1
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
                if host != re.findall('"hostId":"(.*?)"', line)[0]:
                    line = file.readline()
                    continue
                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                if sub not in subjects:
                    line = file.readline()
                    continue

                if types == 'EVENT_BOOT':
                    line = file.readline()
                    continue

                if not event_type.__contains__(types):
                    line = file.readline()
                    continue

                if events[types][1] == 'com.bbn.tc.schema.avro.cdm18.FileObject':
                    if pre1 not in files:
                        line = file.readline()
                        continue
                elif events[types][1] == 'com.bbn.tc.schema.avro.cdm18.NetFlowObject':
                    if pre1 not in networks:
                        line = file.readline()
                        continue
                elif events[types][1] == 'com.bbn.tc.schema.avro.cdm18.Subject':
                    if pre1 not in subjects:
                        line = file.readline()
                        continue
                else:
                    line = file.readline()
                    continue
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
                        subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = (path, cmdline, parentUid)
                    except:
                        subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = ('', '', parentUid)
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

        # prune_data = []
        # neighbor = {}
        # for i in range(num-1, -1, -1):
        #     time = new_data[i][3]
        #     oid = new_data[i][0]
        #     pid = new_data[i][1]
        #     if pid not in neighbor:
        #         neighbor[pid] = {}
        #     if oid not in neighbor:
        #         neighbor[oid] = {}
        #     if oid not in neighbor[pid]:
        #         neighbor[pid][oid] = time
        #         neighbor[oid] = {}
        #         prune_data.append(new_data[i])
        #     elif neighbor[pid][oid] - time > 1:
        #         neighbor[pid][oid] = time
        #         neighbor[oid] = {}
        #         prune_data.append(new_data[i])
        #     else:
        #         neighbor[pid][oid] = time
        # num = len(prune_data)
        pickle.dump(new_data, open(darpa + '/'+darpa+'_'+str(code)+'.pkl', 'wb'))
    pickle.dump(subjects, open(darpa + '/subjects.pkl', 'wb'))
    pickle.dump(networks, open(darpa +'/networks.pkl', 'wb'))
    pickle.dump(files, open(darpa + '/files.pkl', 'wb'))
    pickle.dump(nodes, open(darpa + '/nodes.pkl', 'wb'))
    pickle.dump(vicinity, open(darpa+'/vicinity.pkl', 'wb'))

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
        # '81.49.200.166',
        # '61.167.39.128',
        # '78.205.235.65',
        # '139.123.0.113',
        # '200.36.109.214',
        # '154.145.113.18',
        # '155.162.39.48',
        # '76.56.184.25',
        # '192.113.144.28',
        # '198.115.236.119',
        # '25.159.96.207',
        # '53.158.101.118'
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

    other_nodes = 'nginx'

    print("process")
    filelist = getfiles(darpa)
    # subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
    # networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    # files = pickle.load(open(darpa + '/files.pkl', 'rb'))

    subjects = {}
    networks = {}
    files = {}


    vicinity = {}
    host = '83C8ED1F-5045-DBCD-B39F-918F0DF4F851'
    nodes = {}
    cnt = 0
    count = 0
    code = -1
    # anomaly_nodes = {}

    anomaly_nodes = pickle.load(open(darpa+'/anomaly_nodes.pkl', 'rb'))
    hop = {}
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
                # if sub not in subjects:
                #     subjects[sub] = ['', '', '']

                ''' groundtruth '''
                # if time > timestamp[time_index][0]:
                #     time_index += 1
                # if sub in anomaly_nodes and subjects[sub][0] in subjects_attack_nodes[time_index-1]:
                #     ccnt += 1
                #     hop[pre1] = 0
                # elif sub in hop or pre1 in hop:
                #     cccnt += 1
                # line = file.readline()
                # continue

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
                # if not data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.MemoryObject'):
                #     uid = re.findall('"uuid":"(.*?)"', line)[0]
                #     nodes[uid] = line
                # if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Host'):
                #     if host == '':
                #         host = data['datum']['com.bbn.tc.schema.avro.cdm18.Host']['uuid']
                #         print(host)
                #     else:
                #         print(data)
                # elif re.findall('"hostId":"(.*?)"', line)[0] != host:
                #     line = file.readline()
                #     continue
                #
                # if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Subject'):
                #
                #     if subjects.__contains__(data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']):
                #         line = file.readline()
                #         continue
                #     if data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'] is None:
                #         parentUid =''
                #     else:
                #         parentUid = data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['parentSubject'][
                #         'com.bbn.tc.schema.avro.cdm18.UUID']
                #     if not subjects.__contains__(parentUid):
                #         # parentUid = subjects[parentUid]
                #         parentUid = ''
                #     try:
                #         path = re.findall('"path":"(.*?)"', line)[0]
                #         cmdline = re.findall('"string":"(.*?)"', line)[0]
                #
                #     except:
                #         path = ''
                #         cmdline = ''
                #     subjects[data['datum']['com.bbn.tc.schema.avro.cdm18.Subject']['uuid']] = [path, cmdline, parentUid]
                # elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.FileObject'):
                #     files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = ''
                #     # filename = re.findall('"filename":"(.*?)"', line)
                #     # if len(filename)==1:
                #     #     files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = filename[0]
                #     # else:
                #     #     try:
                #     #         localPrincipal = re.findall('"localPrincipal":{"com.bbn.tc.schema.avro.cdm18.UUID":"(.*?)"', line)[0]
                #     #         print(data)
                #     #         filename = subjects[localPrincipal][0]
                #     #         files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = filename
                #     #     except:
                #     #         files[data['datum']['com.bbn.tc.schema.avro.cdm18.FileObject']['uuid']] = 'null'
                # elif data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.NetFlowObject'):
                #     networks[data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['uuid']] = data['datum'][
                #         'com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remoteAddress'] + '/' + str(
                #         data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['remotePort']) + '/' + str(
                #         data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localAddress'])+ '/' + str(
                #         data['datum']['com.bbn.tc.schema.avro.cdm18.NetFlowObject']['localPort'])

            line = file.readline()
        num = len(new_data)
        print(num)


        # prune_data = []
        # neighbor = {}
        # for i in range(num-1, -1, -1):
        #     time = new_data[i][3]
        #     oid = new_data[i][0]
        #     pid = new_data[i][1]
        #     if pid not in neighbor:
        #         neighbor[pid] = {}
        #     if oid not in neighbor:
        #         neighbor[oid] = {}
        #     if oid not in neighbor[pid]:
        #         neighbor[pid][oid] = time
        #         neighbor[oid] = {}
        #         prune_data.append(new_data[i])
        #     elif neighbor[pid][oid] - time > 1:
        #         neighbor[pid][oid] = time
        #         neighbor[oid] = {}
        #         prune_data.append(new_data[i])
        #     else:
        #         neighbor[pid][oid] = time
        # num = len(prune_data)
        # pickle.dump(new_data, open(darpa+'/'+darpa+'_'+str(code)+'.pkl', 'wb'))
    # subjects = pickle.load(open('cadets3/subjects.pkl', 'rb'))
    # files = pickle.load(open('cadets3/files.pkl', 'rb'))

        print(ccnt)
        print(cccnt)
    # host = '83C8ED1F-5045-DBCD-B39F-918F0DF4F851'
    # for i in filelist:
    #     code += 1
    #     print(i + '----------------------------------------------')
    #     file = open('../darpa/'+darpa+'/'+i, 'r')
    #     line = file.readline()
    #     times = 0
    #     while line:
    #         times += 1
    #         data = json.loads(line)
    #         data = dict(data)
    #         if data['datum'].__contains__('com.bbn.tc.schema.avro.cdm18.Event'):
    #             if data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'] == None or data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'] == None:
    #                 line = file.readline()
    #                 continue
    #             if host != re.findall('"hostId":"(.*?)"', line)[0]:
    #                 line = file.readline()
    #                 continue
    #             time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
    #             types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
    #             pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
    #                 'com.bbn.tc.schema.avro.cdm18.UUID']
    #             sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
    #                 'com.bbn.tc.schema.avro.cdm18.UUID']
    #
    #
    #             try:
    #                 cmd = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['name']['string']
    #                 path = re.findall('"exec":"(.*?)"', line)[0]
    #                 subjects[sub][0] = path
    #                 subjects[sub][1] = cmd
    #                 if files.__contains__(pre1):
    #                     path = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObjectPath']['string']
    #                     files[pre1] = path
    #                 elif networks.__contains__(pre1):
    #                     pass
    #                 line = file.readline()
    #                 continue
    #             except:
    #                 line = file.readline()
    #                 continue
    #         else:
    #             line = file.readline()

    # print(cnt)
    # print(count)
    # print(len(anomaly_nodes))
    # cnt = 0
    # for i in subjects:
    #     if subjects[i][0] != '':
    #         cnt += 1
    # print(cnt)
    # print(len(subjects)-cnt)
    #
    # cnt = 0
    # for i in files:
    #     if files[i] != '':
    #         cnt += 1
    # print(cnt)
    # print(len(files) - cnt)
    #
    # # pickle.dump(subjects, open(darpa+'/subjects.pkl', 'wb'))
    # # pickle.dump(networks, open(darpa+'/networks.pkl', 'wb'))
    # # pickle.dump(files, open(darpa+'/files.pkl', 'wb'))
    # pickle.dump(vicinity, open(darpa + '/vicinity.pkl', 'wb'))
    # pickle.dump(nodes, open(darpa + '/nodes.pkl', 'wb'))
    # pickle.dump(anomaly_nodes, open(darpa + '/anomaly_nodes.pkl', 'wb'))


def processTheia3(darpa):
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



def show():
    subjects = pickle.load(open('subjects.pkl', 'rb'))
    files = pickle.load(open('files.pkl', 'rb'))
    # networks = pickle.load(open('networks.pkl', 'rb'))
    communities = pickle.load(open('communities.pkl', 'rb'))
    index = 23
    G = nx.DiGraph()
    nodes = {}
    tail = 0
    nodes_ = []
    for i in communities[index]:

        if i[2] != 'EVENT_CLONE' and i[2] != 'EVENT_EXECUTE':
            continue
        if not nodes.__contains__(i[0]):
            nodes[i[0]] = tail
            nodes_.append(i[0])
            tail += 1
        if not nodes.__contains__(i[1]):
            nodes[i[1]] = tail
            nodes_.append(i[1])
            tail += 1

        G.add_edge(nodes[i[0]], nodes[i[1]], weight=event_type[i[2]])
        if len(nodes)>20:
            break
    # print(files[nodes_[0]])
    # print(nodes_[1])
    print(len(nodes))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, alpha=0.5)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def reverse():
    # subjects = pickle.load(open('subjects.pkl', 'rb'))
    files = pickle.load(open('files.pkl', 'rb'))
    # networks = pickle.load(open('networks.pkl', 'rb'))
    subjectReverse = {}
    fileReverse = {}
    networkReverse = {}

    # for i in subjects:
    #     if subjects[i][0] not in subjectReverse:
    #         subjectReverse[subjects[i][0]] = [i]
    #     else:
    #         subjectReverse[subjects[i][0]].append(i)

    for i in files:
        if files[i] not in fileReverse:
            fileReverse[files[i]] = [i]
        else:
            fileReverse[files[i]].append(i)

    # for i in networks:
    #     if networks[i] not in networkReverse:
    #         networkReverse[networks[i]] = [i]
    #     else:
    #         networkReverse[networks[i]].append(i)

    a = []
    for i in fileReverse:
        a.append((len(fileReverse[i]), i))
    a = sorted(a, key=lambda x: x[0], reverse=True)

    for i in range(100):
        print(a[i])
    # pickle.dump(subjectReverse, open('subjectReverse.pkl', 'wb'))
    # pickle.dump(networkReverse, open('networkReverse.pkl', 'wb'))
    # pickle.dump(fileReverse, open('fileReverse.pkl', 'wb'))


def temporary():
    subjectReverse = pickle.load(open('subjectReverse.pkl', 'rb'))
    # print(len(subjectReverse))
    #
    # cnt = 0
    # for i in subjectReverse:
    #     print(i)
    #     print(len(subjectReverse[i]))

    subjects = pickle.load(open('subjects.pkl', 'rb'))
    locates = pickle.load(open('locates2.pkl', 'rb'))
    communities = pickle.load(open('communities2.pkl', 'rb'))
    child = pickle.load(open('childs2.pkl', 'rb'))
    father = pickle.load(open('fathers2.pkl', 'rb'))


    def bfs(src, depth):
        tmp = []
        for i in src:
            if i not in locates:
                continue
            locate = locates[i]
            for event in communities[locate]:
                try:
                    if event[2] == 'EVENT_CLONE':
                        edge.append([event[0], event[1]])
                        tmp.append(event[1])
                except:
                    print(event)
                    sys.exit()
        if tmp != []:
            bfs(tmp, depth + 1)
    for j in range(30):
        edge = []
        uid = subjectReverse['/usr/bin/python2.7'][j]
        tmp = [uid]
        bfs(tmp, 0)
        if len(edge)>2:
            print(edge)
            print(len(edge))
            break

    new_edge = []
    for i in edge:
        new_edge.append([subjects[i[0]][0], subjects[i[1]][0]])

    print(new_edge)
    # G = nx.DiGraph()
    # for i in edge:
    #     G.add_edge(i[0], i[1])
    #
    # pos = nx.spring_layout(G)
    # nx.draw(G, pos, with_labels=True, alpha=0.5)
    # labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # plt.show()

def temporarySingle():
    subjectReverse = pickle.load(open('subjectReverse.pkl', 'rb'))
    files = pickle.load(open('files.pkl', 'rb'))
    networks = pickle.load(open('networks.pkl', 'rb'))

    subjects = pickle.load(open('subjects.pkl', 'rb'))
    locates = pickle.load(open('locates2.pkl', 'rb'))
    communities = pickle.load(open('communities2.pkl', 'rb'))
    child = pickle.load(open('childs.pkl', 'rb'))
    father = pickle.load(open('fathers.pkl', 'rb'))

    def bfs(src, depth):
        tmp = []
        for i in src:
            if i not in locates:
                continue
            locate = locates[i]
            for event in communities[locate]:
                try:
                    if event[2] == 'EVENT_CLONE':
                        edge.append([event[0], event[1]])
                        tmp.append(event[1])
                except:
                    print(event)
                    sys.exit()
        if tmp != []:
            bfs(tmp, depth + 1)

    types = {}
    for j in range(15):
        types = {}
        edge = []
        uid = subjectReverse['/etc/firefox/native-messaging-hosts/gtcache'][j]
        try:
            locate = locates[uid]
        except:
            continue
        # if len(communities[locate]) < 50:
        #     continue
        for event in communities[locate]:
            if event[2] in types:
                types[event[2]] += 1
            else:
                types[event[2]] = 1
            if event[2] == 'EVENT_SENDTO':
                print(networks[event[1]])
                break

        print(types)
        print(subjects[uid])

def detection():
    subjects = pickle.load(open('subjects.pkl', 'rb'))
    files = pickle.load(open('files.pkl', 'rb'))
    networks = pickle.load(open('networks.pkl', 'rb'))
    subjectReverse = {}
    fileReverse = {}
    networkReverse = {}

    for i in subjects:
        if subjects[i][0] not in subjectReverse:
            subjectReverse[subjects[i][0]] = [i]
        else:
            subjectReverse[subjects[i][0]].append(i)

    for i in files:
        if files[i] not in fileReverse:
            fileReverse[files[i]] = [i]
        else:
            fileReverse[files[i]].append(i)

    for i in networks:
        if networks[i] not in networkReverse:
            networkReverse[networks[i]] = [i]
        else:
            networkReverse[networks[i]].append(i)

    locates = pickle.load(open('locates2.pkl', 'rb'))
    communities = pickle.load(open('communities2.pkl', 'rb'))
    childs = pickle.load(open('childs2.pkl', 'rb'))
    fathers = pickle.load(open('fathers2.pkl', 'rb'))
    print(locates['02000000-0000-0000-0000-000000000020'])
    print(subjects['02000000-0000-0000-0000-000000000020'])
    exists = {}
    adj = {}
    for i in locates:
        if i in subjects:
            locate = locates[i]
            for j in communities[locate]:
                sub = j[0]
                obj = j[1]
                if 'REC' in j[2] or 'READ' in j[2] or 'EXECUTE' in j[2]:
                    sub = j[1]
                    obj = j[0]
                try:
                    assert(sub==i)
                except:
                    print(j)
                    print(i)
                    return
                if not exists.__contains__(sub):
                    exists[sub] = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]
                exists[sub][event_type[j[2]]][obj] = 0

                sub = subjects[sub][1]
                if events[j[2]][1] == 'com.bbn.tc.schema.avro.cdm18.NetFlowObject':
                    try:
                        obj = networks[obj]
                    except:
                        obj = ''
                elif events[j[2]][1] == 'com.bbn.tc.schema.avro.cdm18.FileObject':
                    try:
                        obj = files[obj]
                        if isinstance(obj, list):
                            obj = obj[0]
                    except:
                        obj = ''
                else:
                    try:
                        obj = subjects[obj][1]
                    except:
                        obj = ''

                if not adj.__contains__(sub):
                    adj[sub] = [{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}]

                try:
                    if not adj[sub][event_type[j[2]]].__contains__(obj):
                        adj[sub][event_type[j[2]]][obj] = 0
                except:
                    print(j)
                    print(obj)
                    return

    print(exists['02000000-0000-0000-0000-000000000020'])
    print(adj['kthreadd'])
    pickle.dump(adj, open('exists.pkl', 'wb'))
    pickle.dump(exists, open('adj.pkl', 'wb'))
    # adj = pickle.load(open('adj.pkl', 'rb'))
    return
    # for i in adj:
    #     print(i)
    #     break

    total = 0
    filelist = [
        'theia3_6.pkl',
        'theia3_7.pkl',
        'theia3_8.pkl',
    ]
    anomaly = []
    types = {}
    for file in filelist:
        data = pickle.load(open(file, 'rb'))
        total += len(data)
        for j in data:
            sub = j[0]
            obj = j[1]
            if 'REC' in j[2] or 'READ' in j[2] or 'EXECUTE' in j[2]:
                sub = j[1]
                obj = j[0]
            try:
                sub = subjects[sub][1]
            except:
                anomaly.append(j)
                continue
            if events[j[2]][1] == 'com.bbn.tc.schema.avro.cdm18.NetFlowObject':
                try:
                    obj = networks[obj]
                except:
                    anomaly.append(j)
                    continue
            elif events[j[2]][1] == 'com.bbn.tc.schema.avro.cdm18.FileObject':
                try:
                    obj = files[obj]
                    if isinstance(obj, list):
                        obj = obj[0]
                except:
                    anomaly.append(j)
                    continue
            elif events[j[2]][1] == 'com.bbn.tc.schema.avro.cdm18.Subject':
                try:
                    obj = subjects[obj][1]
                except:
                    anomaly.append(j)
                    continue
            else:
                print(j)
                return

            if adj.__contains__(sub):
                if adj[sub][event_type[j[2]]].__contains__(obj):
                    continue
                else:
                    continue
            else:
                if types.__contains__(sub):
                    pass
                else:
                    types[sub] = 1
                    # if len(sub)>80:
                    #     sub = sub[:80]
                    print(sub)

            anomaly.append(j)
    print(total)
    print(len(anomaly))


def rootNode(darpa):
    subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
    files = pickle.load(open(darpa + '/files.pkl', 'rb'))
    networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    isroot = {}
    cnt = 0
    print(len(subjects))
    for uid in subjects:
        root = ''
        # if subjects[uid][0] == '/bin/dash':
        #     print(subjects[uid])
        #     cnt += 1
        #     if cnt == 20:
        #         return
        while True:
            if isroot.__contains__(uid):
                break
            isroot[uid] = 0
            if subjects[uid][2] != '' and subjects.__contains__(subjects[uid][2]):
                puid = subjects[uid][2]
                if subjects[puid][1] == '-bash' or subjects[puid][1] == 'bash' or subjects[puid][0] == '/bin/bash' or \
                        subjects[puid][0] == '/bin/dash' or subjects[puid][0] == '/sbin/init' or \
                        '/usr/bin' in subjects[puid][0]:
                    if subjects[uid][1] == '-bash' or subjects[uid][1] == 'bash' or subjects[uid][0] == '/bin/bash' or \
                            subjects[uid][0] == '/bin/dash' or subjects[uid][0] == '/sbin/init' or \
                            '/usr/bin' in subjects[uid][0]:
                        pass
                    else:
                        root = uid
                uid = puid
                continue
            else:
                if subjects[uid][1] == '-bash' or subjects[uid][1] == 'bash' or subjects[uid][0] == '/bin/bash' or \
                        subjects[uid][0] == '/bin/dash' or subjects[uid][0] == '/sbin/init' or \
                        '/usr/bin' in subjects[uid][0]:
                    pass
                else:
                    root = uid
                break
        if root != '':
            isroot[root] = 1
    print(len(isroot))
    pickle.dump(isroot, open(darpa + '/isroot.pkl', 'wb'))
    types = {}
    for i in isroot:
        if isroot[i] == 0:
            continue
        if types.__contains__(subjects[i][0]):
            types[subjects[i][0]] += 1
        else:
            types[subjects[i][0]] = 1
    print(types)
    print(len(types))


    myroot = {}
    for uid in subjects:
        tmp = []
        while True:
            if isroot.__contains__(uid) and isroot[uid] == 1:
                myroot[uid] = uid
                for node in tmp:
                    myroot[node] = uid
                break
            if myroot.__contains__(uid):
                for node in tmp:
                    myroot[node] = myroot[uid]
                break
            if subjects[uid][2] != '' and subjects.__contains__(subjects[uid][2]):
                tmp.append(uid)
                uid = subjects[uid][2]
            else:
                for node in tmp:
                    myroot[node] = node
                break

    pickle.dump(myroot, open(darpa + '/myroot.pkl', 'wb'))


def rootCommunity():
    subjects = pickle.load(open('cadets3/subjects.pkl', 'rb'))
    # files = pickle.load(open('files.pkl', 'rb'))
    # networks = pickle.load(open('networks.pkl', 'rb'))
    # isroot = pickle.load(open('isroot.pkl', 'rb'))
    myroot = pickle.load(open('cadets3/myroot.pkl', 'rb'))
    locates = {}
    communities = []
    cnt = 0
    for i in myroot:
        if locates.__contains__(myroot[i]):
            locates[i] = locates[myroot[i]]
        else:
            locates[myroot[i]] = cnt
            locates[i] = cnt
            cnt += 1
    print(len(locates))
    for i in subjects:
        if myroot.__contains__(i):
            locates[i] = locates[myroot[i]]
        else:
            locates[i] = cnt
            cnt += 1
    for i in range(cnt):
        communities.append([])

    files = [
        'cadets3_0.pkl',
        'cadets3_1.pkl',
        'cadets3_2.pkl',
        'cadets3_3.pkl',
        'cadets3_4.pkl',
        'cadets3_5.pkl',
        'cadets3_6.pkl',
        'cadets3_7.pkl',
        'cadets3_8.pkl',
        'cadets3_9.pkl',
    ]

    relate_subs = {}
    for file in files:
        print(file)
        data = pickle.load(open('cadets3/'+file, 'rb'))
        for i in data:

            if 'REC' in i[2] or 'READ' in i[2] or 'EXECUTE' in i[2]:
                communities[locates[i[1]]].append(i)
                if relate_subs.__contains__(i[0]):
                    if not relate_subs[i[0]].__contains__(i[1]):
                        relate_subs[i[0]][i[1]] = 0
                else:
                    relate_subs[i[0]] = {i[1]: 0}
            else:
                communities[locates[i[0]]].append(i)
                if relate_subs.__contains__(i[1]):
                    if not relate_subs[i[1]].__contains__(i[0]):
                        relate_subs[i[1]][i[0]] = 0
                else:
                    relate_subs[i[1]] = {i[0]: 0}

    pickle.dump(communities, open('cadets3/rootcommunities.pkl', 'wb'))
    pickle.dump(locates, open('cadets3/rootlocates.pkl', 'wb'))
    pickle.dump(relate_subs, open('cadets3/relatesubs.pkl', 'wb'))

def attackCommunity():
    attacks = ['0836A1B8-0200-0000-0000-000000000020',
    '0A36B3B8-0200-0000-0000-000000000020',
    'D037D3BA-0200-0000-0000-000000000020',
    'D137D4BA-0200-0000-0000-000000000020',
    'D237D6BA-0200-0000-0000-000000000020',
    '1D38E3BB-0200-0000-0000-000000000020',
    '223838BC-0200-0000-0000-000000000020',
    '23383FBC-0200-0000-0000-000000000020',
    '273847BC-0200-0000-0000-000000000020',
    '54387BBE-0200-0000-0000-000000000020',
    '55387DBE-0200-0000-0000-000000000020',
    '0100D00F-A60F-2400-0000-0000A43DD030',
    '0100D00F-A84B-1E00-0000-000049134A16',
    '0100D00F-1D12-1E00-0000-00009F8F0C12',
    '0100D00F-A84B-1E00-0000-00008C1CB31C',
    '283847BC-0200-0000-0000-000000000020',
    '293847BC-0200-0000-0000-000000000020']
    file_label = open('label', 'r')
    line = file_label.readline()
    label = {}
    while line:
        line = line.strip().split(' ')
        label[line[0]] = 1
        line = file_label.readline()

    myroot = pickle.load(open('myroot.pkl', 'rb'))
    subject_reverse = pickle.load(open('subjectReverse.pkl', 'rb'))
    subjects = pickle.load(open('subjects.pkl', 'rb'))
    files = pickle.load(open('files.pkl', 'rb'))
    networks = pickle.load(open('networks.pkl', 'rb'))
    communities = pickle.load(open('rootcommunities.pkl', 'rb'))
    locates = pickle.load(open('rootlocates.pkl', 'rb'))
    train_communities = pickle.load(open('train_rootcommunities.pkl', 'rb'))
    train_locates = pickle.load(open('train_rootlocates.pkl', 'rb'))
    relatesubs = pickle.load(open('relatesubs.pkl', 'rb'))
    train_relatesubs = pickle.load(open('train_relatesubs.pkl', 'rb'))

    # for i in attacks:
    #     if i in myroot:
    #         print(subjects[myroot[i]])
    #         print(subject_reverse[subjects[myroot[i]][0]])
    #         print(train_locates[myroot[i]])
    #         print(len(train_communities[train_locates[myroot[i]]]))



    uid = '02000000-0000-0000-0000-000000000020'
    anomalies = {}
    fatherisuid = {}
    for event in communities[locates[uid]]:
        # if subjects.__contains__(event[0]):
        #     if subjects[subjects[event[0]][2]][2] == uid:
        #         fatherisuid[event[0]] = 1
        # if subjects.__contains__(event[1]):
        #     if subjects[subjects[event[1]][2]][2] == uid:
        #         fatherisuid[event[1]] = 1
        if not anomalies.__contains__(event[0]):
            anomalies[event[0]] = 1
        if not anomalies.__contains__(event[1]):
            anomalies[event[1]] = 1
    #
    # print(len(anomalies))
    # for i in fatherisuid:
    #     print(subjects[i])
    # cnt = 0
    # for i in label:
    #     if anomalies.__contains__(i):
    #         cnt += 1
    # print(cnt)
def labelCadets3():
    attack_nodes = [
        'vUgefal',
        '/var/log/devc',
        'nginx',
        '81.49.200.166',
        '78.205.235.65',
        '200.36.109.214',
        '139.123.0.113',
        '152.111.159.139',
        '61.167.39.128',
    ]
    subjects = pickle.load(open('cadets3/subjects.pkl', 'rb'))
    files = pickle.load(open('cadets3/files.pkl', 'rb'))
    networks = pickle.load(open('cadets3/networks.pkl', 'rb'))
    cnt = 0

    anomaly = {}
    for i in subjects:
        if subjects[i][0] in attack_nodes:
            anomaly[i] = 1
    print(len(anomaly))
    # locates = pickle.load(open('cadets/rootlocates.pkl', 'rb'))
    myroot = pickle.load(open('cadets3/myroot.pkl', 'rb'))
    for i in anomaly:
        print(subjects[i])
        print(subjects[myroot[i]])


def communityDetection(darpa):
    subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
    # files = pickle.load(open('files.pkl', 'rb'))
    # networks = pickle.load(open('networks.pkl', 'rb'))
    # isroot = pickle.load(open('isroot.pkl', 'rb'))
    myroot = pickle.load(open(darpa + '/myroot.pkl', 'rb'))
    communities = {}
    for i in myroot:
        if myroot[i] not in communities:
            communities[myroot[i]] = []
        communities[myroot[i]].append(i)

    vicinity = pickle.load(open(darpa + '/vicinity.pkl', 'rb'))

    intervals = {}
    for i in vicinity:
        intervals[i] = 10
        threshold = []
        timestamp = float(vicinity[i][0][1])
        length = len(vicinity[i])
        for k in range(length):
            threshold.append(float(vicinity[i][k][1]) - timestamp)
            timestamp = float(vicinity[i][k][1])

        threshold = sorted(threshold)
        tmp = 2
        start = 0
        for k in range(length):
            if threshold[k] < 20:
                continue
            else:
                start = k
                break
        if start == length:
            intervals[i] = 20
            continue
        total = 0

        count = (threshold[-1] - threshold[start]) * 2 / (length - start)
        tmp = threshold[start] + count
        for k in range(start, length):
            if threshold[k] <= tmp:
                total += 1
                continue
            else:
                if total < 2:
                    intervals[i] = tmp - count
                else:
                    total = 0
                    tmp += count

    windows = {}


    for i in vicinity:
        windows[i] = []
        length = len(vicinity[i])
        start = 0
        timestamp = float(vicinity[i][0][1])
        interval = 0
        for k in range(length):
            if float(vicinity[i][k][1]) - timestamp > max(intervals[i], 2 * interval):
                windows[i].append((float(vicinity[i][start][1]) - 0.01, float(vicinity[i][k - 1][1])))
                start = k
            interval = float(vicinity[i][k][1]) - timestamp
            timestamp = float(vicinity[i][k][1])
        windows[i].append((float(vicinity[i][start][1]) - 0.01, float(vicinity[i][length - 1][1])))

    communities_windows = {}
    for i in communities:
        communities_windows[i] = []
        for j in communities[i]:
            if j not in windows:
                continue
            for k in windows[j]:
                communities_windows[i].append(k)

    for i in communities_windows:
        communities_windows[i] = sorted(communities_windows[i], key=lambda x: x[0])
    windows_ = {}
    for i in communities_windows:
        windows_[i] = []
        if len(communities_windows[i]) == 0:
            # print(communities[i])
            continue
        start = communities_windows[i][0][0]
        end = communities_windows[i][0][1]
        for j in communities_windows[i]:
            if j[0] > end:
                windows_[i].append((start, end))
                start = j[0]
                end = j[1]
            else:
                if j[1] > end:
                    end = j[1]

        windows_[i].append((start, end))

    print(len(windows_))
    pickle.dump(communities, open(darpa+'/communities.pkl', 'wb'))
    pickle.dump(windows_, open(darpa+'/windows.pkl', 'wb'))
    pickle.dump(intervals, open(darpa+'/intervals.pkl', 'wb'))


def groundTruth(darpa='cadets3'):
    files_attack_nodes = [
        '/tmp/vUgefal',
        '/var/log/devc',
        '/etc/passwd',
        '/etc/group',
        '/usr/log/devc'
        '/tmp/tmux-1002',
        '/tmp/minions',
        '/tmp/test',
        '/var/log/sendmail',
        'tmp/grain'
    ]
    networks_attack_nodes = [
        '81.49.200.166',
        '61.167.39.128',
        '78.205.235.65',
        '139.123.0.113',
        '200.36.109.214',
        '154.145.113.18',
        '155.162.39.48',
        '76.56.184.25',
        '192.113.144.28',
        '198.115.236.119',
        '25.159.96.207',
        '53.158.101.118',
    ]


    subjects_attack_nodes = [
        'tmux-1002',
        'test',
        'main',
        'minions',
        'makewhatis',
        'ssh',
        'whoami',
        'pEja72mA',
        'vUgefal',
        'nginx',
    ]
    print("process")
    filelist = getfiles(darpa)
    subjects = pickle.load(open(darpa+'/subjects.pkl', 'rb'))
    files = pickle.load(open(darpa + '/files.pkl', 'rb'))
    networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    host = '83C8ED1F-5045-DBCD-B39F-918F0DF4F851'
    nodes = {}
    cnt = 0
    vicinity = {}
    count = 0
    code = -1
    anomaly_nodes = {}
    other_nodes = 'nginx'
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
                        print(line)
                        line = file.readline()
                        continue
                except:
                    line = file.readline()
                    continue

                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']



                if types == 'EVENT_CLONE':
                    subjects[pre1][2] = sub

                if types == 'EVENT_BOOT':
                    line = file.readline()
                    continue


                if pre1 not in files and pre1 not in networks and pre1 not in subjects:
                    line = file.readline()
                    continue


                if pre1 in networks:
                    if '128.55.12.110/51153' in networks[pre1]:
                        print(line)
                        print(subjects[sub])
                        print(networks[pre1])
                        sys.exit()
                line = file.readline()
                continue


                tmp = count
                if subjects[sub][0] in subjects_attack_nodes:
                    count += 1
                    if sub not in anomaly_nodes:
                        anomaly_nodes[sub] = 0
                    if pre1 not in anomaly_nodes:
                        anomaly_nodes[pre1] = 0
                    anomaly_nodes[sub] += 1
                    anomaly_nodes[pre1] += 1

                elif pre1 in networks and tmp == count:
                    if subjects[sub][0] == other_nodes:
                        for k in networks_attack_nodes:
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
                    if subjects[sub][0] == other_nodes:
                        for k in files_attack_nodes:
                            if k in files[pre1]:
                                count += 1
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                if sub in anomaly_nodes and tmp == count:
                    count += 1
                    if sub not in anomaly_nodes:
                        anomaly_nodes[sub] = 0
                    if pre1 not in anomaly_nodes:
                        anomaly_nodes[pre1] = 0
                    anomaly_nodes[sub] += 1
                    anomaly_nodes[pre1] += 1
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
                        if object in networks:
                            if '128.55.12.166' in networks[object]:
                                print(data)
                                sys.exit()
                    elif time - neighbor[sub][pre1][0] > 1 or neighbor[sub][pre1][1] != types:
                        neighbor[sub][pre1] = (time, types)
                        neighbor[pre1] = {}
                        new_data.append([sub, pre1, types, time])
                        vicinity[subject].append((types, time, object))
                        if object in networks:
                            if '128.55.12.166' in networks[object]:
                                print(data)
                                sys.exit()
                except:
                    print(neighbor)
                    print(neighbor[sub])
                    print(neighbor[sub][pre1])
                    return

            line = file.readline()
        num = len(new_data)

        print(count)

    for i in anomaly_nodes:
        if i in subjects:
            print(len(vicinity[i]))
            print(subjects[i])

    #
    # n = ['128.55.12.166',
    #  '128.55.12.67']
    # for i in vicinity:
    #     tmp = {}
    #     for j in vicinity[i]:
    #         if j[2] in networks:
    #             for k in n:
    #                 if k in networks[j[2]]:
    #                     tmp[k] = 1
    #     if len(tmp) == 4:
    #         print(i)
    #         anomaly_nodes[i] = len(vicinity[i])
    #
    #
    # pickle.dump(anomaly_nodes, open(darpa + '/anomaly_nodes.pkl', 'wb'))


def groundTruthTrace(darpa='cadets3'):
    files_attack_nodes = [
        '/tmp/vUgefal',
        '/var/log/devc',
        '/etc/passwd',
        '/etc/group',
        '/usr/log/devc'
        '/tmp/tmux-1002',
        '/tmp/minions',
        '/tmp/test',
        '/var/log/sendmail',
        'tmp/grain'
    ]
    networks_attack_nodes = [
        '81.49.200.166',
        '61.167.39.128',
        '78.205.235.65',
        '139.123.0.113',
        '200.36.109.214',
        '154.145.113.18',
        '155.162.39.48',
        '76.56.184.25',
        '192.113.144.28',
        '198.115.236.119',
        '25.159.96.207',
        '53.158.101.118',
    ]


    subjects_attack_nodes = [
        'tmux-1002',
        'test',
        'main',
        'minions',
        'makewhatis',
        'ssh',
        'whoami',
        'pEja72mA',
        'vUgefal',
        'nginx',
    ]
    print("process")
    filelist = getfiles(darpa)
    subjects = pickle.load(open(darpa+'/subjects.pkl', 'rb'))
    files = pickle.load(open(darpa + '/files.pkl', 'rb'))
    networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
    host = '83C8ED1F-5045-DBCD-B39F-918F0DF4F851'
    nodes = {}
    cnt = 0
    vicinity = {}
    count = 0
    code = -1
    anomaly_nodes = {}
    other_nodes = 'nginx'
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
                        print(line)
                        line = file.readline()
                        continue
                except:
                    line = file.readline()
                    continue

                time = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['timestampNanos'] / 100000000
                types = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['type']
                pre1 = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['predicateObject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']
                sub = data['datum']['com.bbn.tc.schema.avro.cdm18.Event']['subject'][
                    'com.bbn.tc.schema.avro.cdm18.UUID']



                if types == 'EVENT_CLONE':
                    subjects[pre1][2] = sub

                if types == 'EVENT_BOOT':
                    line = file.readline()
                    continue


                if pre1 not in files and pre1 not in networks and pre1 not in subjects:
                    line = file.readline()
                    continue


                if pre1 in networks:
                    if '128.55.12.110/51153' in networks[pre1]:
                        print(line)
                        print(subjects[sub])
                        print(networks[pre1])
                        sys.exit()
                line = file.readline()
                continue


                tmp = count
                if subjects[sub][0] in subjects_attack_nodes:
                    count += 1
                    if sub not in anomaly_nodes:
                        anomaly_nodes[sub] = 0
                    if pre1 not in anomaly_nodes:
                        anomaly_nodes[pre1] = 0
                    anomaly_nodes[sub] += 1
                    anomaly_nodes[pre1] += 1

                elif pre1 in networks and tmp == count:
                    if subjects[sub][0] == other_nodes:
                        for k in networks_attack_nodes:
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
                    if subjects[sub][0] == other_nodes:
                        for k in files_attack_nodes:
                            if k in files[pre1]:
                                count += 1
                                if sub not in anomaly_nodes:
                                    anomaly_nodes[sub] = 0
                                if pre1 not in anomaly_nodes:
                                    anomaly_nodes[pre1] = 0
                                anomaly_nodes[sub] += 1
                                anomaly_nodes[pre1] += 1
                                break

                if sub in anomaly_nodes and tmp == count:
                    count += 1
                    if sub not in anomaly_nodes:
                        anomaly_nodes[sub] = 0
                    if pre1 not in anomaly_nodes:
                        anomaly_nodes[pre1] = 0
                    anomaly_nodes[sub] += 1
                    anomaly_nodes[pre1] += 1
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
                        if object in networks:
                            if '128.55.12.166' in networks[object]:
                                print(data)
                                sys.exit()
                    elif time - neighbor[sub][pre1][0] > 1 or neighbor[sub][pre1][1] != types:
                        neighbor[sub][pre1] = (time, types)
                        neighbor[pre1] = {}
                        new_data.append([sub, pre1, types, time])
                        vicinity[subject].append((types, time, object))
                        if object in networks:
                            if '128.55.12.166' in networks[object]:
                                print(data)
                                sys.exit()
                except:
                    print(neighbor)
                    print(neighbor[sub])
                    print(neighbor[sub][pre1])
                    return

            line = file.readline()
        num = len(new_data)

        print(count)

    for i in anomaly_nodes:
        if i in subjects:
            print(len(vicinity[i]))
            print(subjects[i])

    #
    # n = ['128.55.12.166',
    #  '128.55.12.67']
    # for i in vicinity:
    #     tmp = {}
    #     for j in vicinity[i]:
    #         if j[2] in networks:
    #             for k in n:
    #                 if k in networks[j[2]]:
    #                     tmp[k] = 1
    #     if len(tmp) == 4:
    #         print(i)
    #         anomaly_nodes[i] = len(vicinity[i])
    #
    #
    # pickle.dump(anomaly_nodes, open(darpa + '/anomaly_nodes.pkl', 'wb'))


darpa = 'cadets3'
processCadets3(darpa)
# processTheia3(darpa)
# rootNode(darpa)
# communityDetection(darpa)
# processClearScope3(darpa)
# processTheia3(darpa)
# vicinity = pickle.load(open(darpa + '/all_vicinity.pkl', 'rb'))
# subjects = pickle.load(open(darpa + '/subjects.pkl', 'rb'))
# networks = pickle.load(open(darpa + '/networks.pkl', 'rb'))
# files = pickle.load(open(darpa + '/files.pkl', 'rb'))
# anomaly_nodes = pickle.load(open(darpa + '/anomaly_nodes.pkl', 'rb'))
#
# for i in anomaly_nodes:
#     if i in subjects:
#         if subjects[i][0] == '/home/admin/Downloads/firefox/firefox':
#             print(anomaly_nodes[i])
#             print(len(vicinity[i]))
#             print(subjects[i])

#
# for i in subjects:
#     if subjects[i][0] == '/usr/bin/firefox' and i in vicinity:
#         if len(vicinity[i]) > 1000:
#             print(len(vicinity[i]))
#             print(subjects[i])


# sshd = 'D7A0E029-39B0-11E8-BF66-D9AA8AFF4A69'
#
# profile = 'FB1F9E30-0000-0000-0000-000000000020'
# cnt = 0
# total = 0
# print(len(vicinity[firefox]))
# for i in vicinity[firefox]:
#     total += 1
#     if i[2] in anomaly_nodes:
#         cnt += 1
#         print(i)
#         if i[2] in subjects:
#             print(subjects[i[2]])
#         elif i[2] in files:
#             print(files[i[2]])
#         else:
#             print(networks[i[2]])
#     else:
#         print("~~~~~~")
#         print(i)
#         if i[2] in subjects:
#             print(subjects[i[2]])
#         elif i[2] in files:
#             print(files[i[2]])
#         else:
#             print(networks[i[2]])
#     if total == 20:
#         break
# print(cnt)






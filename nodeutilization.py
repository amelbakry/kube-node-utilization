#!/usr/bin/env python3
import os
import json
import re
import json
import pprint
import ast
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
from kubernetes.client.api_client import ApiClient
from terminaltables import AsciiTable

config.load_kube_config()
v1 = client.CoreV1Api()
api_client = ApiClient()


class Convert:

  def cpu(value):
    """
    Return CPU in milicores if it is configured with value
    """
    if re.match(r"[0-9]{1,9}m", str(value)):
      cpu = re.sub("[^0-9]", "", value)
    elif re.match(r"[0-9]{1,4}$", str(value)):
      cpu = int(value) * 1000
    elif re.match(r"[0-9]{1,15}n", str(value)):
      cpu = int(re.sub("[^0-9]", "", value)) // 1000000
    elif re.match(r"[0-9]{1,15}u", str(value)):
      cpu = int(re.sub("[^0-9]", "", value)) // 1000
    return int(cpu)

  def memory(value):
    """
    Return Memory in MB
    """
    if re.match(r"[0-9]{1,9}Mi?", str(value)):
      mem = re.sub("[^0-9]", "", value)
    elif re.match(r"[0-9]{1,9}Ki?", str(value)):
      mem = re.sub("[^0-9]", "", value)
      mem = int(mem) // 1024
    elif re.match(r"[0-9]{1,9}Gi?", str(value)):
      mem = re.sub("[^0-9]", "", value)
      mem = int(mem) * 1024
    return int(mem)


def print_table(func):
  def _print(*args, **kwargs):

    table_data = func(*args, **kwargs)[0]
    func(*args, **kwargs)
    title = func(*args, **kwargs)[1]
    print('\033[1m' + ' %s' % title + '\033[0m')
    table = AsciiTable(table_data)
    print(table.table)
  return _print


@print_table
def nodeutilization():
  ready_nodes = []
  usage = {}
  allocatable = {}
  allocatable_space = {}
  available_space = {}

  for n in v1.list_node().items:
    role = n.metadata.labels["kubernetes.io/role"]
    for status in n.status.conditions:
      if status.status == 'True' and status.type == 'Ready':
        ready_nodes.append(n.metadata.name)
  for node in ready_nodes:
    node_metrics = "/apis/metrics.k8s.io/v1beta1/nodes/" + node
    response = api_client.call_api(node_metrics,
                                   'GET', auth_settings=['BearerToken'],
                                   response_type='json', _preload_content=False)
    response = json.loads(response[0].data.decode('utf-8'))
    used = response.get("usage")
    values = {}
    values["memory"] = Convert.memory(used.get("memory"))
    values["cpu"] = Convert.cpu(used.get("cpu"))
    usage[node] = values
  for n in v1.list_node().items:
    allocation = n.status.allocatable
    values = {}
    values["memory"] = Convert.memory(allocation.get("memory"))
    values["cpu"] = Convert.cpu(allocation.get("cpu"))
    allocatable_space[n.metadata.name] = values

  title = " "
  table_data = [["NodeName", "CPU", "Memory"]]

  for node in ready_nodes:
    try:
      usedmem = usage[node].get("memory")
      allmem = allocatable_space[node].get("memory")
      avamem = (usedmem / allmem) * 100
      avamem = "%.2f" % avamem
      usedcpu = usage[node].get("cpu")
      allcpu = allocatable_space[node].get("cpu")
      avacpu = (int(usedcpu) / int(allcpu)) * 100
      avacpu = "%.2f" % avacpu
      available_space[node] = {"memory": avamem, "cpu": avacpu}
    except:
      pass

  for node, util in available_space.items():
    data = [node, available_space[node].get("cpu") + "%", available_space[node].get("memory") + "%"]
    table_data.append(data)
  return table_data, title


if __name__ == '__main__':
  try:
    print('\033[1m' + ' Kubernetes Node Utilization.......... ' + '\033[0m')
    nodeutilization()
  except Exception as e:
    if "Forbidden" or "Unauthorized" in e:
      print("Unauthorized. Please make sure to login to the cluster and that you have permission")
    else:
      print(e)

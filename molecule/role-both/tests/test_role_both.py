import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nomad_service_enabled_and_running(host):
    s = host.service('nomad')

    assert s.is_enabled
    assert s.is_running


def test_nomad_http_port(host):
    s = host.socket("tcp://0.0.0.0:4646")
    assert s.is_listening


def test_nomad_rpc_port(host):
    s = host.socket("tcp://0.0.0.0:4647")
    assert s.is_listening


def test_nomad_serf_port(host):
    s = host.socket("tcp://0.0.0.0:4648")
    assert s.is_listening


def test_nomad_status(host):
    host.run_test("/usr/local/bin/nomad status")


def test_nomad_server_members(host):
    host.run_test("/usr/local/bin/nomad server members")

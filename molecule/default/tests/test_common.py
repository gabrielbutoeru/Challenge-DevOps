import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('centos7')


@pytest.mark.parametrize('pkg', [
    'docker'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'docker'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled

@pytest.mark.parametrize('file, content', [
  ("/lib/systemd/system/docker.service", "ExecStart=/usr/bin/dockerd -g /mnt/docker -H fd:// -H tcp://0.0.0.0:2376")
])
def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)

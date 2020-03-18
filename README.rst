# Cisco ASA Ansible Collection
# ============================

## Tech Preview

This is the [Ansible
Collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)
provided by the [Ansible Security Automation
Team](https://github.com/ansible-security) for automating actions in
[Cisco ASA](https://www.cisco.com/c/en_in/products/security/adaptive-security-appliance-asa-software/index.html)

This Collection is meant for distribution via
[Ansible Galaxy](https://galaxy.ansible.com/) as is available for all
[Ansible](https://github.com/ansible/ansible) users to utilize, contribute to,
and provide feedback about.

### Using Cisco ASA Ansible Collection

An example for using this collection to manage a ACL resource
[Cisco ASA](https://www.cisco.com/c/en/us/td/docs/security/asa/asa90/configuration/guide/asa_90_cli_config/acl_extended.html)
is as follows:

`inventory.ini` (Note the password should be managed by a [Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) for a production environment.
```
[asa]
host_asa.example.com

[asa:vars]
ansible_user=admin
ansible_ssh_pass=password
ansible_become=true
ansible_become_method=ansible.netcommon.enable
ansible_become_pass=become_password
ansible_connection=ansible.netcommon.network_cli
ansible_network_os=cisco.asa.asa
ansible_python_interpreter=python
```

#### Using the modules with Fully Qualified Collection Name (FQCN)

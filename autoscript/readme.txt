1.���ļ��з��ڰ�װ��openstack�Ļ���������·����
2.ִ�����python auto_****.py�����нű�
3.��Ҫ���ܣ�����keypair�����������������floating ip���������װpuppet�������work��ӹ�Կ
4.�����ļ�˵����
[nova_auth]
os_username = nova��¼�û���
os_password = nova��¼����
os_tenant_name = novaʹ�õ�projectid
os_auth_url = nova��֤url

[server_create]
key_path = keypair����·��
key_name = keypair����
key_save_url = ����keypair��������ip��·��
name = ���������
image = ����id
flavor = flavorid
security_groups = ��ȫ������
pool = floating ip��
floating_ip = ���ɵ�floating ip(��������)

[ssh_puppet_install]
ssh_username = ������û���
repo_save_path = ����repo��·��
repo_1_url = ����repo��url
repo_2_url = ����repo��url
public_key_save_path = ��Կ���·��
public_key_url = ���ع�Կ��url(ֻ��Ŀ¼)
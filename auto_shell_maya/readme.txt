1.���ļ��з��ڰ�װ��openstack�Ļ���������·����
2.ִ�����python auto_server_create.py�����нű�
3.��Ҫ���ܣ�����keypair�����������������floating ip�������/workĿ¼��ӹ�Կ�����������yum��repo���������װlibxp������������ز���װmaya��������ƽ�maya��
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

[ssh_install]
ssh_username = ������û���
public_key_url = ���ع�Կ��url(ֻ��Ŀ¼)
public_key_save_path = ��Կ���·��
base_repo_url = ���ػ���repo��url
epel_repo_url = ������չrepo��url
repo_save_path = ����repo��·��
maya_url = ����maya��װ�ļ���url
maya_name = maya��װ�ļ�������
maya_save_path = ����maya��װ�ļ���·��
maya_folder_path = ��ѹ��maya�ļ��е�·��
maya_folder_name = ��ѹ��maya�ļ��е�����
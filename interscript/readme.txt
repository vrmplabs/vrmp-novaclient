1.��.py�ļ����ڰ�װ��openstack�Ļ���������·����
2.ִ�����python ****.py�����нű�
3.������ʾ������ز���
4.����˵����

vrmp_servers.create.py(������������õ�id):
name(���������):����
image(����id):���� ���б�õ�ֵ
flavor(flavorid):���� ���б�õ�ֵ
userdata(userdata):�Ǳ���
key_name(keypair����):�Ǳ��� ���б�õ�ֵ ע�������б�����ʵ�����ƣ�����id
security_groups(��ȫ������):�Ǳ��� ���б�õ�ֵ������Ϊ���ֵ����Ƕ��ŷָ� ע�������б�����ʵ�����ƣ�����id

vrmp_servers.add_floating_ip.py(Ϊ��������floating ip):
server(�����id):���� ���б�õ�ֵ
address(ip��ַ):���� ���б�õ�ֵ

vrmp_security_groups.create.py(������ȫ��):
name(��ȫ������):����
description(��ȫ������):����

vrmp_security_groups.delete.py(ɾ����ȫ��):
group(��ȫ��id):���� ���б�õ�ֵ

vrmp_security_group_rules.create.py(������ȫ�����):
parent_group_id():���� ���б�õ�ֵ
ip_protocol():���� tcp/udp/icmp��ѡһ
from_port():���� ����ʾ��Χ����
to_port():���� ����ʾ��Χ����
group_id():�Ǳ��� ��security group�б�õ�ֵ
cidr():�Ǳ��� Ĭ��0.0.0.0/0

vrmp_security_group_rules.delete.py(ɾ����ȫ�����):
rule(����id):���� ���б�õ�ֵ

vrmp_keypairs.create.py(����key):
name(key����):����
public_key(�����keyֵ):�Ǳ��� ������λ�û��

vrmp_keypairs.delete.py(ɾ��key):
key(key����):���� ���б�õ�ֵ

vrmp_flavors.create.py(����flavor):
flavorid(flavorid):���� �������Ĭ��ֵ����������б�ѡ�񲻴��ڵ�id
name(flavor����):����
vcpus(����cpu����):����
ram(�ڴ��СMB):����
disk(root���̴�СGB):����
ephemeral(ephemeral���̴�СGB):�Ǳ��� Ĭ��0

vrmp_flavors.delete.py(ɾ��flavor):
flavor(flavorid):���� ���б�õ�ֵ
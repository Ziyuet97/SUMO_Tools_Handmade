 
from lxml import etree 
import os


def get_xml_files(path):
    xml_list = []
    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            xml_list.append(os.path.join(path, filename))
    return xml_list
 
def createFile(oripath):
    xml_list = get_xml_files(oripath)
    for i in xml_list:  # 遍历所有xml文件
        change_(i)  # 将完整路径作为参数传入调用该函数
 
 
def change_(path):  # path 是原来xml文件的完整路径
    tree = etree.parse(path)
    root = tree.getroot()
    jcs = root.findall('junction')
    for jc in jcs:  # i是该xml中的所有标签  
        if jc.attrib['type'] in ["rail_signal"]:

            jc.attrib['type'] ='priority'
    connections = root.findall('connection[@tl]')
    for connection in connections:
            connection.attrib.pop("tl", None)
            etree.dump(connection)









            # parent=connection.getparent()
            # parent.remove(connection)           


        # etree.dump(connection) // ==print connection


    with open('E:\sumo\\RL\\1234\\1234.net.xml', 'wb') as f:
        tree.write(f, encoding='utf-8')
 
 
if __name__ == '__main__':
    path = r'E:\sumo\tools\2023-08-18-14-00-05\netwenjian' #你要处理的xml文件所在的文件夹路径
    createFile(path)

import os

import yaml


class  YamlUtils:
    #读取yaml文件
   def  read_extract_yaml(self, key):
       with open(os.getcwd()+"/extract.yaml",mode="r",encoding="utf-8") as f:
           value=yaml.load(strean=f,Loader=yaml.FullLoader)
           return  value[key];

          #写入yaml文件
   def write_extract_yaml(self, data):
        with open(os.getcwd() + "/extract.yaml", mode="r", encoding="utf-8") as f:
            value = yaml.dump(data=data,strean=f, Loader=yaml.FullLoader,allow_unicode=True)
            return value;
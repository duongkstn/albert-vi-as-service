<h2 align="center">What is it</h2>
`albert-vi-as-service` is a fork of [bert-as-service](https://github.com/hanxiao/bert-as-service) to deploy [albert_vi](https://github.com/ngoanpv/albert_vi) 

<h2 align="center">Install</h2>

Install the server and client via `pip`. They can be installed separately or even on *different* machines:
```bash
# server
git clone https://github.com/duongkstn/albert-vi-as-service.git
cd albert-vi-as-service/server
pip install albert-vi-serving-server  
python setup.py install

#client
pip install bert-serving-client==1.10.0  # client, independent of `albert-vi-as-service`
```


<h2 align="center">Getting Started</h2>

#### 1. Download a Pre-trained ALBERT_VI Model
Download a model of [albert_vi](https://github.com/ngoanpv/albert_vi), remember to download sentence piece model

#### 2. Start the ALBERT_VI service
After installing the server, you should be able to use `albert-vi-serving-start` CLI as follows:
```bash
albert-vi-serving-start -model_dir albert_vi_model/ -spm_model_file albertvi_30k-clean.model -config_name albert_config.json -ckpt_name model.ckpt-1015000
```
At client side, your code should be similar to original bert-as-service repos 

It is noted that you can still use `bert-serving-start` command independently
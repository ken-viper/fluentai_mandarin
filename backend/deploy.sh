#!/bin/bash
cd /home/ubuntu/fluentai-be
git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart fluentai-be
sleep 5
sudo systemctl status fluentai-be

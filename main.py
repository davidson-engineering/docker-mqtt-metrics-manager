#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2023-01-23
# version ='1.0'
# ---------------------------------------------------------------------------
"""a_short_project_description"""
# ---------------------------------------------------------------------------

from mqtt_node_network.configure import initialize
from mqtt_node_network.client import MQTTClient

config = initialize(
    config="config/config.toml", secrets=".env", logger="config/logger.yaml"
)


def start_client():
    client = MQTTClient(broker_config=config["mqtt"]["broker"])


if __name__ == "__main__":
    start_client()

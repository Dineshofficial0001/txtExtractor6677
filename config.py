#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8023907692:AAELv_YzyTBvLfFIS1Crck8S5vXuEsXo-5g")
    API_ID = int(os.environ.get("API_ID", "21364683"))
    API_HASH = os.environ.get("API_HASH", "3c160af344efb5c87de7bb76a7107cd9")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6416816452")

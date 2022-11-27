# Testing out Versa FlexVNF with scrapli

Ran into some issues with the <a href="https://github.com/scrapli/scrapli_community" target="_blank">community version of scrapli</a> running Versa FlexVNF. It seems like some of the privilege level patterns needed to be changed, and the escalate, and deescalate commands. Still needs some testing. Not sure on how to handling going from shell to cli in the same session.

I took from the IOSXEDriver and AsyncIOSXEDriver to pull the base layout for the VersaFlexVNF class which is a child of the NetworkDriver class. There the text_fsm and genie settings were changed, default privilege, and on_open/on_close settings. the community version Versa base driver was used for the patterns. The regex needed to be changed and escalate/deescalate settings. Still not sure why a space doesn't work, but space{,1} does. The sync driver was changed to first go into cli because if you want to run commands in shell those paging settings will go away because they are per-session.

Would like to see how to handle the versa "| display json" with either adding this to the end of every command sent to the cli, and add this to the response object as json/dictionary. So far this is handled separately.

## Getting started

This assumes you have a Versa FlexVNF lab device to run on

### Clone and install dependencies

```bash
git clone https://github.com/DavidTWynn/versa_flexvnf_scrapli.git
cd versa_flexvnf_scrapli
python3.10 -m pip install -r requirements.txt
```

### Create settings.json based off of example_settings.json

```javascript
{ "lab_device": {
    "host": "127.0.0.1",
    "auth_username": "admin",
    "auth_password": "versa123"
    }
}
```

### Run Script

```python
python versa_scrapli.py
```

The xiaomi air condition partner remote platform allows you to send IR commands from your Xiaomi Air Condition partner.

Please follow the instructions on Retrieving the Access Token to get the API token to use in the configuration.yaml file.

Configuring the Platform
To add a Xiaomi Air Condition partner to your installation, add the following to your configuration.yaml file:

remote:
  - platform: xiaomi_miio
    host: 192.168.42.42
    token: YOUR_TOKEN
CONFIGURATION VARIABLES
host
(string)(Required)The IP of your remote.

token
(string)(Required)The API token of your remote.

name
(string)(Optional)The name of your remote.

slot
(int)(Optional)The slot used to save learned command.

Default value: 1

timeout
(int)(Optional)Timeout for learning a new command.

Default value: 30

hidden
(boolean)(Optional)Hide the entity from UI. There is currently no reason to show the entity in UI as turning it off or on does nothing.

Default value: true

commands
(map)(Optional)

command
(list)(Required)A list of commands as raw (learned command) or pronto hex code.

Other configures same as Xiaomi IR Remote:
https://www.home-assistant.io/components/remote.xiaomi_miio/

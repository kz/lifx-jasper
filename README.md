# lifx-jasper
lifx-jasper is a [Jasper](http://jasperproject.github.io/) module built to control all of your LIFX lights using your voice.

lifx-jasper utilises:
- the LIFX HTTP Cloud API using the [lifx-cli](https://github.com/Rawa/lifx-cli) application by executing its commands in the shell
- the [LIFX Python SDK](https://github.com/smarthall/python-lifx-sdk) for basic commands such as on/off/toggle.

The reason for building this project is because I have a single LIFX light situated in my bedroom which I would like to control using my voice. Therefore, this repository will not have the handling of individual lights in mind, although it may be something I will consider in the future.

## Installation
1. Navigate to `~/jasper/client/modules` folder, assuming that your Jasper files are situated under your home directory
2. Clone this repository into `/tmp` or any temporary folder that can be deleted afterwards and move `Light.py` into the modules folder
3. Clone [lifx-cli](https://github.com/Rawa/lifx-cli) to a folder such as `~/lifx-cli`
4. Follow the lifx-cli installation in its README, including the creation of its `lifx-token` file
5. Run `sudo pip install lifx-sdk` to install the [Python LIFX SDK](https://github.com/smarthall/python-lifx-sdk).
6. Create the file `~/.lifx-jasper/config.yml` based on this repository's `config.yml` file
7. Boot Jasper and you should be ready to go!

## Usage and Commands
To activate the LIFX module, your speech command must include `light` or `lights`. For example, you can say `lights on` to turn all lights on. Here is a list of other commands:

- `on` or `enable` - Turns all lights on
- `off` or `disable` - Turns all lights off
- Just saying `light` or `lights` toggles all lights

To implement:
- Presets

## License
Please see [LICENSE.md](LICENSE.md) for more details.

# lifx-jasper
lifx-jasper is a [Jasper](http://jasperproject.github.io/) module built to control all of your LIFX lights using your voice.

lifx-jasper utilises the LIFX HTTP Cloud API using the [lifx-cli](https://github.com/Rawa/lifx-cli) application by executing its commands in the shell.

The reason for building this project is because I have a single LIFX light situated in my bedroom which I would like to control using my voice. Therefore, this repository will not have the handling of individual lights in mind, although it may be something I will consider in the future.

## Code Example
Code examples will be included once this project is functional.

## Installation
1. Navigate to `~/jasper/client/modules` folder, assuming that your Jasper files are situated under your home directory
2. Download a release and move `Light.py` into the modules folder
3. Clone [lifx-cli](https://github.com/Rawa/lifx-cli) to a folder such as `~/lifx-cli`
4. Follow the lifx-cli installation in its README, including the creation of its `lifx-token` file
5. Create the file `~/.config/lifx-jasper/lifx-cli-path` and enter the path to lifx-cli's `lifx` file - e.g., `~/lifx-cli/lifx`
4. Boot Jasper and you should be ready to go!

## License
Please see [LICENSE.md](LICENSE.md) for more details.

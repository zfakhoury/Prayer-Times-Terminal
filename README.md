# Prayer-Times-Terminal

This repository includes a python script that takes shows islamic prayer times for a given country and city.

## Running the program in an executbale file (shortcut)

First of all, set the variables `country` and `city` to your desired default values.

### All platforms - pyinstaller package

- Make sure `pyinstaller` is installed by running in the terminal: `pip3 install pyinstaller`
- Set working directory to the location of `prayer_times.py`
- Run `pyinstaller prayer_times.py --onefile --noconsole`

The command produces 2 folders: `build` and `dist`.

The executable file is contained in the `dist` folder.

### macOS Specific

- Open `prayer_times.py` and add at the very top: `#!/usr/bin/env python`
- Rename the file to `prayer_times.command`
- Convert to executable by running in the terminal: `chmod +x prayer_times.command`

---

Once the executable file has been created, you can copy it to your Desktop for example and check prayer times instantly with a double click.

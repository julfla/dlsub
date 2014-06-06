dlsub
=====

Automatic subtitle downloader

# Dependencies
  ```bash
  sudo apt-get install libvlc-dev libvlccore-dev
  ```

# Install
  ```bash
  sudo ln -s $(pwd)/libfoo_plugin.so /usr/lib/vlc/plugins/misc/
  ```

# Remove
  Just delete what has been done previously
  ```bash
  sudo rm /usr/lib/vlc/plugins/misc/libfoo_plugin.so
  ```

# Testing
  ```bash
  vlc --list | grep foo
  vlc --extraintf foo
  ```


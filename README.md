# bash-slugify

## Installation

Place `slugify.sh` into your `~/.local/bin/` directory as `slugify` and assign executable permissions to it.

```shell-script
wget -O ~/.local/bin/slugify https://raw.githubusercontent.com/barseghyanartur/bash-slugify/main/slugify.sh
chmod +x ~/.local/bin/slugify
```

Or just use one-liner:

```shell-script
wget -O ~/.local/bin/slugify https://raw.githubusercontent.com/barseghyanartur/bash-slugify/main/slugify.sh && chmod +x ~/.local/bin/slugify
```

## Usage examples

```shell-script
slugify "Lorem ipsum dolor sit amet, consectetur's adipiscing elit"
# lorem-ipsum-dolor-sit-amet-consectetur-s-adipiscing-elit
```

## Testing

```shell-script
python -m tests
```

## License

LGPL-2.1-or-later

## Author

Artur Barseghyan [artur.barseghyan@gmail.com](mailto:artur.barseghyan@gmail.com)

# bash-slugify

## Installation

Place `slugify.sh` into your `~/.local/bin/` directory as `slugify` and assign executable permissions to it.

**Using `wget`**

```shell-script
wget -O ~/.local/bin/slugify https://raw.githubusercontent.com/barseghyanartur/bash-slugify/main/slugify.sh && chmod +x ~/.local/bin/slugify
```

**Using `curl`**

```shell-script
curl -o ~/.local/bin/slugify https://raw.githubusercontent.com/barseghyanartur/bash-slugify/main/slugify.sh && chmod +x ~/.local/bin/slugify
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

MIT

## Author

Artur Barseghyan [artur.barseghyan@gmail.com](mailto:artur.barseghyan@gmail.com)

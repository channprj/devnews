# Devnews
- 한국 개발자들을 위한 뉴스/블로그/슬라이드/비디오 공유 사이트

## Getting Started

### Prerequisites
- [direnv](https://direnv.net/)
- Python >= 3.7
  - [pyenv](https://github.com/pyenv/pyenv/)
  - [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Docker](https://docker.com/)

### Installation
Add this in your `~/.direnvrc`.
```bash
use_python() {
  local python_root=$HOME/.pyenv/versions/$1
  load_prefix "$python_root"
  layout_python "$python_root/bin/python"
}
```

Add `eval "$(direnv hook zsh)"` in your run commands.
```bash
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc # or .bashrc
```

Setup requirements like below:
```bash
# Setup and activate virtual environments with pyenv and direnv
pyenv install 3.7.2
direnv allow

# Install packages
pip install -r requirements.txt

# Deploy mysql for dev
docker run --name devnews-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=devnews-db -e MYSQL_USER=devnews-user -e MYSQL_PASSWORD=devnews-password -d mariadb

# Optional: Connect db shell
mysql -h0 -udevnews-user -pdevnews-password devnews-db

# Optional: Change default admin theme - uswds
./manage.py loaddata admin_interface_theme_uswds.json

# Run in local
./manage.py runserver 0:8000
```

## Deployment
> Work in progress...

## Built With
- [Docker](https://www.docker.com/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [React.js](https://reactjs.org/)
- [Ant Design](https://ant.design/)

## Contributing
Please read [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/tebica/devnews/tags).

## Authors
- [tebica](https://github.com/tebica) - *Project owner*
- [channprj](https://github.com/channprj) - *Initial work*

See also the list of [contributors](https://github.com/tebica/devnews/contributors) who participated in this project.

## License
- [MIT License](LICENSE)

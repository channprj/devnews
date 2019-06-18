# Devnews
> Work in progress...

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

Setup requirements like below:
```bash
# Setup and activate virtual environments with pyenv and direnv
pyenv install 3.7.2
direnv allow

# Install packages
pip install -r requirements.txt

# Deploy postgresql for dev
docker run --name devnews-postgres -p 5432:5432 -e POSTGRES_DB=devnews-db -e POSTGRES_USER=devnews-user -e POSTGRES_PASSWORD=devnews-password -e POSTGRES_INITDB_ARGS=--encoding=UTF-8 -d postgres

# Optional: Connect db shell
psql --host localhost dbname=devnews-db --username devnews-user

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

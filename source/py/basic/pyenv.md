# Pyenv

```shell
curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


pyenv install --list | grep ' 3.9'

pyenv install 3.9.4

pyenv versions

pyenv global 3.8.0

pyenv local 2.7.17
```
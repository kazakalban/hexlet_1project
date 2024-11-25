install: # устанавливает зависимости проекта из pyproject.toml и фиксирует версии из poetry.lock, создавая или обновляя виртуальное окружение.
	poetry install

brain-games: #выполняет команду poetry run brain-games
	poetry run brain-games

brain-even: #выполняет команду poetry run brain-even
	poetry run brain-even

brain-calc: #выполняет команду poetry run brain-calc
	poetry run brain-calc

build: #создаёт дистрибутивы проекта (форматы sdist и wheel) на основе pyproject.toml. Это нужно для публикации или распространения пакета.
	poetry build

publish: #имитирует процесс публикации пакета на указанный репозиторий без фактической отправки. Используется для проверки, что всё настроено правильно.
	poetry publish --dry-run

package-install: # устанавливает скомпилированный пакет из файла .whl (расположенного в папке dist) для текущего пользователя без затрагивания системных пакетов.
	python3 -m pip install --user dist/*.whl --force-reinstall

lint: # проеверяет код на flake8
	poetry run flake8 brain_games
add_git_package-install:
	git add dist/hexlet_code-0.1.0-py3-none-any.whl dist/hexlet_code-0.1.0.tar.gz
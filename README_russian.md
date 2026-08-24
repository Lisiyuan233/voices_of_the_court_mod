# Часто задаваемые вопросы

## 1. Диалоговое окно не появляется
Этот мод требует дополнительную фоновую программу для работы. Скачайте локализованную фоновую программу здесь: [https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest). Скачанный .exe файл установится автоматически при открытии.

## 2. Проблемы с настройкой API
Рекомендуется использовать официальный DeepSeek API. В выпадающем меню для подключения модели диалога выберите страницу `custom(openai-compatible)` для настройки:
- URL сервера: `https://api.deepseek.com/beta`
- API ключ: Введите ваш собственный API ключ, который можно получить на [https://platform.deepseek.com](https://platform.deepseek.com).

OpenAI и OpenRouter также должны быть совместимы.

## 3. Диалоговое окно не появляется, даже когда фоновая программа запущена после установки
**Решение**: Вы должны использовать локализационный мод.

Способы установки (выберите один):
1. После извлечения скачанных файлов локализационного мода, перезапишите оригинальные файлы мода в директории Steam Workshop напрямую.
2. Поместите извлечённую папку мода `voices_of_the_court_mod-1.2.1-beta` в папку модов игры. Затем используйте Блокнот, чтобы создать новый файл с именем `voices_of_the_court_mod-1.2.1-beta.mod` в папке `Documents\Paradox Interactive\Crusader Kings III\mod` со следующим содержимым:
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [Ваше имя пользователя ПК здесь] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

Если диалоговое окно всё ещё не появляется после установки и включения локализационного мода, путь к папке пользователя CK3 может быть установлен неправильно, или игра может быть в режиме Ironman. Этот мод не работает в режиме Ironman.

## 4. Ошибка "TypeError: Cannot read properties of undefined (reading 'playerID')" с красным текстом при открытии окна чата
**Решение**: Создайте папку с именем `run` в `Documents\Paradox Interactive\Crusader Kings III`. Войдите в эту папку и создайте текстовый файл с именем `votc.txt`.

## 5. Недавние воспоминания не читаются при разговоре с персонажами
**Решение**:
1. Это небольшая ошибка в оригинальной фоновой программе автора; скачивание локализованной фоновой программы решает эту проблему.
2. Это также может быть из-за ограничений токенов памяти. Настройте размер `max memory tokens` на странице настроек фоновой программы. После настройки токенов памяти вы также должны увеличить `max new tokens`; лучше, если `max new tokens` будет больше, чем `max memory tokens`.

## 6. Скрипт генерации промпта сбрасывается после перезапуска фоновой программы
**Решение**:
Сохраните его как отдельный файл в папке `custom`.

## Лицензия и Атрибуция

### Информация о моде
- **Название мода**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **Лицензия**: GNU General Public License v3.0 (GPLv3)
- **Поддерживаемая версия CK3**: 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### Уведомление GPLv3
Эта программа является свободным программным обеспечением: вы можете распространять и/или изменять её в соответствии с условиями GNU General Public License, опубликованной Free Software Foundation, либо версии 3 Лицензии, либо (по вашему выбору) любой более поздней версии.

Эта программа распространяется в надежде, что она будет полезной, но БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемой гарантии КОММЕРЧЕСКОЙ ЦЕННОСТИ или ПРИГОДНОСТИ ДЛЯ КОНКРЕТНОЙ ЦЕЛИ. Подробнее см. в GNU General Public License.

Вы должны были получить копию GNU General Public License вместе с этой программой. Если нет, см. <https://www.gnu.org/licenses/>.

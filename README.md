# Frequently Asked Questions

## 1. No dialog box pops up
This mod requires an additional backend program to run. Download the localized backend program here: [https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest). The downloaded .exe file will install automatically upon opening.

## 2. API configuration issues
It is recommended to use the official DeepSeek API. In the dropdown menu for the dialogue model connection, select the `custom(openai-compatible)` page to configure:
- Server URL: `https://api.deepseek.com/beta`
- API Key: Enter your own API key, which can be applied for at [https://platform.deepseek.com](https://platform.deepseek.com).

OpenAI and OpenRouter should also be compatible.

## 3. No dialog box pops up even when the backend program is running after installation
**Solution**: You must use the localization mod.

Installation methods (choose one):
1. After extracting the downloaded localization mod files, overwrite the original mod files in the Steam Workshop directory directly.
2. Place the extracted mod folder `voices_of_the_court_mod-1.2.1-beta` into the game's mod folder. Then, use Notepad to create a new file named `voices_of_the_court_mod-1.2.1-beta.mod` in the `Documents\Paradox Interactive\Crusader Kings III\mod` folder with the following content:
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [Your PC Username Here] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

If the dialog box still does not appear after installing and enabling the localization mod, the CK3 user folder path may be set incorrectly, or the game might be in Ironman mode. This mod does not work in Ironman mode.

## 4. Error "TypeError: Cannot read properties of undefined (reading 'playerID')" with red text when opening the chat window
**Solution**: Create a folder named `run` in `Documents\Paradox Interactive\Crusader Kings III`. Enter that folder and create a text file named `votc.txt`.

## 5. Recent memories are not being read when talking to characters
**Solution**:
1. This is a small bug in the original author's backend program; downloading the localized backend solves this.
2. It may also be due to memory token limits. Adjust the `max memory tokens` size in the backend program's settings page. After adjusting the memory tokens, you should also increase the `max new tokens`; it is best if `max new tokens` is larger than `max memory tokens`.

## 6. Prompt generation script reverts after restarting the backend program
**Solution**:
Save it as a separate file in the `custom` folder.

## License and Attribution

### Mod Information
- **Mod Name**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **License**: GNU General Public License v3.0 (GPLv3)
- **Supported CK3 Version**: 1.18 "Crane"

### Credits & Attribution
This project, Voices of the Court 2.0 - Community Edition, is a derivative work of Voices of the Court (VOTC) / AliChat.

**Original Work**: Voices of the Court and Voices of the Court 2.0 Mod

**Original Authors**: The VOTC Team, Durond, MrAndroPC, and community contributors.

**Source**: [https://github.com/Voices-of-the-Court/votc_mod](https://github.com/Voices-of-the-Court/votc_mod)

**Original License**: Licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) and GNU GPLv3.

**Modifications**:

* Integration with Voices of the Court 2.0 - Community Edition
* Added features
* Added bug fixes

Relicensed derivative works under GNU GPLv3 as a compatible ShareAlike license.

### GPLv3 Notice
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

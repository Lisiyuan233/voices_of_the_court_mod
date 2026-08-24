# 자주 묻는 질문

## 1. 대화창이 뜨지 않습니다
이 모드를 실행하려면 추가 백엔드 프로그램이 필요합니다. 여기에서 현지화된 백엔드 프로그램을 다운로드하세요: [https://github.com/szmania/Voices_of_the_Court/releases/latest](https://github.com/szmania/Voices_of_the_Court/releases/latest). 다운로드한 .exe 파일은 실행 시 자동으로 설치됩니다.

## 2. API 설정 문제
공식 DeepSeek API 사용을 권장합니다. 대화 모델 연결 드롭다운 메뉴에서 `custom(openai-compatible)` 페이지를 선택하여 다음과 같이 설정하세요:
- 서버 URL: `https://api.deepseek.com/beta`
- API 키: [https://platform.deepseek.com](https://platform.deepseek.com)에서 신청한 본인의 API 키를 입력하세요.

OpenAI 및 OpenRouter도 호환될 것입니다.

## 3. 설치 후 백엔드 프로그램이 실행 중인데도 대화창이 뜨지 않습니다
**해결책**: 현지화 모드를 사용해야 합니다.

설치 방법 (택일):
1. 다운로드한 현지화 모드 파일의 압축을 푼 후, Steam Workshop 디렉토리의 원본 모드 파일에 직접 덮어씁니다.
2. 압축을 푼 모드 폴더 `voices_of_the_court_mod-1.2.1-beta`를 게임의 모드 폴더에 넣습니다. 그런 다음 메모장을 사용하여 `Documents\Paradox Interactive\Crusader Kings III\mod` 폴더에 `voices_of_the_court_mod-1.2.1-beta.mod`라는 이름의 새 파일을 만들고 다음 내용을 입력합니다:
version="1.0"
tags={
"Gameplay"
}
name="Voices of the Court mcc"
supported_version="1.13.1"
path="C:/Users/ [사용자 PC 이름] / Documents/Paradox Interactive/Crusader Kings III/mod/voices_of_the_court_mod-1.2.1-beta"

현지화 모드를 설치하고 활성화했는데도 대화창이 나타나지 않는다면, CK3 사용자 폴더 경로가 잘못 설정되었거나 게임이 아이언맨 모드일 수 있습니다. 이 모드는 아이언맨 모드에서 작동하지 않습니다.

## 4. 채팅창을 열 때 빨간색 텍스트로 "TypeError: Cannot read properties of undefined (reading 'playerID')" 오류가 발생합니다
**해결책**: `Documents\Paradox Interactive\Crusader Kings III` 안에 `run`이라는 이름의 폴더를 만듭니다. 해당 폴더로 들어가 `votc.txt`라는 이름의 텍스트 파일을 만듭니다.

## 5. 캐릭터와 대화할 때 최근 기억이 읽히지 않습니다
**해결책**:
1. 이것은 원작자의 백엔드 프로그램에 있는 작은 버그입니다. 현지화된 백엔드를 다운로드하면 해결됩니다.
2. 메모리 토큰 제한 때문일 수도 있습니다. 백엔드 프로그램의 설정 페이지에서 `max memory tokens` 크기를 조정하세요. 메모리 토큰을 조정한 후에는 `max new tokens`도 늘려야 합니다. `max new tokens`가 `max memory tokens`보다 큰 것이 가장 좋습니다.

## 6. 백엔드 프로그램을 재시작하면 프롬프트 생성 스크립트가 초기화됩니다
**해결책**:
`custom` 폴더에 별도의 파일로 저장하세요.

## 라이선스 및 저작권 표시

### 모드 정보
- **모드 이름**: Voices of the Court 2.0 - Community Edition (VOTC-CE)
- **라이선스**: GNU General Public License v3.0 (GPLv3)
- **지원 CK3 버전**: 1.18 "Crane"

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

### GPLv3 고지
이 프로그램은 자유 소프트웨어입니다: Free Software Foundation에서 게시한 GNU General Public License의 조건에 따라 이 프로그램을 재배포 및/또는 수정할 수 있습니다. 라이선스 버전 3 또는 (선택에 따라) 이후 버전 중 하나입니다.

이 프로그램은 유용할 것이라는 희망으로 배포되지만, 상품성이나 특정 목적에의 적합성에 대한 묵시적 보증을 포함한 어떠한 보증도 없습니다. 자세한 내용은 GNU General Public License를 참조하십시오.

이 프로그램과 함께 GNU General Public License의 사본을 받았어야 합니다. 그렇지 않은 경우 <https://www.gnu.org/licenses/>를 참조하십시오.

# Custom PARA Template

**PARA 방식**(Projects, Areas, Resources, Archives) 기반의 workspace template

---

## 구조 요약

- `1_Projects/`: 명확한 목표와 마감기한이 있는 단기 작업
- `2_Areas/`: 지속적인 유지보수와 관리가 필요한 장기 책임 영역
- `3_Resources/`: 향후 참조를 위한 지식, 코드 조각, 템플릿, 프로토콜 등 재사용 가능한 자료
- `4_Archives/`: 완료되거나 보관 처리된 항목 (상위 P/A/R 구조를 미러링)

세부 규칙 및 명명 규칙은 [`AGENTS.md`](AGENTS.md)를 참고하십시오.

---

## 스킬별 선행 설치 요구사항 (Prerequisites)

`.agents/skills/`에 포함된 커스텀 스킬 중 외부 프로그램이나 CLI 도구 연동이 필요한 스킬들의 사전 준비 사항입니다.

### 1. 비텍스트 문서 변환 (`read-document-with-pandoc`)
Word(`.docx`), PowerPoint(`.pptx`), OpenDocument(`.odt`), RTF, EPUB, LaTeX(`.tex`), HTML 문서를 Markdown이나 텍스트로 변환하여 분석하는 스킬입니다.

- **필수 도구**: Pandoc CLI
- **설치 방법**:
  - Windows 패키지 관리자:
    ```powershell
    winget install JohnMacFarlane.Pandoc
    ```
  - 공식 설치 파일: [Pandoc 공식 다운로드](https://pandoc.org/installing.html)

### 2. Zotero 참고문헌 라이브러리 연동 (`manage-zotero-library`)
로컬 Zotero 데스크톱과 연동하여 논문 검색, DOI/PMID 기반 임포트, BibTeX 내보내기, 본문 인용 처리를 수행하는 스킬입니다.

- **필수 프로그램 및 도구**:
  1. **Zotero Desktop (v7 / v8 / v9)**:
     - 스킬 실행 시 로컬에 Zotero 프로그램이 실행되어 있어야 합니다.
     - 다운로드: [Zotero 공식 웹사이트](https://www.zotero.org/download/)
  2. **zotero-cli (`cli-anything-zotero`)**:
     - Python 기반 독립형 CLI 도구입니다. `uv`를 사용하여 전역 도구로 간편하게 설치할 수 있습니다.
     - 설치 명령:
       ```powershell
       uv tool install cli-anything-zotero
       ```
     - 브릿지 플러그인 설치 (Zotero 데스크톱 실행 상태에서 실행):
       ```powershell
       zotero-cli app install-plugin
       ```
  3. **(선택 사항) LibreOffice**:
     - Word(`.docx`) 문서 내 새로고침 가능한 동적 인용 필드를 삽입할 때 필요합니다. 일반 텍스트 인용 생성 시에는 필요하지 않습니다.

---

## 스킬 의존성 요약

| 스킬 | 역할 | 선행 설치 요구사항 |
|---|---|---|
| `init-para-project` | 기본 PARA 디렉토리 및 AGENTS.md 초기화/검증 | 없음 |
| `init-project` | 1_Projects 폴더 내 5단계 프로젝트 구조 생성 | 없음 |
| `init-log` | 00-log 감사 추적(이슈 및 결정 기록) 관리 | 없음 |
| `validate-para-structure` | 디렉토리 명명 규칙 및 구분자 유효성 검사 | 없음 |
| `archive-para-item` | ISO 분기 태그를 부여하여 4_Archives로 보관 | 없음 |
| `review-paper` | 정형화된 학술 논문 리뷰 포맷 작성 | 없음 |
| `read-document-with-pandoc` | 문서(docx, pptx 등) Markdown 변환 열람 | **Pandoc CLI** |
| `manage-zotero-library` | Zotero 논문 검색, 인용 및 라이브러리 관리 | **Zotero Desktop**, **zotero-cli (`uv tool install`)**, JS Bridge 플러그인 *(동적 인용 시 LibreOffice 선택)* |

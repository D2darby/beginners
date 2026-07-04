# Beginners 포트폴리오 — 설치 가이드 v1.0
파일: README_설치가이드_v1.0.md / 대상: beginners_portfolio_v1.0.zip / 작성: 2026-07-04 Claude

**소요 약 20분, 전부 무료.** 순서대로만 하면 됨. 막히면 단계 번호 말해줘.

---

## 구조 요약
- 사진·태그의 원본은 **지금 그대로 Notion 기록 DB** (Drive→Make 자동화 그대로 살아있음)
- 이 사이트는 Notion을 읽어서 미술관 톤으로 보여주는 **얼굴**
- 매시간 자동 갱신 + 수동 즉시 갱신 버튼
- zip에 현재 사진 4장이 이미 들어있어서 **토큰 없이도 업로드 즉시 작동**

## 1. GitHub 가입 (있으면 건너뜀)
1. github.com → Sign up → 이메일 인증까지

## 2. 저장소(repo) 만들기
1. 우상단 **+** → **New repository**
2. Repository name: `beginners`
3. **Public** 선택 (GitHub Pages 무료 조건)
4. **Create repository**

## 3. 파일 업로드
1. zip 압축 해제
2. repo 화면에서 **uploading an existing file** 클릭
3. 압축 푼 **폴더 안의 내용물 전부** 드래그:
   - `index.html`
   - `photos.json`
   - `scripts` 폴더
   - `.github` 폴더 ← **이게 빠지면 자동 갱신이 안 됨.** 숨김 폴더라 안 보이면 Finder에서 `Cmd+Shift+.`
4. 하단 **Commit changes**

## 4. Pages 켜기 (사이트 공개)
1. repo → **Settings** → 왼쪽 **Pages**
2. Source: **Deploy from a branch** / Branch: **main** / 폴더: **/(root)** → **Save**
3. 1~2분 뒤 상단에 주소 표시: `https://<계정명>.github.io/beginners/`
4. 열어서 사진 4장 뜨는지 확인 ← **여기까지가 사이트 오픈**

## 5. Notion 토큰 발급 (자동 갱신용)
1. notion.so/profile/integrations (또는 설정 → 내 연결 → 통합 개발)
2. **New integration** → 이름 `beginners-site` → Internal → 워크스페이스 선택
3. Capabilities: **Read content**만 있으면 됨
4. **Internal Integration Secret** 복사 (`ntn_...` 또는 `secret_...`)
5. Notion 앱에서 **Beginners — 김가족 기록** 홈 → 우상단 ⋯ → **연결** → `beginners-site` 추가

## 6. 토큰을 GitHub에 등록
1. repo → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
3. Name: `NOTION_TOKEN` (정확히 이 이름) / Secret: 복사한 값 → **Add secret**

## 7. 자동 갱신 확인
1. repo → **Actions** 탭 → 좌측 **Update photos** → **Run workflow** (수동 즉시 갱신 버튼)
2. 초록 체크 뜨면 성공. 이후엔 매시간 자동
3. 새 사진 플로우: **Drive 폴더에 사진 → (15분 내) Notion 등록 → (다음 정시 23분) 사이트 반영**

## 나중에 할 것
- **도메인 연결**: 도메인 사면 repo Settings → Pages → Custom domain에 입력 + DNS는 그때 내가 가이드. oopy 불필요 (연 6만원 절약)
- **태깅**: 장소·인물은 Notion에서 나한테 시키면 사이트에 자동 반영

## 문제 해결
| 증상 | 원인/조치 |
|---|---|
| 사이트 404 | Pages 설정 직후 1~2분 대기. Branch가 main/(root)인지 확인 |
| 사진 안 뜸 | photos.json 업로드 누락 여부 확인 |
| Actions 빨간 X | Secret 이름이 `NOTION_TOKEN` 정확한지 / 5-5단계(페이지에 연결 추가) 했는지 |
| 자동 갱신 안 됨 | `.github` 폴더 업로드 누락 — 3단계 다시 |

# StudyBuddy MVP — Feature Status Audit

## Context

You asked which features described in your product docs are actually implemented in the current codebase. This file reconciles the two MD sources against the code so you know what's deploy-ready, what's a stub, and what's missing.

Sources cross-referenced:
- `Archives/Startup/StudyBuddy — Product Brief.md` (§5 In/Out scope)
- `Archives/Startup/StudyBuddy – Контекст проекта.md` (§6 implemented, §8 not done)

Project root: `C:\Users\User\Desktop\tg bot 0.6 (settings not working)`.

## Legend
- ✅ Fully implemented
- 🟡 Partial / stub / works differently than described
- ❌ Not implemented (declared in docs but absent in code)
- ⏭ Out of MVP scope per the brief itself (so absence is expected)

## MVP feature matrix

| Feature (per docs) | Status | Evidence | Notes |
|---|---|---|---|
| **Pomodoro timer — standard 25 min** | ✅ | [bot.py:680](bot.py:680) `handle_standard_timer` | Works, with duplicate-timer guard + cancellable task. |
| **Pomodoro timer — custom 5–120 min** | ✅ | [bot.py:711](bot.py:711) `handle_custom_timer_start`, [bot.py:717](bot.py:717) `process_duration` | Range-validated. |
| **Background-run + stop early** | ✅ | [bot.py:739](bot.py:739) `handle_stop_timer`, [bot.py:769](bot.py:769) back-to-menu, `/stop` command added in fix #12 | Stop awards partial coins; `/stop` works from any state. |
| **Study session logging + coins (+1/min)** | ✅ | [services.py:137](services.py:137) `complete_session`; `base_coins = duration` | Atomic under db.lock now. |
| **Streak tracking + midnight reset** | ✅ | [services.py:178](services.py:178) `StreakService.process_all_users`, [tasks.py](tasks.py) `streak_scheduler` at 23:59 MSK | +15 coin bonus from day 2. |
| **Achievement system — 9 categories** | ✅ | [services.py:7-90](services.py:7) `AchievementService` checks 9 ach IDs; `achievements.json` defines them | Progress + completion stored in `user_achievements`. |
| **Digital pet mood** | 🟡 | [bot.py:417-425](bot.py:417) `get_pet_emotion(streak)` | Text-only (emoji + descriptor). Depends **only on streak**, not on "sad if no session today" as the brief describes. No image asset. |
| **Profile screen** | ✅ | [bot.py:395-414](bot.py:395) `cmd_profile` | Shows ID, sessions, coins, streak, last session, pet emotion. |
| **Notification settings — toggle on/off** | ✅ | [bot.py:`NotificationSettings`](bot.py) class + `settings_toggle` callback | Morning / evening / streak / achievements toggles work. |
| **Notification settings — edit times** | ❌ | `get_keyboard()` only emits toggle buttons; no "change time" button or callback | Project context claims `«Изменить утро/вечер»` buttons exist — they don't. Times stay at defaults `09:00` / `21:00`. |
| **Onboarding wizard (set morning + evening + confirm)** | 🟡 | [bot.py:336-352](bot.py:336) `cmd_start` only — sets state to `SetupStates.choosing_path` | FSM states `setting_morning`, `setting_evening`, `confirming` are **declared but have no handlers**. Neither "🔧 Настроить сейчас" nor "🚀 Начать сразу" has a handler. The wizard enters and dead-ends. |
| **Morning reminder notification** | ❌ | No code in `tasks.py` or `bot.py` schedules morning sends. | Project context already calls this out as not done. |
| **Evening reminder if no session yet** | ❌ | Same — no scheduler. | Only the 23:59 streak job runs. |
| **Text quizzes — Production Management** | 🟡 | [bot.py:776+](bot.py:776) handlers exist; `quizzes/production-management/` | **Only Section I has content** (15 terms). Section II file is empty. Sections III and IV files don't exist. Users selecting II/III/IV get "Раздел не найден или пуст". |
| **Smart answer checking** | ✅ | [bot.py:`check_text_answer`](bot.py) | Two-gate: keyword stem-match (fixed in #14) + 80% word overlap with definition. |
| **Spaced repetition scheduling** | 🟡 | [bot.py:`quiz_interval_days`](bot.py) — fixed `[1, 2, 4, 7]` intervals | Brief mentions **SM-2 algorithm**; implementation is simple fixed intervals, not SM-2 (no easiness factor, no quality grade). |
| **User timezone support** | 🟡 | `users.timezone` column defaults to `Europe/Moscow`; never edited by any flow | Stored but no UI to set it; streak job always uses Moscow time regardless of user. |
| **Admin /reply** | ✅ | [bot.py:894](bot.py:894) `cmd_reply` | Works. |
| **Admin /broadcast or mass-message** | ❌ | Not found in codebase. | Brief lists "broadcast" — never implemented. |
| **Data persistence via async SQLite** | ✅ | [db.py](db.py), `aiosqlite`, WAL on | Tables: users, notification_settings, study_sessions, user_achievements, quiz_progress, admins. |
| **FAQ button** | ✅ | [bot.py:357](bot.py:357) `handle_faq` | Static text. |
| **Support / feedback channel** | ✅ | [bot.py:373](bot.py:373) `handle_support` + `handle_any_message` forwards to admins; logs to `messages.log` (post-fix #7) | Live forward works; append-only log post-fix #7. |
| **Tips: time management / memory / links** | ✅ | [bot.py:842-868](bot.py:842) | Reads `timemanagement.txt`, `memoryretention.txt`, `links-to-productivity-material.txt`. |
| **Daily tasks (stub)** | ❌ | No code, no DB table, no button. | Project context says "stub exists" — there is **none** in the current code. |
| **`/help` command** | ❌ | Not implemented. | Listed in docs as "desirable after launch". |
| **Persistent FSM storage** | ❌ | `MemoryStorage()` in `main()` | All FSM state lost on restart (in-progress timers, quizzes, etc.). |
| **Web app** | ⏭ | Out of MVP scope per brief. | Not in code; expected. |
| **Premium / payments** | ⏭ | Out of MVP scope. | Removed from code per project context. |
| **Multi-subject quizzes** | ⏭ | Out of MVP scope. | Expected. |
| **Social features (friends, leaderboards)** | ⏭ | Out of MVP scope. | Expected. |
| **Advanced analytics / charts** | ⏭ | Out of MVP scope. | Expected. |

## Summary

**Implemented (12 features):** Pomodoro standard + custom, session logging + coins, streak tracking + midnight reset, achievements (9 types), profile screen, notification on/off toggles, smart answer checking, fixed-interval review scheduling, async SQLite persistence, /reply admin command, FAQ + support + tips, message audit log.

**Partial / not as described (5 features):**
- Pet mood — depends only on streak (not on "no session today").
- Onboarding wizard — entry exists, body doesn't.
- Quizzes — only Section I has terms; II is empty, III & IV don't exist.
- Spaced repetition — fixed intervals, not SM-2 as brief claims.
- Timezone — stored, never settable; streak job ignores it (always Moscow).

**Declared in docs but missing entirely (6 features):**
- Edit notification times.
- Morning reminders.
- Evening reminders.
- Admin /broadcast.
- Daily tasks (stub).
- /help command.
- Persistent FSM storage.

**Out of MVP scope (expected absent):** web app, premium, multi-subject quizzes, social, analytics.

## Critical-path gaps for MVP

If you want the bot to do what the brief actually promises a user, these are the gaps that matter most for the user-facing experience (ranked by user impact):

1. **Onboarding wizard body** — users tapping "🔧 Настроить сейчас" hit a dead end. Either wire up `setting_morning` / `setting_evening` / `confirming` handlers, or remove the choice and go straight to the main menu.
2. **Morning + evening reminders** — the brief's value prop ("notifications match personal rhythm") doesn't exist. The data model is there (`morning_time`, `evening_time`), just no scheduler.
3. **Quiz sections II-IV content** — selecting them shows an error. Either fill the files or hide the buttons.
4. **Edit notification times** — without this, the time fields in the DB are decorative.

The other gaps (broadcast, daily tasks stub, /help, persistent FSM, SM-2) are described in your docs as nice-to-have / post-launch. Leaving them won't break the user experience.

## Verification

To re-verify any item in this table:

```powershell
# Search for a feature
Grep "feature_name" --type py

# Manual smoke for the wizard dead-end:
# /start → "🔧 Настроить сейчас" → bot is silent (no handler fires)

# Manual smoke for missing reminders:
# Wait until your configured morning_time → nothing arrives
```

No further code changes are part of this plan — this file is the audit deliverable. Use it as the input to decide which gaps to close before launch.

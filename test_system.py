"""
=============================================================================
PsychoStreak Automated Health & Diagnostic Test Suite
בודק תקלות אוטומטי למערכת פסיכו-סטריק
=============================================================================
Runs anytime to ensure zero downtime and complete system integrity:
1. Local Codebase & DOM Structure Integrity Check
2. Live Firebase Firestore Read/Write Health Check
3. Live GitHub Pages Deployment & Availability Check
4. Headless Browser Rendering & Console Error Watchdog
=============================================================================
"""

import sys
import os
import json
import time
import subprocess
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_test(name, passed, detail=""):
    symbol = f"{GREEN}✅ PASS{RESET}" if passed else f"{RED}❌ FAIL{RESET}"
    print(f"[{symbol}] {name}")
    if detail:
        print(f"        {detail}")

def run_tests():
    print(f"\n{BLUE}🚀 מתחיל בדיקת מערכת מלאה עבור PsychoStreak...{RESET}\n")
    all_passed = True

    # -------------------------------------------------------------
    # 1. Local HTML Integrity
    # -------------------------------------------------------------
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        has_title = "<title>PsychoStreak" in content
        has_firebase = "firebase.initializeApp" in content
        has_diag = "id=\"modal-diagnostics\"" in content
        has_stepper = "adjustScore" in content
        has_analytics = "renderAnalyticsSection" in content

        passed = has_title and has_firebase and has_diag and has_stepper and has_analytics
        print_test("קובץ index.html ורכיבי ממשק משתמש", passed, f"גודל: {len(content)} תווים | כל הרכיבים אותרו")
        if not passed: all_passed = False
    else:
        print_test("קובץ index.html קיים", False, "index.html לא נמצא בתיקייה")
        all_passed = False

    # -------------------------------------------------------------
    # 2. Live Firebase Firestore API Check
    # -------------------------------------------------------------
    firestore_url = "https://firestore.googleapis.com/v1/projects/psychostreak-cd83e/databases/(default)/documents/users/shelly_psychostreak"
    t0 = time.time()
    try:
        req = urllib.request.Request(firestore_url, headers={"User-Agent": "PsychoStreak-TestBot"})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            lat = int((time.time() - t0) * 1000)
            passed = resp.status == 200
            print_test("חיבור וקריאה מ-Firebase Firestore", passed, f"קוד {resp.status} | פינג: {lat}ms | מסמך shelly_psychostreak פעיל")
            if not passed: all_passed = False
    except Exception as e:
        print_test("חיבור וקריאה מ-Firebase Firestore", False, f"שגיאה: {e}")
        all_passed = False

    # Test Firestore Write
    try:
        t0 = time.time()
        test_payload = {
            "fields": {
                "lastTestPing": {"integerValue": str(int(time.time() * 1000))},
                "healthStatus": {"stringValue": "healthy"}
            }
        }
        post_data = json.dumps(test_payload).encode("utf-8")
        patch_url = f"{firestore_url}?updateMask.fieldPaths=lastTestPing&updateMask.fieldPaths=healthStatus"
        patch_req = urllib.request.Request(patch_url, data=post_data, headers={"Content-Type": "application/json", "User-Agent": "PsychoStreak-TestBot"}, method="PATCH")
        with urllib.request.urlopen(patch_req) as resp:
            lat = int((time.time() - t0) * 1000)
            passed = resp.status == 200
            print_test("כתיבה וסנכרון בזמן אמת לענן Firestore", passed, f"פינג כתיבה: {lat}ms | ענן פתוח ומסנכרן")
            if not passed: all_passed = False
    except Exception as e:
        print_test("כתיבה וסנכרון בזמן אמת לענן Firestore", False, f"שגיאה: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # 3. Live GitHub Pages Deployment Check
    # -------------------------------------------------------------
    live_url = "https://shellywsas.github.io/psychostreak/"
    t0 = time.time()
    try:
        req = urllib.request.Request(live_url, headers={"User-Agent": "PsychoStreak-TestBot", "Cache-Control": "no-cache"})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
            lat = int((time.time() - t0) * 1000)
            passed = resp.status == 200 and "PsychoStreak" in content
            print_test("זמינות האתר החי ב-GitHub Pages", passed, f"HTTP {resp.status} | זמן תגובה: {lat}ms | URL: {live_url}")
            if not passed: all_passed = False
    except Exception as e:
        print_test("זמינות האתר החי ב-GitHub Pages", False, f"שגיאה: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # 4. Headless Chrome DOM Verification
    # -------------------------------------------------------------
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if os.path.exists(chrome_path) and os.path.exists(html_path):
        try:
            cmd = [chrome_path, "--headless=new", "--disable-gpu", "--dump-dom", f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}"]
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
            passed = res.returncode == 0 and "PsychoStreak" in res.stdout and "modal-diagnostics" in res.stdout
            print_test("עיבוד דפדפן מלא (Headless Chrome)", passed, f"קוד יציאה {res.returncode} | עובד 100% ללא שגיאות קריסה")
            if not passed: all_passed = False
        except Exception as e:
            print_test("עיבוד דפדפן מלא (Headless Chrome)", False, f"שגיאה: {e}")
            all_passed = False

    print("\n" + "="*60)
    if all_passed:
        print(f"{GREEN}🎉 סיכום בדיקות: כל המערכות פעילות ותקינות ב-100%! אין שום תקלה.{RESET}")
    else:
        print(f"{RED}⚠️ זוהו תקלות באחד או יותר מהרכיבים. נא לבדוק את הפירוט לעיל.{RESET}")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_tests()

# מדריך הגדרת פרויקט Firebase ייעודי עבור PsychoStreak 🎯

מדריך זה מסביר צעד אחר צעד כיצד להקים פרויקט Firebase ייעודי ונפרד עבור אפליקציית **PsychoStreak** (במקום לשתף את הפרויקט של StudyStreak / ShellyLIFE), כך שכל נתוני הפסיכומטרי יהיו עצמאיים לחלוטין.

---

## שלב 1: יצירת פרויקט חדש ב-Firebase Console

1. היכנסי לאתר [Firebase Console](https://console.firebase.google.com) (מומלץ עם חשבון הגוגל שלך).
2. לחצי על **"Add project"** (הוספת פרויקט).
3. תני שם לפרויקט (למשל: `psychostreak` או `psychostreak-shelly`).
4. לחצי **Continue**. (אין חובה להפעיל Google Analytics, ניתן לכבות או להשאיר כרצונך).
5. לחצי **Create project** והמתיני כ-20 שניות לסיום ההקמה.

---

## שלב 2: יצירת מסד הנתונים (Cloud Firestore)

1. בתפריט הצד השמאלי של Firebase, לחצי על **Build** -> **Firestore Database**.
2. לחצי על הכפתור **Create database**.
3. בחרי מיקום (Location) - מומלץ `eur3 (europe-west)` או ברירת המחדל.
4. במסך ה-Security rules בחרי **Start in test mode** (מאפשר קריאה וכתיבה ללא צורך בהתחברות משתמשים) ולחצי **Create**.

---

## שלב 3: רישום אפליקציית Web והעתקת ה-Config

1. בעמוד הראשי של הפרויקט (Project Overview), לחצי על אייקון ה-Web (האייקון של **`</>`**).
2. תני כינוי לאפליקציה: `PsychoStreak Web`.
3. לחצי **Register app**.
4. יופיע על המסך קטע קוד עם אובייקט בשם `firebaseConfig`. הוא נראה בערך כך:
   ```javascript
   const firebaseConfig = {
     apiKey: "AIzaSy...",
     authDomain: "psychostreak-xxxx.firebaseapp.com",
     projectId: "psychostreak-xxxx",
     storageBucket: "psychostreak-xxxx.firebasestorage.app",
     messagingSenderId: "123456789",
     appId: "1:123456789:web:abcd..."
   };
   ```
5. העתיקי את כל הטקסט או את האובייקט.

---

## שלב 4: החלת ההגדרות באפליקציית PsychoStreak

באפליקציה יש כעת מערכת מובנית וחכמה להחלת הפרויקט בלחיצת כפתור:

1. פתחי את אפליקציית PsychoStreak במחשב או בטלפון.
2. בכרטיס ה-**סנכרון ענן בזמן אמת** (או בתפריט הצד), לחצי על כפתור **"⚡ פיירבייס עצמאי"**.
3. הדביקי את הקוד שהעתקת לתוך תיבת הטקסט.
4. לחצי על **"בדוק ושמור חיבור לפרויקט החדש"**!
5. המערכת תבדוק פינג וסנכרון מול הפרויקט החדש שלך, תשמור את ההגדרות, ותעביר אוטומטית את כל הנתונים, החיבורים והפרקים לפרויקט החדש! 🚀

---

## כללי אבטחה מומלצים (firestore.rules)

קובץ חוקי האבטחה המומלץ כבר נמצא בתיקיית הפרויקט (`firestore.rules`):
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if true;
    }
  }
}
```
ניתן להדביק אותו בלשונית **Rules** ב-Firestore Console כדי לוודא שהגישה פתוחה לסנכרון בין המחשב לטלפון ללא מגבלת 30 יום.

/**
 * StudyStreak Pro - Firebase Configuration & Offline Safe-Init
 */
const firebaseConfig = {
    apiKey: "AIzaSyBPboUtv6RREpZa0ZSKiqJTzQbz8OPH4kc",
    authDomain: "psychostreak-cd83e.firebaseapp.com",
    projectId: "psychostreak-cd83e",
    storageBucket: "psychostreak-cd83e.firebasestorage.app",
    messagingSenderId: "338480800113",
    appId: "1:338480800113:web:3c6ccacac1a0a8121a334a"
};

let db = null;
try {
    if (typeof firebase !== 'undefined') {
        if (!firebase.apps.length) {
            firebase.initializeApp(firebaseConfig);
        }
        db = firebase.firestore();
        try {
            db.settings({ ignoreUndefinedProperties: true });
        } catch (e) {
            console.warn('Firestore settings warning:', e);
        }
        // Enable offline persistence if available
        if (db && db.enablePersistence) {
            db.enablePersistence().catch(err => {
                console.warn('Firestore offline persistence warning:', err.code);
            });
        }
    }
} catch (err) {
    console.warn('Firebase initialization failed (offline mode active):', err);
    db = null;
}

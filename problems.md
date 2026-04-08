# ⚠️ Problems Faced & Solutions

## 1. ModuleNotFoundError
**Issue:** Python couldn't find `src`  
**Solution:** Added sys.path fix

---

## 2. Slow LLM Response
**Issue:** 100+ seconds delay  
**Solution:**
- Reduced tokens
- Optimized prompt
- Used mistral for speed

---

## 3. API Response Error
**Issue:** Schema mismatch  
**Solution:** Standardized keys (`ai_feedback`)

---

## 4. Poor Output Structure
**Issue:** Unstructured AI response  
**Solution:** Improved prompt design

---

## 5. Sequential Execution Slow
**Issue:** Models running one by one  
**Solution:** Implemented parallel execution
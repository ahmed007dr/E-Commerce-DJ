import random

# تخزين الأكواد التي تم توليدها مسبقًا
used_codes = set()

def generate_code(length=8):
    data = '0123456789ABCDEFGHIJKLMNOPQRSTYVWXXYZ'
    
    while True:
        # توليد الكود العشوائي
        code = ''.join(random.choice(data) for x in range(length))
        
        # إذا كان الكود غير موجود في الأكواد المستخدمة، نعيده
        if code not in used_codes:
            used_codes.add(code)
            return code

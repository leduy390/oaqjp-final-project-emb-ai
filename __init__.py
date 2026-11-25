mkdir -p EmotionDetection
echo "from . import emotion_detection" > EmotionDetection/__init__.py
git add EmotionDetection/__init__.py
git commit -m "Add __init__.py to EmotionDetection package"
git push -u origin HEAD

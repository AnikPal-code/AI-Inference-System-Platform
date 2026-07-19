from transformers import pipeline

_classifier = None

def get_classifier():
    global _classifier

    if _classifier is None:
        _classifier = pipeline(
            task="image-classification",
            model="google/vit-base-patch16-224",
            framework="pt",
            device=-1
        )

    return _classifier


def classify_image(image):
    classifier = get_classifier()
    return classifier(image)[0]
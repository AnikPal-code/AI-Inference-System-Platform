from transformers import pipeline

classifier = pipeline(
    task="image-classification",
    model="google/vit-base-patch16-224",
    framework="pt"  # Force PyTorch framework
)


def classify_image(image):
    return classifier(image)[0]

def TextReader(label_image_path):
    """
    TextReader() turns a nutrition fact label into raw text description
    :param label_image_path: path to the nutrition fact label image
    :return: a string of text description from nutrition fact label, splitted by '\t'
    """
    import io
    import os
    from google.cloud import vision
    from google.cloud.vision import types
    client = vision.ImageAnnotatorClient()
    # [END migration_client]
    # The name of the image file to annotate
    file_name = os.path.join(os.path.dirname(__file__),label_image_path)
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description

if __name__ == '__main__':
    result = TextReader('test_image\\testlabel.jpg')
    print(result)
    result = result.split('\n')
    print(result)
    print(type(result))

    labels = ['Calories','Calories from Fat','Total Fat','Cholesterol','Sodium','Potassium','Total Carbohydrate','Protein']
    label_dict = {}
    for i in range(len(labels)):
        label_dict[labels[i]] = None
    for i in result:
        for label in label_dict:
            if label in i:
                label_dict[label] = i
    print(label_dict)

if __name__ == '__main__':
    pass

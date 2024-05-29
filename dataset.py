import json 
import os 
import pandas as pd 

images_path = "images"
kanji_csv = "extracted_data.csv"

def convert_to_huggingface_format():
    """Huggingface requires a particular data / directory format for StableDiffusion 
    https://huggingface.co/docs/datasets/v2.4.0/en/image_load#imagefolder-with-metadata
    
    We take our scraped data and fit it to this format to allow for a simple fine-tuning. 
    """
    import ast
    import jsonlines
    
    dataframe = pd.read_csv(kanji_csv)
    with jsonlines.open('data/train/metadata.jsonl', mode='w') as writer:
        for i, row in enumerate(dataframe.iterrows()):

            impath = str(i).zfill(5) + ".png"
            # This can be a list, single value, or empty
            meanings = ast.literal_eval(dataframe.Meanings[i])
            # print(meanings)
            if len(meanings) == 0:
                entry = {"file_name":impath, "text":" "}
                writer.write(entry)
            for m in meanings:
                # We will fine-tune with the same image multiple times if it has multiple meanings. 
                entry = {"file_name":impath, "text":m}
                writer.write(entry)

def zfill_images():
    """Simply loop through the folder of SVG images and rename with zfill 
    Example:  01.png -> 00001.png   /    18.png -> 00018.png
    """
    import os 
    for impath in os.listdir(images_path):
        imid = str(impath.split('.')[0])
        newpath = imid.zfill(5) + ".png"
        os.rename(f"images/{impath}", f"images/{newpath}")
    